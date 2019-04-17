"""Module with class that generates component specifications for the component analysis.

Copyright (c) 2019 Red Hat Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class ComponentGenerator:
    """Class that generates component specifications for the component analysis."""

    components = {
        "pypi": {
            "clojure_py": ["0.1.0g", "0.2.0", "0.2.1", "0.2.2", "0.2.3",
                           "0.2.4"],
            "six": ["0.9.0", "0.9.1", "0.9.2", "1.0b1", "1.0.0", "1.1.0",
                    "1.2.0", "1.3.0", "1.4.0", "1.4.1", "1.5.0", "1.5.1",
                    "1.5.2", "1.6.0", "1.6.1", "1.7.0", "1.7.1", "1.7.2",
                    "1.7.3", "1.8.0", "1.9.0", "1.10.0"],
            "ansicolors": ["1.0", "1.0.1", "1.0.2", "1.1.5", "1.1.6", "1.1.7",
                           "1.1.8"],
            "pytest": ["2.0.0", "2.0.1", "2.0.2", "2.0.3", "2.1.0", "2.1.1",
                       "2.1.2", "2.1.3", "2.2.0", "2.2.1", "2.2.2", "2.2.3",
                       "2.2.4", "2.3.0", "2.3.1", "2.3.2", "2.3.3", "2.3.4",
                       "2.3.5", "2.4.0", "2.4.1", "2.4.2", "2.5.0", "2.5.1",
                       "2.5.2", "2.6.0", "2.6.1", "2.6.2", "2.6.3", "2.6.4",
                       "2.7.0", "2.7.1", "2.7.2", "2.7.3", "2.8.0", "2.8.1",
                       "2.8.2", "2.8.3", "2.8.4", "2.8.5", "2.8.6", "2.8.7",
                       "2.9.0", "2.9.1", "2.9.2", "3.0.0", "3.0.1", "3.0.2",
                       "3.0.3", "3.0.4", "3.0.5", "3.0.6", "3.0.7", "3.1.0",
                       "3.1.1", "3.1.2", "3.1.3", "3.2.0", "3.2.1", "3.2.2"]
        }
    }

    def generator_for_ecosystem(self, ecosystem='pypi'):
        """Provide generator for component specifications for selected ecosystem."""
        components_for_ecosystem = ComponentGenerator.components[ecosystem]
        while True:
            for component, versions in components_for_ecosystem.items():
                for version in versions:
                    yield (ecosystem, component, version)
