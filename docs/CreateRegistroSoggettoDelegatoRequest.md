# CreateRegistroSoggettoDelegatoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero iscrizione unità locale rilasciato all&#39;iscrizione. Per recuperare l&#39;identificativo attribuito all&#39;unità locale delegante consultare l&#39;operazione Elenco unità locali deleganti  nell&#39;area riservata Soggetti delegati dove è presente la voce Num. iscr. UL. | 
**num_iscr_ass** | **str** | Numero iscrizione soggetto delegato rilasciato all&#39;iscrizione. Per recuperare il numero iscrizione soggetto delegato consultare l&#39;operazione Elenco soggetti delegati iscritti nell&#39;area riservata Soggetti delegati dove è presente la voce Numero iscrizione | 
**descrizione** | **str** | Descrizione del registro | 

## Example

```python
from rentri_anagrafiche.models.create_registro_soggetto_delegato_request import CreateRegistroSoggettoDelegatoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRegistroSoggettoDelegatoRequest from a JSON string
create_registro_soggetto_delegato_request_instance = CreateRegistroSoggettoDelegatoRequest.from_json(json)
# print the JSON string representation of the object
print CreateRegistroSoggettoDelegatoRequest.to_json()

# convert the object into a dict
create_registro_soggetto_delegato_request_dict = create_registro_soggetto_delegato_request_instance.to_dict()
# create an instance of CreateRegistroSoggettoDelegatoRequest from a dict
create_registro_soggetto_delegato_request_from_dict = CreateRegistroSoggettoDelegatoRequest.from_dict(create_registro_soggetto_delegato_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


