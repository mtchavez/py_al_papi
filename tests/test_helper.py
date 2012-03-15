import httplib
import os
import random
import re
import unittest
import urllib
import warnings
from al_papi import *
from datetime import date, datetime, timedelta
from decimal import Decimal
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from random import randint


class TestHelper(object):

    @staticmethod
    def includes(collection, expected):
        for item in collection.items:
            if item.id == expected.id:
                return True
        return False

    @staticmethod
    def in_list(collection, expected):
        for item in collection:
            if item == expected:
                return True
        return False
