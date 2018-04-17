# swagger_client.ProjectsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_project_get**](ProjectsApi.md#api_project_get) | **GET** /api/project | GET all projects
[**api_project_oid_delete**](ProjectsApi.md#api_project_oid_delete) | **DELETE** /api/project/{oid} | DELETE an existing isntance of Project
[**api_project_oid_get**](ProjectsApi.md#api_project_oid_get) | **GET** /api/project/{oid} | GET all projects
[**api_project_oid_put**](ProjectsApi.md#api_project_oid_put) | **PUT** /api/project/{oid} | Change an existing isntance of Project
[**api_project_post**](ProjectsApi.md#api_project_post) | **POST** /api/project | POST to create a project


# **api_project_get**
> api_project_get(oid)

GET all projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
oid = 56 # int | 

try:
    # GET all projects
    api_instance.api_project_get(oid)
except ApiException as e:
    print("Exception when calling ProjectsApi->api_project_get: %s\n" % e)
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

# **api_project_oid_delete**
> api_project_oid_delete(oid)

DELETE an existing isntance of Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
oid = 'oid_example' # str | 

try:
    # DELETE an existing isntance of Project
    api_instance.api_project_oid_delete(oid)
except ApiException as e:
    print("Exception when calling ProjectsApi->api_project_oid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_project_oid_get**
> api_project_oid_get(oid)

GET all projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
oid = 56 # int | 

try:
    # GET all projects
    api_instance.api_project_oid_get(oid)
except ApiException as e:
    print("Exception when calling ProjectsApi->api_project_oid_get: %s\n" % e)
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

# **api_project_oid_put**
> api_project_oid_put(oid)

Change an existing isntance of Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
oid = 'oid_example' # str | 

try:
    # Change an existing isntance of Project
    api_instance.api_project_oid_put(oid)
except ApiException as e:
    print("Exception when calling ProjectsApi->api_project_oid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_project_post**
> api_project_post(project)

POST to create a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyQueryParam
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
project = swagger_client.null() #  | 

try:
    # POST to create a project
    api_instance.api_project_post(project)
except ApiException as e:
    print("Exception when calling ProjectsApi->api_project_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [****](.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

