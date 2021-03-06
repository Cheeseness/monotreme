"""
Copyright (C) 2007 2010 2011 Cisco Systems

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
# PySNMP SMI module. Autogenerated from smidump -f python AIRPORT-BASESTATION-3-MIB
# by libsmi2pysnmp-0.0.7-alpha at Sat Sep  8 12:42:29 2007,
# Python version (2, 2, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols('ASN1', 'Integer', 'ObjectIdentifier', 'OctetString')
( PhysAddress, ) = mibBuilder.importSymbols('RFC1213-MIB', 'PhysAddress')
( Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, Unsigned32, enterprises, ) = mibBuilder.importSymbols('SNMPv2-SMI', 'Bits', 'Counter32', 'Counter64', 'Gauge32', 'Integer32', 'IpAddress', 'ModuleIdentity', 'MibIdentifier', 'MibScalar', 'MibTable', 'MibTableRow', 'MibTableColumn', 'Opaque', 'TimeTicks', 'Unsigned32', 'enterprises')
( DisplayString, ) = mibBuilder.importSymbols('SNMPv2-TC', 'DisplayString')

# Objects

apple = MibIdentifier((1, 3, 6, 1, 4, 1, 63))
airport = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501))
baseStation3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 63, 501, 3)).setRevisions(('2003-01-16 00:01',))
abs3SysConf = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 1))
sysConfName = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 1), DisplayString()).setMaxAccess('readwrite').setDescription('Configured name of the AirPort Base Station.')
sysConfContact = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 2), DisplayString()).setMaxAccess('readwrite').setDescription('Configured name of the contact for the AirPort Base Station.')
sysConfLocation = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 3), DisplayString()).setMaxAccess('readwrite').setDescription('Configured name of where the AirPort Base Station is located.')
sysConfUptime = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 4), Integer32()).setMaxAccess('readonly').setDescription('Length of time, in seconds, the AirPort Base Station has been running.')
sysConfFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 1, 5), DisplayString()).setMaxAccess('readonly').setDescription('Current firmware revision running on the AirPort Base Station.')
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 2))
wirelessNumber = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 1), Integer32()).setMaxAccess('readonly').setDescription('The number of wireless clients associated with this AP.')
wirelessClientsTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2)).setDescription('A list of wireless clients.')
wirelessClient = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1)).setIndexNames((0, 'AIRPORT-BASESTATION-3-MIB', 'wirelessPhysAddress')).setDescription('A wireless client entry containing information about the client.')
wirelessPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 1), PhysAddress()).setMaxAccess('readonly').setDescription('The MAC address of the wireless client.')
wirelessType = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(('sta', 1), ('wds', 2), ))).setMaxAccess('readonly').setDescription('The type of wireless client node.')
wirelessDataRates = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess('readonly').setDescription('The data rates available for the wireless client.')
wirelessTimeAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 4), Integer32()).setMaxAccess('readonly').setDescription('The time that this wireless client associated.')
wirelessLastRefreshTime = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 5), Integer32()).setMaxAccess('readonly').setDescription('The number of seconds since the client reported its statistics to the AirPort Base Station (-1 if never refreshed or not supported).')
wirelessStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 6), Integer32()).setMaxAccess('readonly').setDescription('The signal strength reported by the wireless client (-1 if not supported).')
wirelessNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 7), Integer32()).setMaxAccess('readonly').setDescription('The noise reported by the wireless client (-1 if not supported).')
wirelessRate = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 8), Integer32()).setMaxAccess('readonly').setDescription('The rate reported by the wireless client (-1 if not supported).')
wirelessNumRX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 9), Integer32()).setMaxAccess('readonly').setDescription('The number of packets received reported by the wireless client (-1 if not supported).')
wirelessNumTX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 10), Integer32()).setMaxAccess('readonly').setDescription('The number of packets transmitted reported by this wireless client (-1 if not supported).')
wirelessNumRXErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 11), Integer32()).setMaxAccess('readonly').setDescription('The number of errors encountered receiving packets reported by this wireless client (-1 if not supported).')
wirelessNumTXErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 2, 2, 1, 12), Integer32()).setMaxAccess('readonly').setDescription('The number of errors encountered transmitting packets reported by this wireless client (-1 if not supported).')
dhcpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 3))
dhcpNumber = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 1), Integer32()).setMaxAccess('readonly').setDescription('The number of DHCP clients served by the AirPort base station.')
dhcpClientsTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2)).setDescription('A list of DHCP clients.')
dhcpClient = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1)).setIndexNames((0, 'AIRPORT-BASESTATION-3-MIB', 'dhcpPhysAddress')).setDescription('A DHCP client entry containing information about the client.')
dhcpPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 1), PhysAddress()).setMaxAccess('readonly').setDescription('The MAC address of the DHCP client.')
dhcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 2), IpAddress()).setMaxAccess('readonly').setDescription('The IP address of the DHCP client.')
dhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 3), OctetString()).setMaxAccess('readonly').setDescription('The DHCP client ID of the DHCP client.')
dhcpLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 3, 2, 1, 4), Integer32()).setMaxAccess('readonly').setDescription('The lease time for the DHCP client.')
physicalInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 63, 501, 3, 4))
physicalInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 1), Integer32()).setMaxAccess('readonly').setDescription("The number of physical interfaces on the AirPort Base Station.  This is different than the number of IP interfaces, as reported by the system MIBs, as the AirPort's bridge typically multiplexes two or more interfaces.")
physicalInterfacesTable = MibTable((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2)).setDescription('List of physical interfaces on the AirPort Base Station.')
physicalInterface = MibTableRow((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1)).setIndexNames((0, 'AIRPORT-BASESTATION-3-MIB', 'physicalInterfaceIndex')).setDescription('Entry containing data about the physical interface on the AirPort Base Station.')
physicalInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 1), Integer32()).setMaxAccess('readonly').setDescription('A unique value for each physical interface.  Its value ranges between 1 and the value of physicalInterfaceCount.')
physicalInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 2), OctetString()).setMaxAccess('readonly').setDescription('The name of the physical interface.')
physicalInterfaceUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 3), Integer32()).setMaxAccess('readonly').setDescription('The unit number of the physical interface.')
physicalInterfaceSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 4), Integer32()).setMaxAccess('readonly').setDescription('The speed, in bits per second, of the interface.')
physicalInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,0,)).subtype(namedValues=namedval.NamedValues(('linkDown', 0), ('linkUp', 1), ))).setMaxAccess('readonly').setDescription('The status of this interface.')
physicalInterfaceDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,1,)).subtype(namedValues=namedval.NamedValues(('half', 0), ('full', 1), ))).setMaxAccess('readonly').setDescription('The duplex-state of this interface.')
physicalInterfaceNumTX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 7), Integer32()).setMaxAccess('readonly').setDescription('The number of packets transmitted on this interface.')
physicalInterfaceNumRX = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 8), Integer32()).setMaxAccess('readonly').setDescription('The number of packets received on this interface.')
physicalInterfaceNumTXError = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 9), Integer32()).setMaxAccess('readonly').setDescription('The number of errors during transmission on this interface.')
physicalInterfaceNumRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 63, 501, 3, 4, 2, 1, 10), Integer32()).setMaxAccess('readonly').setDescription('The number of errors during reception on this interface.')

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols('AIRPORT-BASESTATION-3-MIB', PYSNMP_MODULE_ID=baseStation3)

# Objects
mibBuilder.exportSymbols('AIRPORT-BASESTATION-3-MIB', apple=apple, airport=airport, baseStation3=baseStation3, abs3SysConf=abs3SysConf, sysConfName=sysConfName, sysConfContact=sysConfContact, sysConfLocation=sysConfLocation, sysConfUptime=sysConfUptime, sysConfFirmwareVersion=sysConfFirmwareVersion, wireless=wireless, wirelessNumber=wirelessNumber, wirelessClientsTable=wirelessClientsTable, wirelessClient=wirelessClient, wirelessPhysAddress=wirelessPhysAddress, wirelessType=wirelessType, wirelessDataRates=wirelessDataRates, wirelessTimeAssociated=wirelessTimeAssociated, wirelessLastRefreshTime=wirelessLastRefreshTime, wirelessStrength=wirelessStrength, wirelessNoise=wirelessNoise, wirelessRate=wirelessRate, wirelessNumRX=wirelessNumRX, wirelessNumTX=wirelessNumTX, wirelessNumRXErrors=wirelessNumRXErrors, wirelessNumTXErrors=wirelessNumTXErrors, dhcpServer=dhcpServer, dhcpNumber=dhcpNumber, dhcpClientsTable=dhcpClientsTable, dhcpClient=dhcpClient, dhcpPhysAddress=dhcpPhysAddress, dhcpIpAddress=dhcpIpAddress, dhcpClientID=dhcpClientID, dhcpLeaseTime=dhcpLeaseTime, physicalInterfaces=physicalInterfaces, physicalInterfaceCount=physicalInterfaceCount, physicalInterfacesTable=physicalInterfacesTable, physicalInterface=physicalInterface, physicalInterfaceIndex=physicalInterfaceIndex, physicalInterfaceName=physicalInterfaceName, physicalInterfaceUnit=physicalInterfaceUnit, physicalInterfaceSpeed=physicalInterfaceSpeed, physicalInterfaceState=physicalInterfaceState, physicalInterfaceDuplex=physicalInterfaceDuplex, physicalInterfaceNumTX=physicalInterfaceNumTX, physicalInterfaceNumRX=physicalInterfaceNumRX, physicalInterfaceNumTXError=physicalInterfaceNumTXError, physicalInterfaceNumRXError=physicalInterfaceNumRXError)

