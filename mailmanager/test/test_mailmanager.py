#!/usr/bin/env python

import unittest

from mailmanager.address import Address


def sort_addresses(addresses):
    pass


class TestMailmanager(unittest.TestCase):

    def sort_addresses_returns_list(self):
        addresses = []
        addresses.add(Address(1, "Name", "Company", "Address1", "Address2", "City State Zip"))
        addresses.add(Address(2, "Name", "Company", "Address1", "Address2", "City State Zip"))
        
        sort_addresses(addresses)
        



