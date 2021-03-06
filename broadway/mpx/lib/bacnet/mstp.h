/*
Copyright (C) 2003 2010 2011 Cisco Systems

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
*/
// mstp.h: header file for BACnet MSTP datalink layer adapter functions. 
// Communicate between MFW and n_mstp ldisc.

#ifndef __MSTP_H__
#define __MSTP_H__

#define BACNET_MAX_APDU_MSTP  3

int open_mstp(const char *name, struct ADDR *addr, int fd_mstp);
int send_mstp(int fd_mstp,
	     const struct ADDR *source,
	     const struct ADDR *destination,
	     struct BACNET_BUFFER *bnb);
int recv_mstp(int fd_mstp, struct ADDR *source, struct BACNET_BUFFER *bnb);
int close_mstp(int fd_mstp);

#endif // __MSTP_H__
