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
# exec 5>PANDUIT-APPS-POWER-MIB.header 2>&5
# smidump --preload=./PANDUIT-REG.txt --preload=./PANDUIT-TC.txt --preload=./PANDUIT-COMMON-MIB.txt --preload=./PANDUIT-PRODUCTS-PANEL-COMMON-MIB.txt -f python PANDUIT-APPS-POWER-MIB.txt | ../libsmi2pysnmp >PANDUIT-APPS-POWER-MIB.pysnmp
# cat PANDUIT-APPS-POWER-MIB.header | sed 's/^/# /g' >PANDUIT-APPS-POWER-MIB.py
# cat PANDUIT-APPS-POWER-MIB.pysnmp >>PANDUIT-APPS-POWER-MIB.py
# rm PANDUIT-APPS-POWER-MIB.pysnmp
# rm PANDUIT-APPS-POWER-MIB.header
# ----------------------------------------------------------------------------
# ==========================================================================
# PySNMP SMI module. Autogenerated from smidump -f python PANDUIT-APPS-POWER-MIB
# by libsmi2pysnmp-0.0.7-alpha-rz2 at Tue Oct 16 16:30:53 2007,
# Python version (2, 2, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols('ASN1', 'Integer', 'ObjectIdentifier', 'OctetString')
( panduitIdentificationMAC, ) = mibBuilder.importSymbols('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC')
( panduitProdPanelCommonRackId, panduitProdPanelCommonRackPositionId, ) = mibBuilder.importSymbols('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId', 'panduitProdPanelCommonRackPositionId')
( panduitApps, ) = mibBuilder.importSymbols('PANDUIT-REG', 'panduitApps')
( PanduitPoEVoltageType, ) = mibBuilder.importSymbols('PANDUIT-TC', 'PanduitPoEVoltageType')
( pethMainPseConsumptionPower, pethMainPseUsageThreshold, ) = mibBuilder.importSymbols('POWER-ETHERNET-MIB', 'pethMainPseConsumptionPower', 'pethMainPseUsageThreshold')
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols('SNMPv2-CONF', 'ModuleCompliance', 'NotificationGroup', 'ObjectGroup')
( sysName, ) = mibBuilder.importSymbols('SNMPv2-MIB', 'sysName')
( Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols('SNMPv2-SMI', 'Bits', 'Counter32', 'Counter64', 'Gauge32', 'Integer32', 'IpAddress', 'ModuleIdentity', 'MibIdentifier', 'NotificationType', 'ObjectIdentity', 'MibScalar', 'MibTable', 'MibTableRow', 'MibTableColumn', 'Opaque', 'TimeTicks', 'Unsigned32')
( DisplayString, ) = mibBuilder.importSymbols('SNMPv2-TC', 'DisplayString')

# Objects

panduitAppsPower = ModuleIdentity((1, 3, 6, 1, 4, 1, 19536, 7, 3)).setRevisions(('2005-04-29 00:00',))
panduitAppsPowerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0))
panduitPowerVoltage = MibScalar((1, 3, 6, 1, 4, 1, 19536, 7, 3, 1), PanduitPoEVoltageType()).setMaxAccess('readonly').setDescription('Input voltage to the managed object.')
panduitPowerVoltageA = MibScalar((1, 3, 6, 1, 4, 1, 19536, 7, 3, 2), PanduitPoEVoltageType()).setMaxAccess('readonly').setDescription('Input voltage at Power connector A.')
panduitPowerVoltageB = MibScalar((1, 3, 6, 1, 4, 1, 19536, 7, 3, 3), PanduitPoEVoltageType()).setMaxAccess('readonly').setDescription('Input voltage at Power Connector B.')
panduitPowerSourceName = MibScalar((1, 3, 6, 1, 4, 1, 19536, 7, 3, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 64))).setMaxAccess('readwrite').setDescription('The name of the device supplying power to the managed object.')
panduitAppsPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 7, 3, 5))
panduitAppsPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 7, 3, 5, 1))
panduitAppsPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 19536, 7, 3, 5, 2))

# Augmentions

# Notifications

panduitPowerAboveThreshold = NotificationType((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0, 1)).setObjects(('SNMPv2-MIB', 'sysName'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC'), ('POWER-ETHERNET-MIB', 'pethMainPseConsumptionPower'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('POWER-ETHERNET-MIB', 'pethMainPseUsageThreshold'), )
panduitPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0, 3)).setObjects(('SNMPv2-MIB', 'sysName'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC'), )
panduitPowerBelowThreshold = NotificationType((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0, 2)).setObjects(('SNMPv2-MIB', 'sysName'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC'), ('POWER-ETHERNET-MIB', 'pethMainPseConsumptionPower'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('POWER-ETHERNET-MIB', 'pethMainPseUsageThreshold'), )
panduitPowerHigh = NotificationType((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0, 5)).setObjects(('SNMPv2-MIB', 'sysName'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerVoltage'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC'), )
panduitPowerLow = NotificationType((1, 3, 6, 1, 4, 1, 19536, 7, 3, 0, 4)).setObjects(('SNMPv2-MIB', 'sysName'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackId'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerVoltage'), ('PANDUIT-PRODUCTS-PANEL-COMMON-MIB', 'panduitProdPanelCommonRackPositionId'), ('PANDUIT-COMMON-MIB', 'panduitIdentificationMAC'), )

# Groups

panduitAppsPowerNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19536, 7, 3, 5, 1, 2)).setObjects(('PANDUIT-APPS-POWER-MIB', 'panduitPowerAboveThreshold'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerFailure'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerBelowThreshold'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerHigh'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerLow'), )
panduitAppsPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19536, 7, 3, 5, 1, 1)).setObjects(('PANDUIT-APPS-POWER-MIB', 'panduitPowerSourceName'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerVoltage'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerVoltageA'), ('PANDUIT-APPS-POWER-MIB', 'panduitPowerVoltageB'), )

# Exports

# Module identity
mibBuilder.exportSymbols('PANDUIT-APPS-POWER-MIB', PYSNMP_MODULE_ID=panduitAppsPower)

# Objects
mibBuilder.exportSymbols('PANDUIT-APPS-POWER-MIB', panduitAppsPower=panduitAppsPower, panduitAppsPowerNotifications=panduitAppsPowerNotifications, panduitPowerVoltage=panduitPowerVoltage, panduitPowerVoltageA=panduitPowerVoltageA, panduitPowerVoltageB=panduitPowerVoltageB, panduitPowerSourceName=panduitPowerSourceName, panduitAppsPowerConformance=panduitAppsPowerConformance, panduitAppsPowerGroups=panduitAppsPowerGroups, panduitAppsPowerCompliances=panduitAppsPowerCompliances)

# Notifications
mibBuilder.exportSymbols('PANDUIT-APPS-POWER-MIB', panduitPowerAboveThreshold=panduitPowerAboveThreshold, panduitPowerFailure=panduitPowerFailure, panduitPowerBelowThreshold=panduitPowerBelowThreshold, panduitPowerHigh=panduitPowerHigh, panduitPowerLow=panduitPowerLow)

# Groups
mibBuilder.exportSymbols('PANDUIT-APPS-POWER-MIB', panduitAppsPowerNotificationGroup=panduitAppsPowerNotificationGroup, panduitAppsPowerGroup=panduitAppsPowerGroup)
