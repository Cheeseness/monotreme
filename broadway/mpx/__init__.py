"""
Copyright (C) 2001 2002 2003 2010 2011 Cisco Systems

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
from mpx._properties import properties
from mpx._properties import Properties
from mpx._properties import PACKAGES as packages
import _python
import os as _os

_os.umask(0007) # Only user and group can read files created by the framework.

if properties.get_boolean('STRICT_COMPLIANCE',0):
    class StartNewThreadAssertion:
        def __init__(self, module_name):
            self.message = ('STRICT_COMPLIANCE disallows %s.start_new_thread.'
                            % module_name)
            return
        def __call__(self, *args, **keywords):
             raise AssertionError(self.message)
    _python.python_thread.start_new_thread = StartNewThreadAssertion('thread')
    _python.thread.start_new_thread = StartNewThreadAssertion('_python.thread')
    _python.python_thread.start_new = StartNewThreadAssertion('thread')
    _python.thread.start_new = StartNewThreadAssertion('_python.thread')
