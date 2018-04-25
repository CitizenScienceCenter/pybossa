# DefaultApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiFavoritesGet**](DefaultApi.md#apiFavoritesGet) | **GET** /api/favorites | GET all tasks favorited by the current user
[**apiFavoritesOidGet**](DefaultApi.md#apiFavoritesOidGet) | **GET** /api/favorites/{oid} | GET all tasks favorited by the current user
[**apiFavoritesPost**](DefaultApi.md#apiFavoritesPost) | **POST** /api/favorites | POST a favourite task for the current user
[**apiResultGet**](DefaultApi.md#apiResultGet) | **GET** /api/result | Example endpoint returning a list of colors by palette
[**apiResultOidGet**](DefaultApi.md#apiResultOidGet) | **GET** /api/result/{oid} | Example endpoint returning a list of colors by palette


<a name="apiFavoritesGet"></a>
# **apiFavoritesGet**
> apiFavoritesGet(oid)

GET all tasks favorited by the current user

### Example
```java
// Import classes:
//import io.swagger.client.api.DefaultApi;

DefaultApi apiInstance = new DefaultApi();
String oid = "oid_example"; // String | 
try {
    apiInstance.apiFavoritesGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#apiFavoritesGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiFavoritesOidGet"></a>
# **apiFavoritesOidGet**
> apiFavoritesOidGet(oid)

GET all tasks favorited by the current user

### Example
```java
// Import classes:
//import io.swagger.client.api.DefaultApi;

DefaultApi apiInstance = new DefaultApi();
String oid = "oid_example"; // String | 
try {
    apiInstance.apiFavoritesOidGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#apiFavoritesOidGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiFavoritesPost"></a>
# **apiFavoritesPost**
> apiFavoritesPost(taskId)

POST a favourite task for the current user

### Example
```java
// Import classes:
//import io.swagger.client.api.DefaultApi;

DefaultApi apiInstance = new DefaultApi();
TaskId taskId = new TaskId(); // TaskId | The task ID to favorite
try {
    apiInstance.apiFavoritesPost(taskId);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#apiFavoritesPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | [**TaskId**](TaskId.md)| The task ID to favorite | [optional]

### Return type

null (empty response body)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="apiResultGet"></a>
# **apiResultGet**
> apiResultGet(palette)

Example endpoint returning a list of colors by palette

In this example the specification is taken from external YAML file&lt;br/&gt;

### Example
```java
// Import classes:
//import io.swagger.client.api.DefaultApi;

DefaultApi apiInstance = new DefaultApi();
String palette = "palette_example"; // String | 
try {
    apiInstance.apiResultGet(palette);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#apiResultGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiResultOidGet"></a>
# **apiResultOidGet**
> apiResultOidGet(palette)

Example endpoint returning a list of colors by palette

In this example the specification is taken from external YAML file&lt;br/&gt;

### Example
```java
// Import classes:
//import io.swagger.client.api.DefaultApi;

DefaultApi apiInstance = new DefaultApi();
String palette = "palette_example"; // String | 
try {
    apiInstance.apiResultOidGet(palette);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#apiResultOidGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette** | **String**|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

