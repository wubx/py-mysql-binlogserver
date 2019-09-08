# coding=utf-8

from py_mysql_binlogserver.lib import Flags
from py_mysql_binlogserver.lib.packet import Packet
from py_mysql_binlogserver.lib.proto import Proto


class Statistics(Packet):
    def getPayload(self):
        payload = bytearray()

        payload.extend(Proto.build_byte(Flags.COM_STATISTICS))

        return payload

    @staticmethod
    def loadFromPacket(packet):
        obj = Statistics()
        proto = Proto(packet, 3)

        obj.sequenceId = proto.get_fixed_int(1)
        proto.get_filler(1)

        return obj