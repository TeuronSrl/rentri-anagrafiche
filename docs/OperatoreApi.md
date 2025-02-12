# rentri_anagrafiche.OperatoreApi

All URIs are relative to *https://api.rentri.gov.it/anagrafiche/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operatore_get**](OperatoreApi.md#operatore_get) | **GET** /operatore | Elenco degli operatori
[**operatore_identificativo_controllo_autorizzazione_albo_get**](OperatoreApi.md#operatore_identificativo_controllo_autorizzazione_albo_get) | **GET** /operatore/{identificativo}/controllo-autorizzazione-albo | Consultazione autorizzazioni Albo
[**operatore_identificativo_controllo_iscrizione_get**](OperatoreApi.md#operatore_identificativo_controllo_iscrizione_get) | **GET** /operatore/{identificativo}/controllo-iscrizione | Consultazione iscrizioni
[**operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get**](OperatoreApi.md#operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get) | **GET** /operatore/{identificativo}/siti/{comune_id}/controllo-autorizzazioni | Consultazione autorizzazioni unità locali
[**operatore_num_iscr_autorizzazione_albo_get**](OperatoreApi.md#operatore_num_iscr_autorizzazione_albo_get) | **GET** /operatore/{num_iscr}/autorizzazione-albo | Informazioni autorizzazione Albo
[**operatore_num_iscr_siti_get**](OperatoreApi.md#operatore_num_iscr_siti_get) | **GET** /operatore/{num_iscr}/siti | Elenco unità locali
[**operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get**](OperatoreApi.md#operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get) | **GET** /operatore/{num_iscr}/siti/{num_iscr_sito}/autorizzazioni | Informazioni sulle autorizzazioni dell&#39;unità locale
[**operatore_num_iscr_siti_num_iscr_sito_get**](OperatoreApi.md#operatore_num_iscr_siti_num_iscr_sito_get) | **GET** /operatore/{num_iscr}/siti/{num_iscr_sito} | Dati dell&#39;unità locale
[**operatore_num_iscr_siti_num_iscr_sito_registri_get**](OperatoreApi.md#operatore_num_iscr_siti_num_iscr_sito_registri_get) | **GET** /operatore/{num_iscr}/siti/{num_iscr_sito}/registri | Elenco registri
[**operatore_registri_identificativo_delete**](OperatoreApi.md#operatore_registri_identificativo_delete) | **DELETE** /operatore/registri/{identificativo} | Chiudi registro
[**operatore_registri_identificativo_get**](OperatoreApi.md#operatore_registri_identificativo_get) | **GET** /operatore/registri/{identificativo} | Dati registro
[**operatore_registri_identificativo_put**](OperatoreApi.md#operatore_registri_identificativo_put) | **PUT** /operatore/registri/{identificativo} | Modifica registro
[**operatore_registri_identificativo_xml_get**](OperatoreApi.md#operatore_registri_identificativo_xml_get) | **GET** /operatore/registri/{identificativo}/xml | Vidimazione virtuale registro in formato XML
[**operatore_registri_post**](OperatoreApi.md#operatore_registri_post) | **POST** /operatore/registri | Apertura nuovo registro
[**registri_identificativo_delete**](OperatoreApi.md#registri_identificativo_delete) | **DELETE** /registri/{identificativo} | ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Chiudi registro
[**registri_identificativo_get**](OperatoreApi.md#registri_identificativo_get) | **GET** /registri/{identificativo} | ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Dati registro
[**registri_identificativo_put**](OperatoreApi.md#registri_identificativo_put) | **PUT** /registri/{identificativo} | ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Modifica registro
[**registri_identificativo_xml_get**](OperatoreApi.md#registri_identificativo_xml_get) | **GET** /registri/{identificativo}/xml | ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo}/xml - Vidimazione virtuale registro in formato XML
[**registri_post**](OperatoreApi.md#registri_post) | **POST** /registri | ⚠️[DEPRECATO] - utilizzare /operatore/registri - Apertura nuovo registro


# **operatore_get**
> List[OperatoreModel] operatore_get(num_iscr_ass=num_iscr_ass)

Elenco degli operatori

Ritorna l'elenco degli operatori.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.operatore_model import OperatoreModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr_ass = 'num_iscr_ass_example' # str | Filtra l'elenco estraendo gli operatori delegati dal soggetto delegato identificato dal numero iscrizione indicato. (optional)

    try:
        # Elenco degli operatori
        api_response = api_instance.operatore_get(num_iscr_ass=num_iscr_ass)
        print("The response of OperatoreApi->operatore_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_ass** | **str**| Filtra l&#39;elenco estraendo gli operatori delegati dal soggetto delegato identificato dal numero iscrizione indicato. | [optional] 

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

# **operatore_identificativo_controllo_autorizzazione_albo_get**
> bool operatore_identificativo_controllo_autorizzazione_albo_get(identificativo)

Consultazione autorizzazioni Albo

Restituisce se un operatore, identificato dal codice fiscale, è autorizzato oppure no all'Albo Nazionale Gestori Ambientali secondo quanto comunicato dall'operatore al momento dell’iscrizione al RENTRI.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Codice fiscale dell'operatore

    try:
        # Consultazione autorizzazioni Albo
        api_response = api_instance.operatore_identificativo_controllo_autorizzazione_albo_get(identificativo)
        print("The response of OperatoreApi->operatore_identificativo_controllo_autorizzazione_albo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_identificativo_controllo_autorizzazione_albo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Codice fiscale dell&#39;operatore | 

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True se esistono autorizzazioni, false altrimenti |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_identificativo_controllo_iscrizione_get**
> bool operatore_identificativo_controllo_iscrizione_get(identificativo)

Consultazione iscrizioni

Restituisce se un operatore, identificato dal codice fiscale, è iscritto o no al RENTRI<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Codice fiscale dell'operatore

    try:
        # Consultazione iscrizioni
        api_response = api_instance.operatore_identificativo_controllo_iscrizione_get(identificativo)
        print("The response of OperatoreApi->operatore_identificativo_controllo_iscrizione_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_identificativo_controllo_iscrizione_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Codice fiscale dell&#39;operatore | 

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True se l&#39;operatore con il codice fiscale indicato risulta iscritto, false altrimenti |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get**
> bool operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get(identificativo, comune_id, attivita=attivita)

Consultazione autorizzazioni unità locali

Restituisce se un operatore, identificato dal codice fiscale, è autorizzato oppure no, relativamente alle unità locali di un comune, secondo quanto comunicato dall'operatore al momento dell’iscrizione al RENTRI.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Codice fiscale dell'operatore
    comune_id = 'comune_id_example' # str | ISTAT comune dell'unità locale
    attivita = rentri_anagrafiche.OperazioniRecuperoSmaltimento() # OperazioniRecuperoSmaltimento | Attività di recupero/smaltimento (optional)

    try:
        # Consultazione autorizzazioni unità locali
        api_response = api_instance.operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get(identificativo, comune_id, attivita=attivita)
        print("The response of OperatoreApi->operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_identificativo_siti_comune_id_controllo_autorizzazioni_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Codice fiscale dell&#39;operatore | 
 **comune_id** | **str**| ISTAT comune dell&#39;unità locale | 
 **attivita** | [**OperazioniRecuperoSmaltimento**](.md)| Attività di recupero/smaltimento | [optional] 

### Return type

**bool**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True se esistono autorizzazioni, false altrimenti |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_num_iscr_autorizzazione_albo_get**
> AutAlboModel operatore_num_iscr_autorizzazione_albo_get(num_iscr)

Informazioni autorizzazione Albo

Restituisce le informazioni sull'autorizzazione all'Albo Nazionale Gestori Ambientali comunicata dall'operatore al momento dell'iscrizione al RENTRI.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.aut_albo_model import AutAlboModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr = 'num_iscr_example' # str | Numero iscrizione operatore rilasciato all'iscrizione. Per recuperare il numero iscrizione attribuito all'operatore consultare l'operazione Elenco Operatori iscritti nell'area riservata Operatori dove è presente la voce Num. iscr. operatore.

    try:
        # Informazioni autorizzazione Albo
        api_response = api_instance.operatore_num_iscr_autorizzazione_albo_get(num_iscr)
        print("The response of OperatoreApi->operatore_num_iscr_autorizzazione_albo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_num_iscr_autorizzazione_albo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr** | **str**| Numero iscrizione operatore rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione attribuito all&#39;operatore consultare l&#39;operazione Elenco Operatori iscritti nell&#39;area riservata Operatori dove è presente la voce Num. iscr. operatore. | 

### Return type

[**AutAlboModel**](AutAlboModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dati dell&#39;autorizzazione all&#39;Albo Nazionale Gestori Ambientali. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_num_iscr_siti_get**
> List[SitoModel] operatore_num_iscr_siti_get(num_iscr, provincia_id=provincia_id, comune_id=comune_id, num_iscr_sito=num_iscr_sito, num_iscr_siti=num_iscr_siti, nome_sito=nome_sito, stato_delega_da_confermare=stato_delega_da_confermare, delega_da_associazione=delega_da_associazione, stato_delega=stato_delega, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco unità locali

Ottiene l'elenco delle unità locali di un operatore.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.sito_model import SitoModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr = 'num_iscr_example' # str | Numero iscrizione operatore rilasciato all'iscrizione. Per recuperare il numero iscrizione attribuito all'operatore consultare l'operazione Elenco Operatori iscritti nell'area riservata Operatori dove è presente la voce Num. iscr. operatore.
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
        api_response = api_instance.operatore_num_iscr_siti_get(num_iscr, provincia_id=provincia_id, comune_id=comune_id, num_iscr_sito=num_iscr_sito, num_iscr_siti=num_iscr_siti, nome_sito=nome_sito, stato_delega_da_confermare=stato_delega_da_confermare, delega_da_associazione=delega_da_associazione, stato_delega=stato_delega, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of OperatoreApi->operatore_num_iscr_siti_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_num_iscr_siti_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr** | **str**| Numero iscrizione operatore rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione attribuito all&#39;operatore consultare l&#39;operazione Elenco Operatori iscritti nell&#39;area riservata Operatori dove è presente la voce Num. iscr. operatore. | 
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
**200** | Elenco delle unità locali |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get**
> List[AutRecerModel] operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get(num_iscr, num_iscr_sito)

Informazioni sulle autorizzazioni dell'unità locale

Restituisce le informazioni sull'autorizzazione comunicate dall'operatore al momento dell'iscrizione al RENTRI relativamente l'unità locale.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.aut_recer_model import AutRecerModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr = 'num_iscr_example' # str | Numero iscrizione operatore rilasciato all'iscrizione. Per recuperare il numero iscrizione attribuito all'operatore consultare l'operazione Elenco Operatori iscritti nell'area riservata Operatori dove è presente la voce Num. iscr. operatore.
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione.

    try:
        # Informazioni sulle autorizzazioni dell'unità locale
        api_response = api_instance.operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get(num_iscr, num_iscr_sito)
        print("The response of OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_autorizzazioni_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr** | **str**| Numero iscrizione operatore rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione attribuito all&#39;operatore consultare l&#39;operazione Elenco Operatori iscritti nell&#39;area riservata Operatori dove è presente la voce Num. iscr. operatore. | 
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione. | 

### Return type

[**List[AutRecerModel]**](AutRecerModel.md)

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

# **operatore_num_iscr_siti_num_iscr_sito_get**
> SitoModel operatore_num_iscr_siti_num_iscr_sito_get(num_iscr, num_iscr_sito)

Dati dell'unità locale

Ottiene il dettaglio dell'unità locale.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.sito_model import SitoModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr = 'num_iscr_example' # str | Numero iscrizione operatore rilasciato all'iscrizione. Per recuperare il numero iscrizione attribuito all'operatore consultare l'operazione Elenco Operatori iscritti nell'area riservata Operatori dove è presente la voce Num. iscr. operatore.
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione.

    try:
        # Dati dell'unità locale
        api_response = api_instance.operatore_num_iscr_siti_num_iscr_sito_get(num_iscr, num_iscr_sito)
        print("The response of OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr** | **str**| Numero iscrizione operatore rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione attribuito all&#39;operatore consultare l&#39;operazione Elenco Operatori iscritti nell&#39;area riservata Operatori dove è presente la voce Num. iscr. operatore. | 
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
**200** | Dati dell&#39;unità locale. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_num_iscr_siti_num_iscr_sito_registri_get**
> List[RegistroModel] operatore_num_iscr_siti_num_iscr_sito_registri_get(num_iscr, num_iscr_sito, identificativo_operatore=identificativo_operatore, identificativo=identificativo, chiuso=chiuso, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco registri

Ottiene l'elenco dei registri, filtrati in base ai criteri specificati.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    num_iscr = 'num_iscr_example' # str | Numero iscrizione operatore rilasciato all'iscrizione. Per recuperare l'identificativo attribuito all'operatore consultare l'operazione Elenco Operatori iscritti nell'area riservata Operatori dove è presente la voce Num. iscr. operatore.
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione.
    identificativo_operatore = 'identificativo_operatore_example' # str | Codice fiscale dell'operatore da ricercare. (optional)
    identificativo = 'identificativo_example' # str | Identificativo del registro da ricercare. (optional)
    chiuso = True # bool | Flag di chiusura del registro. (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize. (optional) (default to 100)

    try:
        # Elenco registri
        api_response = api_instance.operatore_num_iscr_siti_num_iscr_sito_registri_get(num_iscr, num_iscr_sito, identificativo_operatore=identificativo_operatore, identificativo=identificativo, chiuso=chiuso, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_registri_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_num_iscr_siti_num_iscr_sito_registri_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr** | **str**| Numero iscrizione operatore rilasciato all&#39;iscrizione. Per recuperare l&#39;identificativo attribuito all&#39;operatore consultare l&#39;operazione Elenco Operatori iscritti nell&#39;area riservata Operatori dove è presente la voce Num. iscr. operatore. | 
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione. | 
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
**200** | Lista dei registri. |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Operazione non consentita. |  -  |
**404** | Operatore o unità locale non trovata. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operatore_registri_identificativo_delete**
> operatore_registri_identificativo_delete(identificativo)

Chiudi registro

Chiude un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.

    try:
        # Chiudi registro
        api_instance.operatore_registri_identificativo_delete(identificativo)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_registri_identificativo_delete: %s\n" % e)
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

# **operatore_registri_identificativo_get**
> RegistroModel operatore_registri_identificativo_get(identificativo)

Dati registro

Ottiene il dettaglio di un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # Dati registro
        api_response = api_instance.operatore_registri_identificativo_get(identificativo)
        print("The response of OperatoreApi->operatore_registri_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_registri_identificativo_get: %s\n" % e)
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

# **operatore_registri_identificativo_put**
> UpdateRegistroResponse operatore_registri_identificativo_put(identificativo, update_registro_operatore_request=update_registro_operatore_request)

Modifica registro

Modifica di un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.update_registro_operatore_request import UpdateRegistroOperatoreRequest
from rentri_anagrafiche.models.update_registro_response import UpdateRegistroResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.
    update_registro_operatore_request = rentri_anagrafiche.UpdateRegistroOperatoreRequest() # UpdateRegistroOperatoreRequest | Dati di modifica del registro (optional)

    try:
        # Modifica registro
        api_response = api_instance.operatore_registri_identificativo_put(identificativo, update_registro_operatore_request=update_registro_operatore_request)
        print("The response of OperatoreApi->operatore_registri_identificativo_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_registri_identificativo_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro da chiudere. | 
 **update_registro_operatore_request** | [**UpdateRegistroOperatoreRequest**](UpdateRegistroOperatoreRequest.md)| Dati di modifica del registro | [optional] 

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

# **operatore_registri_identificativo_xml_get**
> DownloadableBaseResponse operatore_registri_identificativo_xml_get(identificativo)

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

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # Vidimazione virtuale registro in formato XML
        api_response = api_instance.operatore_registri_identificativo_xml_get(identificativo)
        print("The response of OperatoreApi->operatore_registri_identificativo_xml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_registri_identificativo_xml_get: %s\n" % e)
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

# **operatore_registri_post**
> CreateRegistroResponse operatore_registri_post(create_registro_request=create_registro_request)

Apertura nuovo registro

Apre un nuovo registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.create_registro_request import CreateRegistroRequest
from rentri_anagrafiche.models.create_registro_response import CreateRegistroResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    create_registro_request = rentri_anagrafiche.CreateRegistroRequest() # CreateRegistroRequest | Richiesta. (optional)

    try:
        # Apertura nuovo registro
        api_response = api_instance.operatore_registri_post(create_registro_request=create_registro_request)
        print("The response of OperatoreApi->operatore_registri_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->operatore_registri_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_registro_request** | [**CreateRegistroRequest**](CreateRegistroRequest.md)| Richiesta. | [optional] 

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

# **registri_identificativo_delete**
> registri_identificativo_delete(identificativo)

⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Chiudi registro

Chiude un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.

    try:
        # ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Chiudi registro
        api_instance.registri_identificativo_delete(identificativo)
    except Exception as e:
        print("Exception when calling OperatoreApi->registri_identificativo_delete: %s\n" % e)
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

# **registri_identificativo_get**
> RegistroModel registri_identificativo_get(identificativo)

⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Dati registro

Ottiene il dettaglio di un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre una risposta vuota) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Dati registro
        api_response = api_instance.registri_identificativo_get(identificativo)
        print("The response of OperatoreApi->registri_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->registri_identificativo_get: %s\n" % e)
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

# **registri_identificativo_put**
> UpdateRegistroResponse registri_identificativo_put(identificativo, update_registro_operatore_request=update_registro_operatore_request)

⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Modifica registro

Modifica di un registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.update_registro_operatore_request import UpdateRegistroOperatoreRequest
from rentri_anagrafiche.models.update_registro_response import UpdateRegistroResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro da chiudere.
    update_registro_operatore_request = rentri_anagrafiche.UpdateRegistroOperatoreRequest() # UpdateRegistroOperatoreRequest | Dati di modifica del registro (optional)

    try:
        # ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo} - Modifica registro
        api_response = api_instance.registri_identificativo_put(identificativo, update_registro_operatore_request=update_registro_operatore_request)
        print("The response of OperatoreApi->registri_identificativo_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->registri_identificativo_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo** | **str**| Identificativo del registro da chiudere. | 
 **update_registro_operatore_request** | [**UpdateRegistroOperatoreRequest**](UpdateRegistroOperatoreRequest.md)| Dati di modifica del registro | [optional] 

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

# **registri_identificativo_xml_get**
> DownloadableBaseResponse registri_identificativo_xml_get(identificativo)

⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo}/xml - Vidimazione virtuale registro in formato XML

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

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    identificativo = 'identificativo_example' # str | Identificativo del registro.

    try:
        # ⚠️[DEPRECATO] - utilizzare /operatore/registri/{identificativo}/xml - Vidimazione virtuale registro in formato XML
        api_response = api_instance.registri_identificativo_xml_get(identificativo)
        print("The response of OperatoreApi->registri_identificativo_xml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->registri_identificativo_xml_get: %s\n" % e)
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

# **registri_post**
> CreateRegistroResponse registri_post(create_registro_request=create_registro_request)

⚠️[DEPRECATO] - utilizzare /operatore/registri - Apertura nuovo registro

Apre un nuovo registro.<hr/><i>Servizio richiamabile in modalità <b>STUB</b> (le richieste restituiranno sempre un codice di stato 422) anche in ambiente di produzione.</i><hr/>

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_anagrafiche
from rentri_anagrafiche.models.create_registro_request import CreateRegistroRequest
from rentri_anagrafiche.models.create_registro_response import CreateRegistroResponse
from rentri_anagrafiche.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/anagrafiche/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_anagrafiche.Configuration(
    host = "https://api.rentri.gov.it/anagrafiche/v1.0"
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
    api_instance = rentri_anagrafiche.OperatoreApi(api_client)
    create_registro_request = rentri_anagrafiche.CreateRegistroRequest() # CreateRegistroRequest | Richiesta. (optional)

    try:
        # ⚠️[DEPRECATO] - utilizzare /operatore/registri - Apertura nuovo registro
        api_response = api_instance.registri_post(create_registro_request=create_registro_request)
        print("The response of OperatoreApi->registri_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperatoreApi->registri_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_registro_request** | [**CreateRegistroRequest**](CreateRegistroRequest.md)| Richiesta. | [optional] 

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

