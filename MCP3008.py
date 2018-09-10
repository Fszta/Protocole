#coding : utf-8

from spidev import SpiDev

class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev() # Creation object spi
        self.open()
        self.spi.max_speed_hz = 1350000
        self.spi.mode = 0b11

    def open(self):
        """ Ouverture port 0 , chip select 0"""
        self.spi.open(self.bus, self.device)

    def read(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def close(self):
        self.spi.close()
