# TasksApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTaskGet**](TasksApi.md#apiTaskGet) | **GET** /api/task | GET all tasks
[**apiTaskOidGet**](TasksApi.md#apiTaskOidGet) | **GET** /api/task/{oid} | GET all tasks


<a name="apiTaskGet"></a>
# **apiTaskGet**
> apiTaskGet(oid)

GET all tasks

### Example
```java
// Import classes:
//import io.swagger.client.api.TasksApi;

TasksApi apiInstance = new TasksApi();
Integer oid = 56; // Integer | 
try {
    apiInstance.apiTaskGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling TasksApi#apiTaskGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiTaskOidGet"></a>
# **apiTaskOidGet**
> apiTaskOidGet(oid)

GET all tasks

### Example
```java
// Import classes:
//import io.swagger.client.api.TasksApi;

TasksApi apiInstance = new TasksApi();
Integer oid = 56; // Integer | 
try {
    apiInstance.apiTaskOidGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling TasksApi#apiTaskOidGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **Integer**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

