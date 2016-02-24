# Copyright 2015-2016 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fake_switches.juniper.juniper_netconf_datastore import JuniperNetconfDatastore, resolve_new_value


class JuniperQfxCopperNetconfDatastore(JuniperNetconfDatastore):
    def __init__(self, configuration):
        super(JuniperQfxCopperNetconfDatastore, self).__init__(configuration)

        self.PORT_MODE_TAG = "interface-mode"

    def apply_trunk_native_vlan(self, interface_data, port):
        if port.trunk_native_vlan is not None:
            interface_data.append({"native-vlan-id": str(port.trunk_native_vlan)})

    def parse_trunk_native_vlan(self, interface_node, port):
        native_vlan_id_node = interface_node.xpath("native-vlan-id")
        if len(native_vlan_id_node) == 1 and native_vlan_id_node[0].text is not None:
            return resolve_new_value(interface_node, "native-vlan-id", port.trunk_native_vlan,
                                 transformer=int)
        return None
