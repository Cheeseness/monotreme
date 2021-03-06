"""
Copyright (C) 2010 2011 Cisco Systems

This program is free software; you can redistribute it and/or         
modify it under the terms of the GNU General Public License         
as published by the Free Software Foundation; either version 2         
of the License, or (at your option) any later version.         
    
This program is distributed in the hope that it will be useful,         
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
GNU General Public License for more details.         
    
You should have received a copy of the GNU General Public License         
along with this program; if not, write to:         
The Free Software Foundation, Inc.         
59 Temple Place - Suite 330         
Boston, MA  02111-1307, USA.         
    
As a special exception, if other files instantiate classes, templates  
or use macros or inline functions from this project, or you compile         
this file and link it with other works to produce a work based         
on this file, this file does not by itself cause the resulting         
work to be covered by the GNU General Public License. However         
the source code for this file must still be made available in         
accordance with section (3) of the GNU General Public License.         
    
This exception does not invalidate any other reasons why a work         
based on this file might be covered by the GNU General Public         
License.
"""
# ============================================================================
# Created via /home/mevans/source/pysnmp-experiments/Panduit-MIBs-1/PANDUIT.sh:
# 
# Use smidump and RZ's custom version of libsmi2pysnmp
# which was part of /home/mevans/source/pysnmp-experiments/ at the time of
# execution.
# 
# Essentially:
# 
# exec 5>PANDUIT-PRODUCTS-PANEL-COMMON-MIB.header 2>&5
# smidump --preload=./PANDUIT-REG.txt --preload=./PANDUIT-TC.txt -f python PANDUIT-PRODUCTS-PANEL-COMMON-MIB.txt | ../libsmi2pysnmp >PANDUIT-PRODUCTS-PANEL-COMMON-MIB.pysnmp
# cat PANDUIT-PRODUCTS-PANEL-COMMON-MIB.header | sed 's/^/# /g' >PANDUIT-PRODUCTS-PANEL-COMMON-MIB.py
# cat PANDUIT-PRODUCTS-PANEL-COMMON-MIB.pysnmp >>PANDUIT-PRODUCTS-PANEL-COMMON-MIB.py
# rm PANDUIT-PRODUCTS-PANEL-COMMON-MIB.pysnmp
# rm PANDUIT-PRODUCTS-PANEL-COMMON-MIB.header
# ----------------------------------------------------------------------------
# PANDUIT-PRODUCTS-PANEL-COMMON-MIB.txt:47: revision not in reverse chronological order
# ==========================================================================
# PySNMP SMI module. Autogenerated from smidump -f python PANDUIT-PRODUCTS-PANEL-COMMON-MIB
# by libsmi2pysnmp-0.0.7-alpha-rz2 at Tue Oct 16 16:30:54 2007,
# Python version (2, 2, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols('ASN1', 'Integer', 'ObjectIdentifier', 'OctetString')
( panduitProdPanel, ) = mibBuilder.importSymbols('PANDUIT-REG', 'panduitProdPanel')
( PanduitLongDisplayString, ) = mibBuilder.importSymbols('PANDUIT-TC', 'PanduitLongDisplayString')
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols('SNMPv2-CONF', 'ModuleCompliance', 'ObjectGroup')
( Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols('SNMPv2-SMI', 'Bits', 'Counter32', 'Counter64', 'Gauge32', 'Integer32', 'IpAddress', 'ModuleIdentity', 'MibIdentifier', 'ObjectIdentity', 'MibScalar', 'MibTable', 'MibTableRow', 'MibTableColumn', 'Opaque', 'TimeTicks', 'Unsigned32')
( DisplayString, ) = mibBuilder.importSymbols('SNMPv2-TC', 'DisplayString')

# Objects

panduitProdPanelCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1)).setRevisions(('2005-04-27 00:00','2005-03-01 00:00',))
panduitProdPanelCommonRackId = MibScalar((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 64))).setMaxAccess('readwrite').setDescription('An identifier for the rack used to mount the panel.')
panduitProdPanelCommonRackPositionId = MibScalar((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 45))).setMaxAccess('readwrite').setDescription("The panel's location in the rack, expressed as \na rack position number.")
panduitProdPanelCommonLocation = MibScalar((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 3), PanduitLongDisplayString()).setMaxAccess('readwrite').setDescription('An object for the location of the Panel.')
panduitProdPanelCommonPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 64))).setMaxAccess('readwrite').setDescription('The name of the Power supply associated with the Panel.')
panduitProdPanelCommonPortLocTable = MibTable((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 5)).setDescription('A list of work area locations for each port in the panel.')
panduitProdPanelCommonPortLocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 5, 1)).setIndexNames((0, 'PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonPortLocIndex')).setDescription('A row in the Port Location Table.')
panduitProdPanelCommonPortLocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess('noaccess').setDescription('Port Location Table Index.')
panduitProdPanelCommonPortLocLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 5, 1, 2), PanduitLongDisplayString()).setMaxAccess('readwrite').setDescription('The work area location.')
panduitProdPanelCommonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 6))
panduitProdPanelCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 6, 1))
panduitProdPanelCommonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 6, 2))

# Augmentions

# Groups

panduitProdPanelCommonInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 6, 1, 1)).setObjects(('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonPowerSource'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonLocation'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonPortLocLocation'), )
panduitProdPanelCommonInfo2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 19536, 3, 1, 1, 6, 1, 2)).setObjects(('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), )

# Exports

# Module identity
mibBuilder.exportSymbols('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', PYSNMP_MODULE_ID=panduitProdPanelCommon)

# Objects
mibBuilder.exportSymbols('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', panduitProdPanelCommon=panduitProdPanelCommon, panduitProdPanelCommonRackId=panduitProdPanelCommonRackId, panduitProdPanelCommonRackPositionId=panduitProdPanelCommonRackPositionId, panduitProdPanelCommonLocation=panduitProdPanelCommonLocation, panduitProdPanelCommonPowerSource=panduitProdPanelCommonPowerSource, panduitProdPanelCommonPortLocTable=panduitProdPanelCommonPortLocTable, panduitProdPanelCommonPortLocEntry=panduitProdPanelCommonPortLocEntry, panduitProdPanelCommonPortLocIndex=panduitProdPanelCommonPortLocIndex, panduitProdPanelCommonPortLocLocation=panduitProdPanelCommonPortLocLocation, panduitProdPanelCommonConformance=panduitProdPanelCommonConformance, panduitProdPanelCommonGroups=panduitProdPanelCommonGroups, panduitProdPanelCommonCompliances=panduitProdPanelCommonCompliances)

# Groups
mibBuilder.exportSymbols('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', panduitProdPanelCommonInfoGroup=panduitProdPanelCommonInfoGroup, panduitProdPanelCommonInfo2Group=panduitProdPanelCommonInfo2Group)
