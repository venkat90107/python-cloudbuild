# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateBuild
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-build


# [START cloudbuild_generated_cloudbuild_v1_CloudBuild_CreateBuild_async]
from google.cloud.devtools import cloudbuild_v1


async def sample_create_build():
    # Create a client
    client = cloudbuild_v1.CloudBuildAsyncClient()

    # Initialize request argument(s)
    request = cloudbuild_v1.CreateBuildRequest(
        project_id="project_id_value",
    )

    # Make the request
    operation = client.create_build(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()
    print(response)

# [END cloudbuild_generated_cloudbuild_v1_CloudBuild_CreateBuild_async]
