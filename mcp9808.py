# -*- coding: utf-8 -*-
from __future__ import division
import sys
import Adafruit_I2C as ada_i2c
from registers import MCP9808_Register

class MCP9808:
  __manID = 0
  __deviceID = 0
  criticalFlag = 0
  upperFlag = 0
  lowerFlag = 0

  def __init__(self, address = None):
    self.register = MCP9808_Register()
    if(address == None):
      self.__address = self.register.I2CADDR_DEFAULT
    elif(address < 0x18 or address > 0x1F):
      raise RuntimeError("Address (%s) must be between 0x18 and 0x1F (See section 3.5 of MCP9808 datasheet)" % hex(address))
    else:
      self.__address = address

    self.__i2c = ada_i2c.Adafruit_I2C(self.__address)


  def begin(self):
    self.reset()
    self.__manID = self.readU16(self.register.MANUF_ID)
    self.__deviceID = self.readU16(self.register.DEVICE_ID)
    if(self.__manID != 0x0054):
      raise RuntimeError("Wrong Manufacturer ID: %s. (Should be 0x5400. Check I2C Address)" %  hex(self.__manID))

    if(self.__deviceID != 0x4):
      raise RuntimeError("Wrong Device ID: %s. (Should be 0x4. Check I2C Address)" %  hex(self.__deviceID))



  def reset(self):
    self.write16(self.register.CONFIG, 0x0000)
    self.write16(self.register.UPPER_TEMP, 0x0000)
    self.write16(self.register.LOWER_TEMP, 0x0000)
    self.write16(self.register.CRIT_TEMP, 0x0000)
    self.__i2c.write8(self.register.RESOLUTION, 0x03)

  def getTemp(self, unit = 'C'):

    rawData = self.readU16(self.register.AMBIENT_TEMP)
    if(rawData & (1<< 16)):
      self.criticalFlag = 1

    if(rawData & (1 << 15)):
      self.upperFlag = 1

    if(rawData & (1 << 14)):
      self.lowerFlag = 1

    temp = rawData & 0x0FFF

    uByte = (temp >> 8)
    lByte = (temp & 0x00FF)

    temp = ((temp & 0x0F00 ) >> 4) + ((temp & 0x00FF) / 16)

    if(rawData & 0x1000):
      temp = 256 - temp

    if(unit == 'F'):
      temp /= 5
      temp *= 9
      temp += 32
    return temp


  def shutdown(self):
    self.__i2c.writeU16(self.register.CONFIG, self.register.SHUTDOWN)


  def readU16(self, register):
    return self.__i2c.reverseByteOrder(self.__i2c.readU16(register))

  def write16(self, register, data):
    self.__i2c.write16(register, self.__i2c.reverseByteOrder(data))

def main():
  therm = MCP9808()
  therm.begin()
  print("The temperature is currently {} °C.".format(therm.getTemp()))

  return 0

if __name__ == "__main__":
	sys.exit(main())
