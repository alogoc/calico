# -*- coding: utf-8 -*-
# Copyright (c) 2015 Metaswitch Networks
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
felix.exceptions
~~~~~~~~~~~

Shared exceptions used in Felix.
"""

class InvalidRequest(Exception):
    """
    Exception that allows us to report an invalid request.
    """
    def __init__(self, message, fields):
        super(InvalidRequest, self).__init__(message)
        self.message = message
        self.fields = fields

    def __str__(self):
        return "%s (request : %s)" % (self.message, self.fields)


class InconsistentIPVersion(Exception):
    """
    Tried to create an Address with inconsistent IP versions between
    properties, e.g. IP and gateway.
    """
    pass


class InvalidAddress(Exception):
    pass
