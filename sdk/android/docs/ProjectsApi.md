# ProjectsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiProjectGet**](ProjectsApi.md#apiProjectGet) | **GET** /api/project | GET all projects
[**apiProjectOidDelete**](ProjectsApi.md#apiProjectOidDelete) | **DELETE** /api/project/{oid} | DELETE an existing isntance of Project
[**apiProjectOidGet**](ProjectsApi.md#apiProjectOidGet) | **GET** /api/project/{oid} | GET all projects
[**apiProjectOidPut**](ProjectsApi.md#apiProjectOidPut) | **PUT** /api/project/{oid} | Change an existing isntance of Project
[**apiProjectPost**](ProjectsApi.md#apiProjectPost) | **POST** /api/project | POST to create a project


<a name="apiProjectGet"></a>
# **apiProjectGet**
> apiProjectGet(oid)

GET all projects

### Example
```java
// Import classes:
//import io.swagger.client.api.ProjectsApi;

ProjectsApi apiInstance = new ProjectsApi();
Integer oid = 56; // Integer | 
try {
    apiInstance.apiProjectGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectsApi#apiProjectGet");
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

<a name="apiProjectOidDelete"></a>
# **apiProjectOidDelete**
> apiProjectOidDelete(oid)

DELETE an existing isntance of Project

### Example
```java
// Import classes:
//import io.swagger.client.api.ProjectsApi;

ProjectsApi apiInstance = new ProjectsApi();
String oid = "oid_example"; // String | 
try {
    apiInstance.apiProjectOidDelete(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectsApi#apiProjectOidDelete");
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
 - **Accept**: Not defined

<a name="apiProjectOidGet"></a>
# **apiProjectOidGet**
> apiProjectOidGet(oid)

GET all projects

### Example
```java
// Import classes:
//import io.swagger.client.api.ProjectsApi;

ProjectsApi apiInstance = new ProjectsApi();
Integer oid = 56; // Integer | 
try {
    apiInstance.apiProjectOidGet(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectsApi#apiProjectOidGet");
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

<a name="apiProjectOidPut"></a>
# **apiProjectOidPut**
> apiProjectOidPut(oid)

Change an existing isntance of Project

### Example
```java
// Import classes:
//import io.swagger.client.api.ProjectsApi;

ProjectsApi apiInstance = new ProjectsApi();
String oid = "oid_example"; // String | 
try {
    apiInstance.apiProjectOidPut(oid);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectsApi#apiProjectOidPut");
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
 - **Accept**: Not defined

<a name="apiProjectPost"></a>
# **apiProjectPost**
> apiProjectPost(project)

POST to create a project

### Example
```java
// Import classes:
//import io.swagger.client.api.ProjectsApi;

ProjectsApi apiInstance = new ProjectsApi();
 project = new null(); //  | 
try {
    apiInstance.apiProjectPost(project);
} catch (ApiException e) {
    System.err.println("Exception when calling ProjectsApi#apiProjectPost");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [****](.md)|  |

### Return type

null (empty response body)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

