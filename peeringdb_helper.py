#!/usr/local/bin/python3
###################################################
# Script Name: peeringdb_helper.py
# Author : Krunal Shah
# Written and tested with Python3.4
# Sets of function to ease PeeringDB API call and
# parse the result.
# Last update : 23 June 2017
###################################################


import json
import urllib.parse as urlparse
import urllib.request as urlrequest
import logging

# define global variables here.
baseurl = 'https://peeringdb.com/api/'
def get_peer_info(asn):
   '''
   This function takes AS number as string and gives information about that ASN based on peering DB
   '''
   data = None
   logging.debug("Calling get_peer_info(asn={})".format(asn))
   js = dict()
   url = baseurl + 'net?' + urlparse.urlencode({'asn':asn})
   logging.debug("Retriving : " + url)
   try:
      with urlrequest.urlopen(url) as uh:
         data = uh.read().decode("utf-8")
   except:
      logging.error("Error in retriving URL")
      logging.error("AS number might be wrong or network info is not available in peeringdb")
   logging.info("Done.")

   try: js = json.loads(str(data))
   except ValueError: js={}
   return js

def get_ixp_ipinfo(ip):
   '''
   This function takes IP address (IPv4 or IPv6) as input and returns IXP info who owns that IP subnet.
   '''
   data = None
   logging.debug("Calling get_ixp_info(ip={})".format(ip))
   js = dict()
   url = baseurl + '/ix/?' + urlparse.urlencode({})
   logging.debug("Retriving : " + url)
   try:
      with urlrequest.urlopen(url) as uh:
         data = uh.read().decode("utf-8")
   except:
      print("Error in retriving URL")
      print("IP address entered is not valid or No IXP found owning that IP subnet")
      exit()
   logging.info("Done.")

   try: js = json.loads(str(data))
   except ValueError: js={}
   return js


def get_peer_ixinfo(asn):
   '''
   This function takes AS number as string and gives information location of their Public peering points
   '''
   data = None
   js = dict()
   url = baseurl + 'netixlan?' + urlparse.urlencode({'asn':asn})
   logging.debug("Retriving : " + url)
   try:
      with urlrequest.urlopen(url) as uh:
         data = uh.read().decode("utf-8")
   except:
      logging.error("Error in retriving URL, AS number might be wrong.")
      logging.error("Peer might not have peeringDB entry")
   logging.info("Done.")

   try: js = json.loads(str(data))
   except ValueError: js={}
   return js

def is_rs_peer(asn,ipaddress):
   '''
   this function takes AS number (str) and IP address (str) as input and queries peering db databased to see if 
   IP address is peer to route server or not. returns 
     True : if IP address is peer to that Internet exchange
     False : otherwise
   '''
   data = None
   js = dict()
   js['asn'] = asn
   if (':' in ipaddress):
      js['ipaddr6'] = ipaddress
   else:
      js['ipaddr4'] = ipaddress
   url = baseurl + 'netixlan?' + urlparse.urlencode(js)
   logging.debug("Retriving : " + url)
   try:
      with urlrequest.urlopen(url) as uh:
         data = uh.read().decode("utf-8")
   except:
      logging.error("Error in retriving URL, AS number / IP address might be wrong.")
      logging.error("Peer might not have correct peeringDB entry")
   logging.info("Done.")
   try: jsn = json.loads(str(data))
   except ValueError: return False
   if jsn['data'] == []:
      return False
   else:
      return jsn['data'][0]['is_rs_peer']

def find_peer_from_ip(ip):
   '''
   This function takes IPv4/IPv6 as string and returns AS number as string for that peering point where
   IP address is assigned. ASN umber can be passed to get_peer_info(asn) to get
   more details about that network.
   '''
   logging.debug("Calling find_peer_from_ip({})".format(ip))
   js = dict()

   if ':' in ip:  #check to see if IPv6 address is passed
       url = baseurl + 'netixlan?' + urlparse.urlencode({'ipaddr6':ip})
   else:
       url = baseurl + 'netixlan?' + urlparse.urlencode({'ipaddr4':ip})
   logging.debug("Retriving : " + url)
   try:
      with urlrequest.urlopen(url) as uh:
         data = uh.read().decode("utf-8")
   except:
      logging.error("Error in retriving URL, IP address might be wrong or not assigned in that IXP")
      return None
   logging.info("Done.")
   try: 
       js = json.loads(str(data))
   except ValueError:
       return None
   return js['data'][0]['asn']

if __name__ == "__main__":
   exit()





