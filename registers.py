

class MCP9808_Register:
  I2CADDR_DEFAULT = 0x18
  CONFIG = 0x01

  SHUTDOWN = 0x0100
  CRITLOCKED = 0x0080
  WINLOCKED = 0x0040
  INTCLR = 0x0020
  ALERTSTAT = 0x0010
  ALERTCTRL = 0x0008
  ALERTSEL = 0x0002
  ALERTPOL = 0x0002
  ALERTMODE = 0x0001

  UPPER_TEMP = 0x02
  LOWER_TEMP = 0x03
  CRIT_TEMP = 0x04
  AMBIENT_TEMP = 0x05
  MANUF_ID = 0x06
  DEVICE_ID = 0x07
  RESOLUTION = 0x08
