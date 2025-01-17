# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from json import loads as _loads
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._collections_operations import build_create_or_update_collection_request, build_delete_collection_request, build_get_collection_path_request, build_get_collection_request, build_list_child_collection_names_request, build_list_collections_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CollectionsOperations:
    """CollectionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_collection(
        self,
        collection_name: str,
        **kwargs: Any
    ) -> Any:
        """Get a collection.

        :param collection_name:
        :type collection_name: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "collectionProvisioningState": "str (optional)",
                    "description": "str (optional)",
                    "friendlyName": "str (optional)",
                    "name": "str (optional)",
                    "parentCollection": {
                        "referenceName": "str (optional)",
                        "type": "str (optional)"
                    },
                    "systemData": {
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByType": "str (optional)",
                        "lastModifiedAt": "datetime (optional)",
                        "lastModifiedBy": "str (optional)",
                        "lastModifiedByType": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_collection_request(
            collection_name=collection_name,
            template_url=self.get_collection.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_collection.metadata = {'url': '/collections/{collectionName}'}  # type: ignore


    @distributed_trace_async
    async def create_or_update_collection(
        self,
        collection_name: str,
        collection: Any,
        **kwargs: Any
    ) -> Any:
        """Creates or updates a collection entity.

        :param collection_name:
        :type collection_name: str
        :param collection:
        :type collection: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                collection = {
                    "collectionProvisioningState": "str (optional)",
                    "description": "str (optional)",
                    "friendlyName": "str (optional)",
                    "name": "str (optional)",
                    "parentCollection": {
                        "referenceName": "str (optional)",
                        "type": "str (optional)"
                    },
                    "systemData": {
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByType": "str (optional)",
                        "lastModifiedAt": "datetime (optional)",
                        "lastModifiedBy": "str (optional)",
                        "lastModifiedByType": "str (optional)"
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "collectionProvisioningState": "str (optional)",
                    "description": "str (optional)",
                    "friendlyName": "str (optional)",
                    "name": "str (optional)",
                    "parentCollection": {
                        "referenceName": "str (optional)",
                        "type": "str (optional)"
                    },
                    "systemData": {
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByType": "str (optional)",
                        "lastModifiedAt": "datetime (optional)",
                        "lastModifiedBy": "str (optional)",
                        "lastModifiedByType": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = collection

        request = build_create_or_update_collection_request(
            collection_name=collection_name,
            content_type=content_type,
            json=json,
            template_url=self.create_or_update_collection.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update_collection.metadata = {'url': '/collections/{collectionName}'}  # type: ignore


    @distributed_trace_async
    async def delete_collection(
        self,
        collection_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a Collection entity.

        :param collection_name:
        :type collection_name: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_collection_request(
            collection_name=collection_name,
            template_url=self.delete_collection.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    delete_collection.metadata = {'url': '/collections/{collectionName}'}  # type: ignore


    @distributed_trace
    def list_collections(
        self,
        *,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[Any]:
        """List the collections in the account.

        :keyword skip_token:
        :paramtype skip_token: str
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "count": "long (optional)",
                    "nextLink": "str (optional)",
                    "value": [
                        {
                            "collectionProvisioningState": "str (optional)",
                            "description": "str (optional)",
                            "friendlyName": "str (optional)",
                            "name": "str (optional)",
                            "parentCollection": {
                                "referenceName": "str (optional)",
                                "type": "str (optional)"
                            },
                            "systemData": {
                                "createdAt": "datetime (optional)",
                                "createdBy": "str (optional)",
                                "createdByType": "str (optional)",
                                "lastModifiedAt": "datetime (optional)",
                                "lastModifiedBy": "str (optional)",
                                "lastModifiedByType": "str (optional)"
                            }
                        }
                    ]
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_collections_request(
                    skip_token=skip_token,
                    template_url=self.list_collections.metadata['url'],
                )._to_pipeline_transport_request()
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_list_collections_request(
                    skip_token=skip_token,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = _loads(pipeline_response.http_response.body())
            list_of_elem = deserialized["value"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_collections.metadata = {'url': '/collections'}  # type: ignore

    @distributed_trace
    def list_child_collection_names(
        self,
        collection_name: str,
        *,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[Any]:
        """Lists the child collections names in the collection.

        :param collection_name:
        :type collection_name: str
        :keyword skip_token:
        :paramtype skip_token: str
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "count": "long (optional)",
                    "nextLink": "str (optional)",
                    "value": [
                        {
                            "friendlyName": "str (optional)",
                            "name": "str (optional)"
                        }
                    ]
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_child_collection_names_request(
                    collection_name=collection_name,
                    skip_token=skip_token,
                    template_url=self.list_child_collection_names.metadata['url'],
                )._to_pipeline_transport_request()
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_list_child_collection_names_request(
                    collection_name=collection_name,
                    skip_token=skip_token,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = _loads(pipeline_response.http_response.body())
            list_of_elem = deserialized["value"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_child_collection_names.metadata = {'url': '/collections/{collectionName}/getChildCollectionNames'}  # type: ignore

    @distributed_trace_async
    async def get_collection_path(
        self,
        collection_name: str,
        **kwargs: Any
    ) -> Any:
        """Gets the parent name and parent friendly name chains that represent the collection path.

        :param collection_name:
        :type collection_name: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "parentFriendlyNameChain": [
                        "str (optional)"
                    ],
                    "parentNameChain": [
                        "str (optional)"
                    ]
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_collection_path_request(
            collection_name=collection_name,
            template_url=self.get_collection_path.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_collection_path.metadata = {'url': '/collections/{collectionName}/getCollectionPath'}  # type: ignore

