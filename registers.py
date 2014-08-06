


class MCP9808_Register:
  I2CADDR_DEFAULT = 0x18
  CONFIG = 0x01

  CONFIG_SHUTDOWN = 0x0100
  CONFIG_CRITLOCKED = 0x0080
  CONFIG_WINLOCKED = 0x0040
  CONFIG_INTCLR = 0x0020
  CONFIG_ALERTSTAT = 0x0010
  CONFIG_ALERTCTRL = 0x0008
  CONFIG_ALERTSEL = 0x0002
  CONFIG_ALERTPOL = 0x0002
  CONFIG_ALERTMODE = 0x0001

  UPPER_TEMP = 0x02
  LOWER_TEMP = 0x03
  CRIT_TEMP = 0x04
  AMBIENT_TEMP = 0x05
  MANUF_ID = 0x06
  DEVICE_ID = 0x07
