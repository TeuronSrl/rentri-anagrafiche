# rentri_anagrafiche.SoggettoDelegatoApi

All URIs are relative to *https://demoapi.rentri.gov.it/anagrafiche/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**soggetto_delegato_get**](SoggettoDelegatoApi.md#soggetto_delegato_get) | **GET** /soggetto-delegato | Elenco dei soggetti delegati
[**soggetto_delegato_num_iscr_ass_registri_get**](SoggettoDelegatoApi.md#soggetto_delegato_num_iscr_ass_registri_get) | **GET** /soggetto-delegato/{num_iscr_ass}/registri | Elenco registri
[**soggetto_delegato_num_iscr_ass_siti_get**](SoggettoDelegatoApi.md#soggetto_delegato_num_iscr_ass_siti_get) | **GET** /soggetto-delegato/{num_iscr_ass}/siti | Elenco unità locali
[**soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get**](SoggettoDelegatoApi.md#soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get) | **GET** /soggetto-delegato/{num_iscr_ass}/siti/{num_iscr_sito} | Ottiene il dettaglio dell&#39;unità locale per cui ha delega il soggetto delegato.
[**soggetto_delegato_registri_identificativo_delete**](SoggettoDelegatoApi.md#soggetto_delegato_registri_identificativo_delete) | **DELETE** /soggetto-delegato/registri/{identificativo} | Chiudi registro
[**soggetto_delegato_registri_identificativo_get**](SoggettoDelegatoApi.md#soggetto_delegato_registri_identificativo_get) | **GET** /soggetto-delegato/registri/{identificativo} | Dati registro
[**soggetto_delegato_registri_identificativo_put**](SoggettoDelegatoApi.md#soggetto_delegato_registri_identificativo_put) | **PUT** /soggetto-delegato/registri/{identificativo} | Modifica registro
[**soggetto_delegato_registri_identificativo_xml_get**](SoggettoDelegatoApi.md#soggetto_delegato_registri_identificativo_xml_get) | **GET** /soggetto-delegato/registri/{identificativo}/xml | Vidimazione virtuale registro in formato XML
[**soggetto_delegato_registri_post**](SoggettoDelegatoApi.md#soggetto_delegato_registri_post) | **POST** /soggetto-delegato/registri | Apertura nuovo registro


# **soggetto_delegato_get**
> List[OperatoreModel] soggetto_delegato_get()

Elenco dei soggetti delegati

Ritorna l'elenco dei soggetti delegati.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.operatore_model import OperatoreModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)

    try:
        # Elenco dei soggetti delegati
        api_response = api_instance.soggetto_delegato_get()
        print("The response of SoggettoDelegatoApi->soggetto_delegato_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[OperatoreModel]**](OperatoreModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elenco degli operatori. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_num_iscr_ass_registri_get**
> List[RegistroModel] soggetto_delegato_num_iscr_ass_registri_get(num_iscr_ass, num_iscr_sito=num_iscr_sito, identificativo_operatore=identificativo_operatore, identificativo=identificativo, chiuso=chiuso, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco registri

Ottiene l'elenco dei registri gestiti da un soggetto delegato, filtrati in base ai criteri specificati.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    num_iscr_ass = 'num_iscr_ass_example' # str | Numero iscrizione soggetto delegato rilasciato all'iscrizione. Per recuperare il numero iscrizione del soggetto delegato consultare l'operazione Elenco soggetti delegati iscritti nell'area riservata Soggetti delegati dove è presente la voce Numero iscrizione.
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione da ricercare. (optional)
    identificativo_operatore = 'identificativo_operatore_example' # str | Codice fiscale dell'operatore da ricercare. (optional)
    identificativo = 'identificativo_example' # str | Identificativo del registro da ricercare. (optional)
    chiuso = True # bool | Flag di chiusura del registro. (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize. (optional) (default to 100)

    try:
        # Elenco registri
        api_response = api_instance.soggetto_delegato_num_iscr_ass_registri_get(num_iscr_ass, num_iscr_sito=num_iscr_sito, identificativo_operatore=identificativo_operatore, identificativo=identificativo, chiuso=chiuso, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_registri_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_registri_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_ass** | **str**| Numero iscrizione soggetto delegato rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione del soggetto delegato consultare l&#39;operazione Elenco soggetti delegati iscritti nell&#39;area riservata Soggetti delegati dove è presente la voce Numero iscrizione. | 
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione da ricercare. | [optional] 
 **identificativo_operatore** | **str**| Codice fiscale dell&#39;operatore da ricercare. | [optional] 
 **identificativo** | **str**| Identificativo del registro da ricercare. | [optional] 
 **chiuso** | **bool**| Flag di chiusura del registro. | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page. | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize. | [optional] [default to 100]

### Return type

[**List[RegistroModel]**](RegistroModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elenco dei registri. |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_num_iscr_ass_siti_get**
> List[SitoModel] soggetto_delegato_num_iscr_ass_siti_get(num_iscr_ass, provincia_id=provincia_id, comune_id=comune_id, num_iscr_sito=num_iscr_sito, num_iscr_siti=num_iscr_siti, nome_sito=nome_sito, stato_delega_da_confermare=stato_delega_da_confermare, delega_da_associazione=delega_da_associazione, stato_delega=stato_delega, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco unità locali

Ottiene l'elenco delle unità locali per cui ha delega il soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.sito_model import SitoModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    num_iscr_ass = 'num_iscr_ass_example' # str | Numero iscrizione soggetto delegato rilasciato all'iscrizione. Per recuperare il numero iscrizione soggetto delegato consultare l'operazione Elenco soggetti delegati iscritti nell'area riservata Soggetti delegati dove è presente la voce Numero iscrizione
    provincia_id = 'provincia_id_example' # str | Ricerca per provincia (optional)
    comune_id = 'comune_id_example' # str | Ricerca per comune (optional)
    num_iscr_sito = 'num_iscr_sito_example' # str | Ricerca per Numero iscrizione unità locale rilasciato all'iscrizione. Per recuperare l'identificativo attribuito all'unità locale consultare l'operazione Elenco Unità Locali iscritte nell'area riservata Operatori dove è presente la voce Numero iscrizione unità locale (optional)
    num_iscr_siti = ['num_iscr_siti_example'] # List[str] | Ricerca per Numero iscrizione unità locali (optional)
    nome_sito = 'nome_sito_example' # str | Ricerca per nome unità locale (optional)
    stato_delega_da_confermare = True # bool | Stato delega da confermare (optional)
    delega_da_associazione = True # bool | Filtra le unità locali iscritte dal soggetto delegato (optional)
    stato_delega = rentri_anagrafiche.Stati() # Stati | Stato della delega (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize. (optional) (default to 100)

    try:
        # Elenco unità locali
        api_response = api_instance.soggetto_delegato_num_iscr_ass_siti_get(num_iscr_ass, provincia_id=provincia_id, comune_id=comune_id, num_iscr_sito=num_iscr_sito, num_iscr_siti=num_iscr_siti, nome_sito=nome_sito, stato_delega_da_confermare=stato_delega_da_confermare, delega_da_associazione=delega_da_associazione, stato_delega=stato_delega, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_siti_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_siti_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_ass** | **str**| Numero iscrizione soggetto delegato rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione soggetto delegato consultare l&#39;operazione Elenco soggetti delegati iscritti nell&#39;area riservata Soggetti delegati dove è presente la voce Numero iscrizione | 
 **provincia_id** | **str**| Ricerca per provincia | [optional] 
 **comune_id** | **str**| Ricerca per comune | [optional] 
 **num_iscr_sito** | **str**| Ricerca per Numero iscrizione unità locale rilasciato all&#39;iscrizione. Per recuperare l&#39;identificativo attribuito all&#39;unità locale consultare l&#39;operazione Elenco Unità Locali iscritte nell&#39;area riservata Operatori dove è presente la voce Numero iscrizione unità locale | [optional] 
 **num_iscr_siti** | [**List[str]**](str.md)| Ricerca per Numero iscrizione unità locali | [optional] 
 **nome_sito** | **str**| Ricerca per nome unità locale | [optional] 
 **stato_delega_da_confermare** | **bool**| Stato delega da confermare | [optional] 
 **delega_da_associazione** | **bool**| Filtra le unità locali iscritte dal soggetto delegato | [optional] 
 **stato_delega** | [**Stati**](.md)| Stato della delega | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page. | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize. | [optional] [default to 100]

### Return type

[**List[SitoModel]**](SitoModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elenco delle unità locali. |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get**
> SitoModel soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get(num_iscr_ass, num_iscr_sito)

Ottiene il dettaglio dell'unità locale per cui ha delega il soggetto delegato.

Ottiene il dettaglio dell'unità locale per cui ha delega il soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.sito_model import SitoModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    num_iscr_ass = 'num_iscr_ass_example' # str | Numero iscrizione soggetto delegato rilasciato all'iscrizione. Per recuperare il numero iscrizione soggetto delegato consultare l'operazione Elenco soggetti delegati iscritti nell'area riservata Soggetti delegati dove è presente la voce Numero iscrizione
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione.

    try:
        # Ottiene il dettaglio dell'unità locale per cui ha delega il soggetto delegato.
        api_response = api_instance.soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get(num_iscr_ass, num_iscr_sito)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_num_iscr_ass_siti_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_ass** | **str**| Numero iscrizione soggetto delegato rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione soggetto delegato consultare l&#39;operazione Elenco soggetti delegati iscritti nell&#39;area riservata Soggetti delegati dove è presente la voce Numero iscrizione | 
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione. | 

### Return type

[**SitoModel**](SitoModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dati delle autorizzazioni relativamente all&#39;unità locale. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_registri_identificativo_delete**
> soggetto_delegato_registri_identificativo_delete(identificativo)

Chiudi registro

Chiude un registro gestito da un soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.

    try:
        # Chiudi registro
        api_instance.soggetto_delegato_registri_identificativo_delete(identificativo)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro da chiudere. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registro chiuso correttamente. |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido. |  -  |
**403** | Operazione non consentita sul registro. |  -  |
**404** | Registro non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_registri_identificativo_get**
> RegistroModel soggetto_delegato_registri_identificativo_get(identificativo)

Dati registro

Ottiene il dettaglio di un registro gestito da un soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # Dati registro
        api_response = api_instance.soggetto_delegato_registri_identificativo_get(identificativo)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro. | 

### Return type

[**RegistroModel**](RegistroModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dati del registro. |  -  |
**403** | Operazione non consentita sul registro. |  -  |
**404** | Registro non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_registri_identificativo_put**
> UpdateRegistroResponse soggetto_delegato_registri_identificativo_put(identificativo, update_registro_request=update_registro_request)

Modifica registro

Modifica un registro gestito da un soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.update_registro_request import UpdateRegistroRequest
from rentri_anagrafiche.models.update_registro_response import UpdateRegistroResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.
    update_registro_request = rentri_anagrafiche.UpdateRegistroRequest() # UpdateRegistroRequest | Dati di modifica del registro. (optional)

    try:
        # Modifica registro
        api_response = api_instance.soggetto_delegato_registri_identificativo_put(identificativo, update_registro_request=update_registro_request)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro da chiudere. | 
 **update_registro_request** | [**UpdateRegistroRequest**](UpdateRegistroRequest.md)| Dati di modifica del registro. | [optional] 

### Return type

[**UpdateRegistroResponse**](UpdateRegistroResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identificativo del registro aggiornato. |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido. |  -  |
**403** | Operazione non consentita sul registro. |  -  |
**404** | Registro non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_registri_identificativo_xml_get**
> DownloadableBaseResponse soggetto_delegato_registri_identificativo_xml_get(identificativo)

Vidimazione virtuale registro in formato XML

Ottiene la vidimazione virtuale del Registro in formato XML.  Rif. MODALITÀ OPERATIVA (8): Vidimazione digitale del registro cronologico di carico e scarico.  Nella fase di creazione di un nuovo registro, la piattaforma telematica RENTRI accede al servizio  per la vidimazione digitale messo a disposizione dalle Camere di Commercio e restituisce l'identificativo  unico nazionale del registro cronologico di carico e scarico.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.downloadable_base_response import DownloadableBaseResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # Vidimazione virtuale registro in formato XML
        api_response = api_instance.soggetto_delegato_registri_identificativo_xml_get(identificativo)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_xml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_registri_identificativo_xml_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro. | 

### Return type

[**DownloadableBaseResponse**](DownloadableBaseResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nel campo \&quot;content\&quot; viene restituito il file XML firmato digitalmente nel formato Base64, che  risponde alla definizione del \&quot;element &#x3D; eREGI\&quot; definito nello schema XSD consultabile nella sezione \&quot;Risorse &gt; Schemi di validazione XSD\&quot; nel file “rentri-registri-1.0.xsd”. |  -  |
**403** | Operazione non consentita sull&#39;Operatore. |  -  |
**404** | Registro non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soggetto_delegato_registri_post**
> CreateRegistroResponse soggetto_delegato_registri_post(create_registro_soggetto_delegato_request=create_registro_soggetto_delegato_request)

Apertura nuovo registro

Apre un nuovo registro gestito da un soggetto delegato.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.create_registro_response import CreateRegistroResponse
from rentri_anagrafiche.models.create_registro_soggetto_delegato_request import CreateRegistroSoggettoDelegatoRequest
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://demoapi.rentri.gov.it/anagrafiche/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_anagrafiche.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_anagrafiche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_anagrafiche.SoggettoDelegatoApi(api_client)
    create_registro_soggetto_delegato_request = rentri_anagrafiche.CreateRegistroSoggettoDelegatoRequest() # CreateRegistroSoggettoDelegatoRequest | Richiesta. (optional)

    try:
        # Apertura nuovo registro
        api_response = api_instance.soggetto_delegato_registri_post(create_registro_soggetto_delegato_request=create_registro_soggetto_delegato_request)
        print("The response of SoggettoDelegatoApi->soggetto_delegato_registri_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoggettoDelegatoApi->soggetto_delegato_registri_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_registro_soggetto_delegato_request** | [**CreateRegistroSoggettoDelegatoRequest**](CreateRegistroSoggettoDelegatoRequest.md)| Richiesta. | [optional] 

### Return type

[**CreateRegistroResponse**](CreateRegistroResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identificativo del registro aperto. |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido. |  -  |
**403** | Operazione non consentita sull&#39;Operatore. |  -  |
**404** | Sito non trovato a registro. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

