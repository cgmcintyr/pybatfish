# coding=utf-8
#   Copyright 2018 The Batfish Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


class AsPath(object):
    """Represents a BGP AS Path."""

    def __init__(self, as_set_list):
        self.asPath = [list(asSet) for asSet in as_set_list]

    def __repr__(self):
        return '[' + ','.join(
            (asSet[0] if len(asSet) == 0 else '[' + ','.join(
                str(asNumber) for asNumber in asSet)) for asSet in
            self.asPath) + ']'
