# SitoModel

Unità locale

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | [optional] 
**num_iscr_operatore** | **str** |  | [optional] 
**denominazione_operatore** | **str** |  | [optional] 
**identificativo_operatore** | **str** |  | [optional] 
**ipa_operatore** | **str** |  | [optional] 
**nome** | **str** |  | [optional] 
**is_sede_legale** | **bool** |  | [optional] 
**comune_id** | **str** |  | [optional] 
**provincia_id** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**civico** | **str** |  | [optional] 
**cciaari** | **str** |  | [optional] 
**progressivo_ri** | **int** |  | [optional] 
**cu_aoo** | **str** |  | [optional] 
**cuu** | **str** |  | [optional] 
**deleghe_ass** | [**List[SitoDelegaAssModel]**](SitoDelegaAssModel.md) |  | [optional] 
**attivita** | [**List[Attivita]**](Attivita.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;CentroRaccolta&lt;/i&gt; - Centro di raccolta&lt;/li&gt;&lt;li&gt;&lt;i&gt;Produzione&lt;/i&gt; - Produzione di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Recupero&lt;/i&gt; - Recupero di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Smaltimento&lt;/i&gt; - Smaltimento di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Trasporto&lt;/i&gt; - Trasporto di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;IntermediazioneSenzaDetenzione&lt;/i&gt; - Intermediazione e commercio di rifiuti senza detenzione&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**data_iscrizione** | **datetime** |  | [optional] 
**data_cancellazione** | **datetime** |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.sito_model import SitoModel

# TODO update the JSON string below
json = "{}"
# create an instance of SitoModel from a JSON string
sito_model_instance = SitoModel.from_json(json)
# print the JSON string representation of the object
print(SitoModel.to_json())

# convert the object into a dict
sito_model_dict = sito_model_instance.to_dict()
# create an instance of SitoModel from a dict
sito_model_from_dict = SitoModel.from_dict(sito_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


