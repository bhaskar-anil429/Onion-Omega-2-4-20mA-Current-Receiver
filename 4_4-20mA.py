# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP3428
# This code is designed to work with the MCP3428 4-20mA current receiver board available from ControlEverything.co
# https://shop.controleverything.com/collections/4-20-ma-current-loop-input/products/4-20ma-current-receiver-4-channel
# https://shop.controleverything.com/collections/4-20-ma-current-loop-input/products/4-channel-4-20ma-current-receiver-for-iot
from OmegaExpansion import onionI2C
import time
DL = 0
DL1 = 0.01
# Get I2C bus
i2c = onionI2C.OnionI2C()

# MCP3428 address, 0x68(104)
# Send configuration command
while True:
#0x10(16)Continuous conversion mode, Channel-1, 12-bit Resolution
        data = [0x10]
        i2c.write(0x68, data)
        time.sleep(DL1)
# MCP3428 address, 0x68(104)
# Read data back from 0x00(0), 2 bytes
# raw_adc MSB, raw_adc LSB
        data = i2c.readBytes(0x68, 0x00, 2)

# Convert the data to 12-bits
        raw_adc = (data[0] & 0x0F) * 256 + data[1]
        if raw_adc > 2047 :
                raw_adc -= 4095
        current = (raw_adc * 0.0221)
# Output data to screen
        print "Current Input at Channel One is    : %.3f" %current
        time.sleep(DL)
#0x30 Continuous conversion mode, Channel-2, 12-bit Resolution
        data = [0x30]
        i2c.write(0x68, data)
        time.sleep(DL1)
# MCP3428 address, 0x68(104)
# Read data back from 0x00(0), 2 bytes
# raw_adc MSB, raw_adc LSB
        data = i2c.readBytes(0x68, 0x00, 2)

# Convert the data to 12-bits
        raw_adc = (data[0] & 0x0F) * 256 + data[1]
        if raw_adc > 2047 :
                raw_adc -= 4095
        current = (raw_adc * 0.0221)
# Output data to screen                                           
        print "Current Input at Channel Two is    : %.3f" %current
        time.sleep(DL)                                            
                                                                  
#0x50 Continuous conversion mode, Channel-3, 12-bit Resolution    
        data = [0x50]                                             
        i2c.write(0x68, data)                                     
        time.sleep(DL1)                                           
# MCP3428 address, 0x68(104)                                      
# Read data back from 0x00(0), 2 bytes                            
# raw_adc MSB, raw_adc LSB                                        
        data = i2c.readBytes(0x68, 0x00, 2)                       
                                                                  
# Convert the data to 12-bits                                     
        raw_adc = (data[0] & 0x0F) * 256 + data[1]                
        if raw_adc > 2047 :                                       
                raw_adc -= 4095                                   
        current = (raw_adc * 0.0221)                              
# Output data to screen                                           
        print "Current Input at Channel Three is  : %.3f" %current
        time.sleep(DL)                                            
                                                                  
#0x70 Continuous conversion mode, Channel-4, 12-bit Resolution    
        data = [0x70]                                             
        i2c.write(0x68, data)                                     
        time.sleep(DL1)                                           
# MCP3428 address, 0x68(104)                                      
# Read data back from 0x00(0), 2 bytes                            
# raw_adc MSB, raw_adc LSB                                        
        data = i2c.readBytes(0x68, 0x00, 2)                       
                                                                  
# Convert the data to 12-bits                                     
        raw_adc = (data[0] & 0x0F) * 256 + data[1]                
        if raw_adc > 2047 :                                       
                raw_adc -= 4095                                   
        current = (raw_adc * 0.0221)                              
# Output data to screen                                           
        print "Current Input at Channel Four is   : %.3f" %current
        time.sleep(DL)                                            
