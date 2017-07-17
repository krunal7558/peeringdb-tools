# peeringdb-tools
peeringbd tools
Sets of function to ease PeeringDB API call and parse the result.
https://peeringdb.com/api/

Help on module peeringdb_helper:

NAME
    peeringdb_helper

DESCRIPTION
    ###################################################
    # Script Name: peeringdb_helper.py
    # Author : Krunal Shah
    # Written and tested with Python3.4
    # Sets of function to ease PeeringDB API call and
    # parse the result.
    # Last update : 17 July 2017
    ###################################################

FUNCTIONS
    find_peer_from_ip(ip)
        This function takes IPv4/IPv6 as string and returns AS number as string for that peering point where
        IP address is assigned. ASN umber can be passed to get_peer_info(asn) to get
        more details about that network.

    get_ixp_ipinfo(ip)
        This function takes IP address (IPv4 or IPv6) as input and returns IXP info who owns that IP subnet.

    get_peer_info(asn)
        This function takes AS number as string and gives information about that ASN based on peering DB

    get_peer_ixinfo(asn)
        This function takes AS number as string and gives information location of their Public peering points

    is_rs_peer(asn, ipaddress)
        this function takes AS number (str) and IP address (str) as input and queries peering db databased to see if
        IP address is peer to route server or not. returns
          True : if IP address is peer to that Internet exchange
          False : otherwise

DATA
    baseurl = 'https://peeringdb.com/api/'

FILE
    /home/pi/peeringdb-tools/peeringdb_helper.py

