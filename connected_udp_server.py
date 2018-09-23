from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):
    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        if(not self.transport._connectedAddr):
            self.transport.connect(addr[0], addr[1])
            print("now we can only send to host %s port %d" % (addr[0], addr[1]))
            self.transport.write(b"hello")  # no need for address

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()
