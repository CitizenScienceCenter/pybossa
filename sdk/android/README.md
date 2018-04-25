# swagger-android-client

## Requirements

Building the API client library requires [Maven](https://maven.apache.org/) to be installed.

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn deploy
```

Refer to the [official documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-android-client</artifactId>
    <version>1.0.0</version>
    <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-android-client:1.0.0"
```

### Others

At first generate the JAR by executing:

    mvn package

Then manually install the following JARs:

* target/swagger-android-client-1.0.0.jar
* target/lib/*.jar

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

import io.swagger.client.api.DefaultApi;

public class DefaultApiExample {

    public static void main(String[] args) {
        DefaultApi apiInstance = new DefaultApi();
        String oid = "oid_example"; // String | 
        try {
            apiInstance.apiFavoritesGet(oid);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#apiFavoritesGet");
            e.printStackTrace();
        }
    }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**apiFavoritesGet**](docs/DefaultApi.md#apiFavoritesGet) | **GET** /api/favorites | GET all tasks favorited by the current user
*DefaultApi* | [**apiFavoritesOidGet**](docs/DefaultApi.md#apiFavoritesOidGet) | **GET** /api/favorites/{oid} | GET all tasks favorited by the current user
*DefaultApi* | [**apiFavoritesPost**](docs/DefaultApi.md#apiFavoritesPost) | **POST** /api/favorites | POST a favourite task for the current user
*DefaultApi* | [**apiResultGet**](docs/DefaultApi.md#apiResultGet) | **GET** /api/result | Example endpoint returning a list of colors by palette
*DefaultApi* | [**apiResultOidGet**](docs/DefaultApi.md#apiResultOidGet) | **GET** /api/result/{oid} | Example endpoint returning a list of colors by palette
*ProjectsApi* | [**apiProjectGet**](docs/ProjectsApi.md#apiProjectGet) | **GET** /api/project | GET all projects
*ProjectsApi* | [**apiProjectOidDelete**](docs/ProjectsApi.md#apiProjectOidDelete) | **DELETE** /api/project/{oid} | DELETE an existing isntance of Project
*ProjectsApi* | [**apiProjectOidGet**](docs/ProjectsApi.md#apiProjectOidGet) | **GET** /api/project/{oid} | GET all projects
*ProjectsApi* | [**apiProjectOidPut**](docs/ProjectsApi.md#apiProjectOidPut) | **PUT** /api/project/{oid} | Change an existing isntance of Project
*ProjectsApi* | [**apiProjectPost**](docs/ProjectsApi.md#apiProjectPost) | **POST** /api/project | POST to create a project
*TasksApi* | [**apiTaskGet**](docs/TasksApi.md#apiTaskGet) | **GET** /api/task | GET all tasks
*TasksApi* | [**apiTaskOidGet**](docs/TasksApi.md#apiTaskOidGet) | **GET** /api/task/{oid} | GET all tasks


## Documentation for Models

 - [TaskId](docs/TaskId.md)


## Documentation for Authorization

Authentication schemes defined for the API:
### APIKeyQueryParam

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

support@scifabric.com

