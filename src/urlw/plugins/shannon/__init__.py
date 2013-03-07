#!/usr/bin/python
import math
import sys

class UrlWeirdosPlugin:
    def __init__(self, urlwlog):
        self.log = urlwlog

    def compute_entropy(self, string):
        entropy = 0.0
        string_len = len(string)

        if string_len < 2:
            return 0

        i = 0
        for i in range(256):
            occurences = float(float(string.count(chr(i))) / float(string_len))
            if occurences > 0:
                logoccurences = float(math.log(occurences, 2))
                entropy += -occurences * logoccurences

        return entropy

    def run(self, url, faup_object):
        domain = faup_object['domain']
        if domain:
            domain = domain.decode('ascii')

        subdomain = faup_object['subdomain']
        if subdomain:
            subdomain = subdomain.decode('ascii')

        domain_entropy = 0.0
        subdomain_entropy = 0.0
        if domain:
            domain_entropy = self.compute_entropy(domain)
            if domain_entropy > 3.5:
                self.log.alert_log("shannon", "Domain likely to be autogenerated (score:%f)" % (domain_entropy), url)
        
        if subdomain:
            subdomain_entropy = self.compute_entropy(subdomain)
            if subdomain_entropy > 3:
                self.log.alert_log("shannon", "Subdomain appears to be a tunnel for evasion", url)
