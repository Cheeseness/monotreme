/*
	Copyright (c) 2004-2009, The Dojo Foundation All Rights Reserved.
	Available via Academic Free License >= 2.1 OR the modified BSD license.
	see: http://dojotoolkit.org/license for details
*/


if(!dojo._hasResource["dojox.drawing.stencil.Line"]){ //_hasResource checks added by build. Do not use _hasResource directly in your code.
dojo._hasResource["dojox.drawing.stencil.Line"] = true;
dojo.provide("dojox.drawing.stencil.Line");

dojox.drawing.stencil.Line = dojox.drawing.util.oo.declare(
	// summary:
	//		Creates a dojox.gfx Line based on data or points provided.
	//
	dojox.drawing.stencil._Base,
	function(options){
		// summary:
		//		constructor
	},
	{
		type:"dojox.drawing.stencil.Line",
		anchorType: "single",
		baseRender:true,
		
/*=====
StencilData: {
	// summary:
	//		The data used to create the dojox.gfx Shape
	// 	x1: Number
	//		First point x
	// 	y1: Number
	//		First point y
	// 	x2: Number
	//		Second point x
	// 	y2: Number
	//		Second point y
	
	// ALTERNATIVE:
	
	// 	x: Number
	//		First point x
	// 	y: Number
	//		First point y
	// 	angle: Number
	//		angle of line
	// 	radius: Number
	//		length of line
},

StencilPoints: [
	// summary:
	//		An Array of dojox.__StencilPoint objects that describe the Stencil
	// 	0: Object
	//		First point
	// 	1: Object
	//		Second point
],
=====*/
		
		dataToPoints: function(o){
			//summary:
			//		Converts data to points.
			o = o || this.data;
			if(o.radius || o.angle){
				// instead of using x1,x2,y1,y1,
				// it's been set as x,y,angle,radius
				
				// forward angle:
				// 90 -> 90
				// 180 -> 0
				// 0 -> 180
				// 270 -> 270
				// 120 -> 60
				// 40 -> 140
				// 315 -> 220
				// 200 -> 340
				
				// reversing the angle for display: 0 -> 180, 90 -> 270
				//angle = 180 - angle; angle = angle==360 ? 0 : angle;
				
				var was = o.angle
				o.angle = (180-o.angle)<0 ? 180-o.angle+360 : 180-o.angle;
				
				//console.log(" ---- angle:", was, "to:", o.angle)
				var pt = this.util.pointOnCircle(o.x,o.y,o.radius,o.angle);
				//console.log(" ---- pts:", pt.x, pt.y);
				this.data = o = {
					x1:o.x,
					y1:o.y,
					x2:pt.x,
					y2:pt.y
				}
				
			}
			this.points = [
				{x:o.x1, y:o.y1},
				{x:o.x2, y:o.y2}
			];
			return this.points;
		},
		pointsToData: function(p){
			// summary:
			//		Converts points to data
			p = p || this.points;
			this.data = {
				x1: p[0].x,
				y1: p[0].y,
				x2: p[1].x,
				y2: p[1].y
			};
			return this.data;
		},
		
		_create: function(/*String*/shp, /*StencilData*/d, /*Object*/sty){
			// summary:
			//		Creates a dojox.gfx.shape based on passed arguments.
			//		Can be called many times by implementation to create
			//		multiple shapes in one stencil.
			//
			this.remove(this[shp]);
			this[shp] = this.container.createLine(d)
				.setStroke(sty);
			this._setNodeAtts(this[shp]);
		},
		
		render: function(){
			// summary:
			//		Renders the 'hit' object (the shape used for an expanded
			//		hit area and for highlighting) and the'shape' (the actual
			//		display object).
			//
			this.onBeforeRender(this);
			this.renderHit && this._create("hit", this.data, this.style.currentHit);
			this._create("shape", this.data, this.style.current);
			
		}		
		
	}
);

dojox.drawing.register({
	name:"dojox.drawing.stencil.Line"	
}, "stencil");

}
