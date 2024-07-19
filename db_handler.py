from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.dns_database
zone_collection = db.dns_zones

def load_zone(qname):
    """Load the best matched zone for a given domain name."""
    
    domain_segments = qname.split('.')

    for i in range(len(domain_segments)):
        cur_domain = '.'.join(domain_segments[i:])
        zone = zone_collection.find_one({"zone_name": cur_domain})
        if zone:
            return zone

    return None

def db_lookup(qname, qtype):
    """Look up DNS record in the database."""

    zone = load_zone(qname)

    if not zone:
        return None, None
    
    zone_len = len(zone["zone_name"].split('.'))
    qname_parts = qname.split('.')

    if len(qname_parts[:-zone_len]) == 0:
        qname_parts = ["@"]
    else:
        qname_parts = qname_parts[:-zone_len]

    for record in zone["records"]:
        rname_parts = record["name"].split('.')
        if record["type"] == qtype and rname_parts == qname_parts:
            return record["value"], record["ttl"]

    return None, None