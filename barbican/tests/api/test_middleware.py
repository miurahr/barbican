# Copyright (c) 2013-2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import mock

from barbican.api.middleware.simple import SimpleFilter


class WhenTestingSimpleMiddleware(unittest.TestCase):

    def setUp(self):
        self.app = mock.MagicMock()
        self.middle = SimpleFilter(self.app)
        self.req = mock.MagicMock()

    def test_should_process_request(self):
        self.middle.process_request(self.req)
