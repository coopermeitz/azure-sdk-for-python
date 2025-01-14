# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AaddsResourceDetails
    from ._models_py3 import Application
    from ._models_py3 import ApplicationGetEndpoint
    from ._models_py3 import ApplicationGetHttpsEndpoint
    from ._models_py3 import ApplicationListResult
    from ._models_py3 import ApplicationProperties
    from ._models_py3 import AsyncOperationResult
    from ._models_py3 import Autoscale
    from ._models_py3 import AutoscaleCapacity
    from ._models_py3 import AutoscaleConfigurationUpdateParameter
    from ._models_py3 import AutoscaleRecurrence
    from ._models_py3 import AutoscaleSchedule
    from ._models_py3 import AutoscaleTimeAndCapacity
    from ._models_py3 import AzureMonitorRequest
    from ._models_py3 import AzureMonitorResponse
    from ._models_py3 import AzureMonitorSelectedConfigurations
    from ._models_py3 import AzureMonitorTableConfiguration
    from ._models_py3 import BillingMeters
    from ._models_py3 import BillingResources
    from ._models_py3 import BillingResponseListResult
    from ._models_py3 import CapabilitiesResult
    from ._models_py3 import ClientGroupInfo
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterConfigurations
    from ._models_py3 import ClusterCreateParametersExtended
    from ._models_py3 import ClusterCreateProperties
    from ._models_py3 import ClusterCreateRequestValidationParameters
    from ._models_py3 import ClusterCreateValidationResult
    from ._models_py3 import ClusterDefinition
    from ._models_py3 import ClusterDiskEncryptionParameters
    from ._models_py3 import ClusterGetProperties
    from ._models_py3 import ClusterIdentity
    from ._models_py3 import ClusterListPersistedScriptActionsResult
    from ._models_py3 import ClusterListResult
    from ._models_py3 import ClusterListRuntimeScriptActionDetailResult
    from ._models_py3 import ClusterListRuntimeScriptActionDetailResultAutoGenerated
    from ._models_py3 import ClusterMonitoringRequest
    from ._models_py3 import ClusterMonitoringResponse
    from ._models_py3 import ClusterPatchParameters
    from ._models_py3 import ClusterResizeParameters
    from ._models_py3 import ComponentsC51Ht8SchemasClusteridentityPropertiesUserassignedidentitiesAdditionalproperties
    from ._models_py3 import ComputeIsolationProperties
    from ._models_py3 import ComputeProfile
    from ._models_py3 import ConnectivityEndpoint
    from ._models_py3 import DataDisksGroups
    from ._models_py3 import Dimension
    from ._models_py3 import DiskBillingMeters
    from ._models_py3 import DiskEncryptionProperties
    from ._models_py3 import EncryptionInTransitProperties
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Errors
    from ._models_py3 import ExcludedServicesConfig
    from ._models_py3 import ExecuteScriptActionParameters
    from ._models_py3 import Extension
    from ._models_py3 import GatewaySettings
    from ._models_py3 import HardwareProfile
    from ._models_py3 import HostInfo
    from ._models_py3 import KafkaRestProperties
    from ._models_py3 import LinuxOperatingSystemProfile
    from ._models_py3 import LocalizedName
    from ._models_py3 import MetricSpecifications
    from ._models_py3 import NameAvailabilityCheckRequestParameters
    from ._models_py3 import NameAvailabilityCheckResult
    from ._models_py3 import NetworkProperties
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationProperties
    from ._models_py3 import OsProfile
    from ._models_py3 import ProxyResource
    from ._models_py3 import QuotaCapability
    from ._models_py3 import QuotaInfo
    from ._models_py3 import RegionalQuotaCapability
    from ._models_py3 import RegionsCapability
    from ._models_py3 import Resource
    from ._models_py3 import Role
    from ._models_py3 import RuntimeScriptAction
    from ._models_py3 import RuntimeScriptActionDetail
    from ._models_py3 import ScriptAction
    from ._models_py3 import ScriptActionExecutionHistoryList
    from ._models_py3 import ScriptActionExecutionSummary
    from ._models_py3 import ScriptActionPersistedGetResponseSpec
    from ._models_py3 import ScriptActionsList
    from ._models_py3 import SecurityProfile
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import SshProfile
    from ._models_py3 import SshPublicKey
    from ._models_py3 import StorageAccount
    from ._models_py3 import StorageProfile
    from ._models_py3 import TrackedResource
    from ._models_py3 import UpdateClusterIdentityCertificateParameters
    from ._models_py3 import UpdateGatewaySettingsParameters
    from ._models_py3 import Usage
    from ._models_py3 import UsagesListResult
    from ._models_py3 import ValidationErrorInfo
    from ._models_py3 import VersionSpec
    from ._models_py3 import VersionsCapability
    from ._models_py3 import VirtualNetworkProfile
    from ._models_py3 import VmSizeCompatibilityFilter
    from ._models_py3 import VmSizeCompatibilityFilterV2
    from ._models_py3 import VmSizeProperty
    from ._models_py3 import VmSizesCapability
except (SyntaxError, ImportError):
    from ._models import AaddsResourceDetails  # type: ignore
    from ._models import Application  # type: ignore
    from ._models import ApplicationGetEndpoint  # type: ignore
    from ._models import ApplicationGetHttpsEndpoint  # type: ignore
    from ._models import ApplicationListResult  # type: ignore
    from ._models import ApplicationProperties  # type: ignore
    from ._models import AsyncOperationResult  # type: ignore
    from ._models import Autoscale  # type: ignore
    from ._models import AutoscaleCapacity  # type: ignore
    from ._models import AutoscaleConfigurationUpdateParameter  # type: ignore
    from ._models import AutoscaleRecurrence  # type: ignore
    from ._models import AutoscaleSchedule  # type: ignore
    from ._models import AutoscaleTimeAndCapacity  # type: ignore
    from ._models import AzureMonitorRequest  # type: ignore
    from ._models import AzureMonitorResponse  # type: ignore
    from ._models import AzureMonitorSelectedConfigurations  # type: ignore
    from ._models import AzureMonitorTableConfiguration  # type: ignore
    from ._models import BillingMeters  # type: ignore
    from ._models import BillingResources  # type: ignore
    from ._models import BillingResponseListResult  # type: ignore
    from ._models import CapabilitiesResult  # type: ignore
    from ._models import ClientGroupInfo  # type: ignore
    from ._models import Cluster  # type: ignore
    from ._models import ClusterConfigurations  # type: ignore
    from ._models import ClusterCreateParametersExtended  # type: ignore
    from ._models import ClusterCreateProperties  # type: ignore
    from ._models import ClusterCreateRequestValidationParameters  # type: ignore
    from ._models import ClusterCreateValidationResult  # type: ignore
    from ._models import ClusterDefinition  # type: ignore
    from ._models import ClusterDiskEncryptionParameters  # type: ignore
    from ._models import ClusterGetProperties  # type: ignore
    from ._models import ClusterIdentity  # type: ignore
    from ._models import ClusterListPersistedScriptActionsResult  # type: ignore
    from ._models import ClusterListResult  # type: ignore
    from ._models import ClusterListRuntimeScriptActionDetailResult  # type: ignore
    from ._models import ClusterListRuntimeScriptActionDetailResultAutoGenerated  # type: ignore
    from ._models import ClusterMonitoringRequest  # type: ignore
    from ._models import ClusterMonitoringResponse  # type: ignore
    from ._models import ClusterPatchParameters  # type: ignore
    from ._models import ClusterResizeParameters  # type: ignore
    from ._models import ComponentsC51Ht8SchemasClusteridentityPropertiesUserassignedidentitiesAdditionalproperties  # type: ignore
    from ._models import ComputeIsolationProperties  # type: ignore
    from ._models import ComputeProfile  # type: ignore
    from ._models import ConnectivityEndpoint  # type: ignore
    from ._models import DataDisksGroups  # type: ignore
    from ._models import Dimension  # type: ignore
    from ._models import DiskBillingMeters  # type: ignore
    from ._models import DiskEncryptionProperties  # type: ignore
    from ._models import EncryptionInTransitProperties  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Errors  # type: ignore
    from ._models import ExcludedServicesConfig  # type: ignore
    from ._models import ExecuteScriptActionParameters  # type: ignore
    from ._models import Extension  # type: ignore
    from ._models import GatewaySettings  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import HostInfo  # type: ignore
    from ._models import KafkaRestProperties  # type: ignore
    from ._models import LinuxOperatingSystemProfile  # type: ignore
    from ._models import LocalizedName  # type: ignore
    from ._models import MetricSpecifications  # type: ignore
    from ._models import NameAvailabilityCheckRequestParameters  # type: ignore
    from ._models import NameAvailabilityCheckResult  # type: ignore
    from ._models import NetworkProperties  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationProperties  # type: ignore
    from ._models import OsProfile  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import QuotaCapability  # type: ignore
    from ._models import QuotaInfo  # type: ignore
    from ._models import RegionalQuotaCapability  # type: ignore
    from ._models import RegionsCapability  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Role  # type: ignore
    from ._models import RuntimeScriptAction  # type: ignore
    from ._models import RuntimeScriptActionDetail  # type: ignore
    from ._models import ScriptAction  # type: ignore
    from ._models import ScriptActionExecutionHistoryList  # type: ignore
    from ._models import ScriptActionExecutionSummary  # type: ignore
    from ._models import ScriptActionPersistedGetResponseSpec  # type: ignore
    from ._models import ScriptActionsList  # type: ignore
    from ._models import SecurityProfile  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import SshProfile  # type: ignore
    from ._models import SshPublicKey  # type: ignore
    from ._models import StorageAccount  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import UpdateClusterIdentityCertificateParameters  # type: ignore
    from ._models import UpdateGatewaySettingsParameters  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsagesListResult  # type: ignore
    from ._models import ValidationErrorInfo  # type: ignore
    from ._models import VersionSpec  # type: ignore
    from ._models import VersionsCapability  # type: ignore
    from ._models import VirtualNetworkProfile  # type: ignore
    from ._models import VmSizeCompatibilityFilter  # type: ignore
    from ._models import VmSizeCompatibilityFilterV2  # type: ignore
    from ._models import VmSizeProperty  # type: ignore
    from ._models import VmSizesCapability  # type: ignore

from ._hd_insight_management_client_enums import (
    AsyncOperationState,
    DaysOfWeek,
    FilterMode,
    HDInsightClusterProvisioningState,
    JsonWebKeyEncryptionAlgorithm,
    OSType,
    PrivateLink,
    ResourceIdentityType,
    ResourceProviderConnection,
    RoleName,
    Tier,
)

__all__ = [
    'AaddsResourceDetails',
    'Application',
    'ApplicationGetEndpoint',
    'ApplicationGetHttpsEndpoint',
    'ApplicationListResult',
    'ApplicationProperties',
    'AsyncOperationResult',
    'Autoscale',
    'AutoscaleCapacity',
    'AutoscaleConfigurationUpdateParameter',
    'AutoscaleRecurrence',
    'AutoscaleSchedule',
    'AutoscaleTimeAndCapacity',
    'AzureMonitorRequest',
    'AzureMonitorResponse',
    'AzureMonitorSelectedConfigurations',
    'AzureMonitorTableConfiguration',
    'BillingMeters',
    'BillingResources',
    'BillingResponseListResult',
    'CapabilitiesResult',
    'ClientGroupInfo',
    'Cluster',
    'ClusterConfigurations',
    'ClusterCreateParametersExtended',
    'ClusterCreateProperties',
    'ClusterCreateRequestValidationParameters',
    'ClusterCreateValidationResult',
    'ClusterDefinition',
    'ClusterDiskEncryptionParameters',
    'ClusterGetProperties',
    'ClusterIdentity',
    'ClusterListPersistedScriptActionsResult',
    'ClusterListResult',
    'ClusterListRuntimeScriptActionDetailResult',
    'ClusterListRuntimeScriptActionDetailResultAutoGenerated',
    'ClusterMonitoringRequest',
    'ClusterMonitoringResponse',
    'ClusterPatchParameters',
    'ClusterResizeParameters',
    'ComponentsC51Ht8SchemasClusteridentityPropertiesUserassignedidentitiesAdditionalproperties',
    'ComputeIsolationProperties',
    'ComputeProfile',
    'ConnectivityEndpoint',
    'DataDisksGroups',
    'Dimension',
    'DiskBillingMeters',
    'DiskEncryptionProperties',
    'EncryptionInTransitProperties',
    'ErrorResponse',
    'Errors',
    'ExcludedServicesConfig',
    'ExecuteScriptActionParameters',
    'Extension',
    'GatewaySettings',
    'HardwareProfile',
    'HostInfo',
    'KafkaRestProperties',
    'LinuxOperatingSystemProfile',
    'LocalizedName',
    'MetricSpecifications',
    'NameAvailabilityCheckRequestParameters',
    'NameAvailabilityCheckResult',
    'NetworkProperties',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationProperties',
    'OsProfile',
    'ProxyResource',
    'QuotaCapability',
    'QuotaInfo',
    'RegionalQuotaCapability',
    'RegionsCapability',
    'Resource',
    'Role',
    'RuntimeScriptAction',
    'RuntimeScriptActionDetail',
    'ScriptAction',
    'ScriptActionExecutionHistoryList',
    'ScriptActionExecutionSummary',
    'ScriptActionPersistedGetResponseSpec',
    'ScriptActionsList',
    'SecurityProfile',
    'ServiceSpecification',
    'SshProfile',
    'SshPublicKey',
    'StorageAccount',
    'StorageProfile',
    'TrackedResource',
    'UpdateClusterIdentityCertificateParameters',
    'UpdateGatewaySettingsParameters',
    'Usage',
    'UsagesListResult',
    'ValidationErrorInfo',
    'VersionSpec',
    'VersionsCapability',
    'VirtualNetworkProfile',
    'VmSizeCompatibilityFilter',
    'VmSizeCompatibilityFilterV2',
    'VmSizeProperty',
    'VmSizesCapability',
    'AsyncOperationState',
    'DaysOfWeek',
    'FilterMode',
    'HDInsightClusterProvisioningState',
    'JsonWebKeyEncryptionAlgorithm',
    'OSType',
    'PrivateLink',
    'ResourceIdentityType',
    'ResourceProviderConnection',
    'RoleName',
    'Tier',
]
