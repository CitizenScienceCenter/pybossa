# swagger_client.TasksApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_task_get**](TasksApi.md#api_task_get) | **GET** /api/task | GET all tasks
[**api_task_oid_get**](TasksApi.md#api_task_oid_get) | **GET** /api/task/{oid} | GET all tasks


# **api_task_get**
> api_task_get(oid)

GET all tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TasksApi()
oid = 56 # int | 

try:
    # GET all tasks
    api_instance.api_task_get(oid)
except ApiException as e:
    print("Exception when calling TasksApi->api_task_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_task_oid_get**
> api_task_oid_get(oid)

GET all tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TasksApi()
oid = 56 # int | 

try:
    # GET all tasks
    api_instance.api_task_oid_get(oid)
except ApiException as e:
    print("Exception when calling TasksApi->api_task_oid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

