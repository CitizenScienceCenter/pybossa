# swagger_client.DefaultApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_favorites_get**](DefaultApi.md#api_favorites_get) | **GET** /api/favorites | GET all tasks favorited by the current user
[**api_favorites_oid_get**](DefaultApi.md#api_favorites_oid_get) | **GET** /api/favorites/{oid} | GET all tasks favorited by the current user
[**api_favorites_post**](DefaultApi.md#api_favorites_post) | **POST** /api/favorites | POST a favourite task for the current user
[**api_result_get**](DefaultApi.md#api_result_get) | **GET** /api/result | Example endpoint returning a list of colors by palette
[**api_result_oid_get**](DefaultApi.md#api_result_oid_get) | **GET** /api/result/{oid} | Example endpoint returning a list of colors by palette


# **api_favorites_get**
> api_favorites_get(oid)

GET all tasks favorited by the current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
oid = 'oid_example' # str | 

try:
    # GET all tasks favorited by the current user
    api_instance.api_favorites_get(oid)
except ApiException as e:
    print("Exception when calling DefaultApi->api_favorites_get: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_favorites_oid_get**
> api_favorites_oid_get(oid)

GET all tasks favorited by the current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
oid = 'oid_example' # str | 

try:
    # GET all tasks favorited by the current user
    api_instance.api_favorites_oid_get(oid)
except ApiException as e:
    print("Exception when calling DefaultApi->api_favorites_oid_get: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_favorites_post**
> api_favorites_post(task_id=task_id)

POST a favourite task for the current user

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
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
task_id = swagger_client.TaskId() # TaskId | The task ID to favorite (optional)

try:
    # POST a favourite task for the current user
    api_instance.api_favorites_post(task_id=task_id)
except ApiException as e:
    print("Exception when calling DefaultApi->api_favorites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**TaskId**](TaskId.md)| The task ID to favorite | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_result_get**
> api_result_get(palette)

Example endpoint returning a list of colors by palette

In this example the specification is taken from external YAML file<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
palette = 'palette_example' # str | 

try:
    # Example endpoint returning a list of colors by palette
    api_instance.api_result_get(palette)
except ApiException as e:
    print("Exception when calling DefaultApi->api_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_result_oid_get**
> api_result_oid_get(palette)

Example endpoint returning a list of colors by palette

In this example the specification is taken from external YAML file<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
palette = 'palette_example' # str | 

try:
    # Example endpoint returning a list of colors by palette
    api_instance.api_result_oid_get(palette)
except ApiException as e:
    print("Exception when calling DefaultApi->api_result_oid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

