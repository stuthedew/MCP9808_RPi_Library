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
    self.__manID = self.__i2c.readU16(self.register.MANUF_ID)
    self.__deviceID = self.__i2c.readU16(self.register.DEVICE_ID)
    print(hex(self.__manID))
    print(hex(self.__deviceID))
    if(self.__manID != 0x5400):
      raise RuntimeError("Wrong Manufacturer ID: %s. (Should be 0x5400. Check I2C Address)" %  hex(self.__manID))

    if(self.__deviceID != 0x4):
      raise RuntimeError("Wrong Device ID: %s. (Should be 0x4. Check I2C Address)" %  hex(self.__deviceID))



  def reset(self):
    self.__i2c.write16(self.register.CONFIG, 0x0000)
    self.__i2c.write16(self.register.UPPER_TEMP, 0x0000)
    self.__i2c.write16(self.register.LOWER_TEMP, 0x0000)
    self.__i2c.write16(self.register.CRIT_TEMP, 0x0000)
    self.__i2c.write8(self.register.RESOLUTION, 0x03)

  def readTemp(self, unit = 'C'):
    rawData = self.__i2c.readU16(self.register.AMBIENT_TEMP)
    if(rawData & (1<< 16)):
      self.criticalFlag = 1

    if(rawData & (1 << 15)):
      self.upperFlag = 1

    if(rawData & (1 << 14)):
      self.lowerFlag = 1


  def shutdown(self):
    self.__i2c.writeU16(self.register.CONFIG, self.register.SHUTDOWN)



def main():
  therm = MCP9808()
  therm.begin()

  return 0

if __name__ == "__main__":
	sys.exit(main())
