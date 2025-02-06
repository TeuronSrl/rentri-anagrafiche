# SitoDelegaAssModel

Stato delega soggetto delegato

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_associazione** | **str** |  | [optional] 
**stato_delega_ass** | [**Stati**](Stati.md) |  | [optional] 
**data_conferma** | **datetime** |  | [optional] 
**data_revoca** | **datetime** |  | [optional] 
**da_associazione** | **bool** |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.sito_delega_ass_model import SitoDelegaAssModel

# TODO update the JSON string below
json = "{}"
# create an instance of SitoDelegaAssModel from a JSON string
sito_delega_ass_model_instance = SitoDelegaAssModel.from_json(json)
# print the JSON string representation of the object
print SitoDelegaAssModel.to_json()

# convert the object into a dict
sito_delega_ass_model_dict = sito_delega_ass_model_instance.to_dict()
# create an instance of SitoDelegaAssModel from a dict
sito_delega_ass_model_from_dict = SitoDelegaAssModel.from_dict(sito_delega_ass_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


