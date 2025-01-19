# AutAlboModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sezione** | **str** |  | [optional] 
**numero_iscrizione** | **int** |  | [optional] 
**attiva** | **bool** |  | [optional] 
**data_iscrizione** | **datetime** |  | [optional] 
**categorie** | [**List[AutAlboCategoriaModel]**](AutAlboCategoriaModel.md) |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.aut_albo_model import AutAlboModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutAlboModel from a JSON string
aut_albo_model_instance = AutAlboModel.from_json(json)
# print the JSON string representation of the object
print(AutAlboModel.to_json())

# convert the object into a dict
aut_albo_model_dict = aut_albo_model_instance.to_dict()
# create an instance of AutAlboModel from a dict
aut_albo_model_from_dict = AutAlboModel.from_dict(aut_albo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


