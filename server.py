import socketserver
from dnslib import *
from db_handler import db_lookup

HOST = "0.0.0.0"
port = 9876

class DNShandler(socketserver.DatagramRequestHandler):
    """Handle DNS requests."""

    def handle(self):
        """Process incoming DNS request."""

        data = self.request[0]
        socket = self.request[1]
        request = DNSRecord.parse(data)

        qname = str(request.q.qname)
        qtype = request.q.qtype
        qtype = QTYPE[qtype]
        print(qname)
        print(qtype)
        
        reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=0), q=request.q)

        answer, ttl = db_lookup(qname,qtype)

        if answer:
            reply.add_answer(RR(rname=qname, rtype=request.q.qtype, ttl=ttl, rdata=self.convert_answer(answer, qtype)))
        else:
            reply.header.rcode = 3

        socket.sendto(reply.pack(), self.client_address)
        print(f"Answer: {answer}")
        print("---+++---")


    def convert_answer(self, value , qtype):
        """Convert answer to appropriate DNS record type."""

        match qtype:
            case "A":
                return A(value)
            case "AAAA":
                return AAAA(value)
            case "MX":
                return MX(value)
            case "CNAME":
                return CNAME(value)
            case "NS":
                return NS(value)
            case "DNAME":
                return DNAME(value)
            case "PTR":
                return PTR(value)
            case "TXT":
                return TXT(value)
            case _:
                return A(value)



if __name__ == "__main__":
    with socketserver.ThreadingUDPServer((HOST, port), DNShandler) as server:
        print(f"DNS Server started on port: {port}")
        server.serve_forever()
