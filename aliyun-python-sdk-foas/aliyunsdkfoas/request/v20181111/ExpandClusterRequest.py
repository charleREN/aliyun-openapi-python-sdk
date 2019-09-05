# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkfoas.endpoint import endpoint_data

class ExpandClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'ExpandCluster','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/clusters/[clusterId]/expand')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_count(self):
		return self.get_body_params().get('count')

	def set_count(self,count):
		self.add_body_params('count', count)

	def get_model(self):
		return self.get_body_params().get('model')

	def set_model(self,model):
		self.add_body_params('model', model)

	def get_userVSwitch(self):
		return self.get_body_params().get('userVSwitch')

	def set_userVSwitch(self,userVSwitch):
		self.add_body_params('userVSwitch', userVSwitch)

	def get_clusterId(self):
		return self.get_path_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_path_param('clusterId',clusterId)