import socket
import telnetlib

import time


class Source(object):
    """this class has some method to interac whit the calan_utils"""
    def __init__(self, ip, port=5025, power=-100):

        """

        :param ip: the ip of the equipment, be sure to be able to do a successfull ping (at least)
        :param port: the port where the protocol is implemnted. This is no always the same
        :param power: the initial power value in dBm, ny defaut it's -100 dB
        """
        self.ip = ip
        self.port = port
        self.power = power

        try:
            self.connection = telnetlib.Telnet(self.ip, self.port)  # for test purpuses timeout=3)
        except socket.error, exc:
            raise Exception('Connection fail, to ip:{equipment_ip}'.format(equipment_ip=self.ip))

        self.connection.write('power %s dbm\r\n' % self.power)

    def turn_on(self):
        self.connection.write('outp on\r\n')
        time.sleep(0.1)

    def change_frequency_hz(self, frequency):
        freq = max(frequency, 9000)
        self.connection.write('freq %s\r\n' % str(freq))
        time.sleep(0.5)

    def turn_off(self):
        self.connection.write('outp off\r\n')
        time.sleep(0.1)

    def stop_source(self):
        self.connection.close()

    def set_power(self, new_power):
        self.connection.write('power %s dbm\r\n' % new_power)