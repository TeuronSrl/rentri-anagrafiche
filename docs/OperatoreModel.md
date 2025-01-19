# OperatoreModel

Operatore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr** | **str** |  | [optional] 
**profilo_soggetto** | [**ProfiliSoggetto**](ProfiliSoggetto.md) |  | [optional] 
**data_iscrizione** | **datetime** |  | [optional] 
**identificativo** | **str** |  | [optional] 
**ipa** | **str** |  | [optional] 
**denominazione** | **str** |  | [optional] 
**forma_giuridica_id** | **str** |  | [optional] 
**piva** | **str** |  | [optional] 
**cciaarea** | **str** |  | [optional] 
**nrea** | **str** |  | [optional] 
**data_iscrizione_ri** | **datetime** |  | [optional] 
**stato_impresa_ri** | **str** |  | [optional] 
**dipendenti_ri** | **int** |  | [optional] 
**data_rilevazione_dipendenti_ri** | **datetime** |  | [optional] 
**nazione_slid** | **str** |  | [optional] 
**provincia_slid** | **str** |  | [optional] 
**comune_slid** | **str** |  | [optional] 
**citta_sl** | **str** |  | [optional] 
**indirizzo_sl** | **str** |  | [optional] 
**civico_sl** | **str** |  | [optional] 
**capsl** | **str** |  | [optional] 
**pec** | **str** |  | [optional] 
**cod_fisc_lr** | **str** |  | [optional] 
**cognome_lr** | **str** |  | [optional] 
**nome_lr** | **str** |  | [optional] 
**dipendenti** | **int** |  | [optional] 
**data_ultima_visura** | **datetime** |  | [optional] 
**flag_esonerato_iscr_albo** | **int** |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.operatore_model import OperatoreModel

# TODO update the JSON string below
json = "{}"
# create an instance of OperatoreModel from a JSON string
operatore_model_instance = OperatoreModel.from_json(json)
# print the JSON string representation of the object
print(OperatoreModel.to_json())

# convert the object into a dict
operatore_model_dict = operatore_model_instance.to_dict()
# create an instance of OperatoreModel from a dict
operatore_model_from_dict = OperatoreModel.from_dict(operatore_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


