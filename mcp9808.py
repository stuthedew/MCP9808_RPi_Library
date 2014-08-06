import sys
import Adafruit_I2C as ada_i2c
from registers import MCP9808_Register

class MCP9808:
  __manID = 0
  __deviceID = 0

  def __init__(self, address = None):
    self.register = MCP9808_Register()
    if(address == None):
      self.__address = self.register.I2CADDR_DEFAULT
    else:
      self.__address = address

    #assert(self.__address >= 0x18 && self.address <= 0x1F, "Address must be between 0x18 and 0x1F (See section 3.5 of MCP9808 datasheet)")

    self.__i2c = ada_i2c.Adafruit_I2C(self.__address)

  def begin(self):
    self.__manID = self.__i2c.readU16(self.register.MANUF_ID)
    self.__deviceID = self.__i2c.readU16(self.register.DEVICE_ID)

    if(self.__manID != 0x5400):
      raise RuntimeError("Wrong Manufacturer ID: %s. (Should be 0x5400)" %  hex(self.__manID))

    if(self.__deviceID != 0x4):
      raise RuntimeError("Wrong Device ID: %s. (Should be 0x4)" %  hex(self.__deviceID))

  def readTemp(unit = 'C'):
    temp = self.__i2c.readU16(self.register.AMBIENT_TEMP)



def main():
  therm = MCP9808()
  therm.begin()

  return 0

if __name__ == "__main__":
	sys.exit(main())
