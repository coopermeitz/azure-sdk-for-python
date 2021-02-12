# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._test_base import _BlobTest

from azure_devtools.perfstress_tests import RandomStream, get_random_bytes
from azure_devtools.perfstress_tests import AsyncRandomStream


class UploadTest(_BlobTest):
    def __init__(self, arguments):
        super().__init__(arguments)
        blob_name = "downloadtest"
        self.blob_client = self.container_client.get_blob_client(blob_name)
        self.async_blob_client = self.async_container_client.get_blob_client(blob_name)
        self.upload_stream = RandomStream(self.args.size)
        self.upload_stream_async = AsyncRandomStream(self.args.size)

    async def global_setup(self):
        await super().global_setup()
        data = get_random_bytes(self.args.size)
        await self.async_blob_client.upload_blob(data)
    
    def run_sync(self):
        self.upload_stream.reset()
        self.blob_client.upload_blob(
            self.upload_stream,
            length=self.args.size,
            overwrite=True,
            max_concurrency=self.args.max_concurrency)

    async def run_async(self):
        self.upload_stream_async.reset()
        await self.async_blob_client.upload_blob(
            self.upload_stream_async,
            length=self.args.size,
            overwrite=True,
            max_concurrency=self.args.max_concurrency)