# -*- coding: utf-8 -*-
# Caliper-python testing package (testing condensor cases)
#
# This file is part of the IMS Caliper Analytics(tm) and is licensed to IMS
# Global Learning Consortium, Inc. (http://www.imsglobal.org) under one or more
# contributor license agreements. See the NOTICE file distributed with this
# work for additional information.
#
# IMS Caliper is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# IMS Caliper is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.standard_library import install_aliases
install_aliases()
from future.utils import with_metaclass
from builtins import *

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import caliper
import caliper_tests.util as util


class TestCaliperEntities(unittest.TestCase):
    def setUp(self):
        self.fixtures = util.get_fixtures_of_type('entity')

    def tearDown(self):
        pass

    def testAllCaliperEntities(self):
        passing = True
        for fixture in self.fixtures:
            print('Testing entity fixture: {}'.format(fixture))
            try:
                self.assertEqual(util.get_fixture(fixture), util.rebuild_entity(fixture))
            except AssertionError as e:
                passing = False
                print('Unable to rebuild matching entity fixture: {}'.format(fixture))
        if not passing:
            raise AssertionError


class TestCaliperEvents(unittest.TestCase):
    def setUp(self):
        self.fixtures = util.get_fixtures_of_type('event')

    def tearDown(self):
        pass

    def testAllCaliperEvents(self):
        passing = True
        for fixture in self.fixtures:
            print('Testing event fixture: {}'.format(fixture))
            try:
                self.assertEqual(util.get_fixture(fixture), util.rebuild_event(fixture))
            except AssertionError as e:
                passing = False
                print('Unable to rebuild matching event fixture: {}'.format(fixture))
        if not passing:
            raise AssertionError