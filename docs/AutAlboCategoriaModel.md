# AutAlboCategoriaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoria** | **str** |  | [optional] 
**classe** | **str** |  | [optional] 
**stato** | [**StatiCatAlbo**](StatiCatAlbo.md) |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.aut_albo_categoria_model import AutAlboCategoriaModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutAlboCategoriaModel from a JSON string
aut_albo_categoria_model_instance = AutAlboCategoriaModel.from_json(json)
# print the JSON string representation of the object
print AutAlboCategoriaModel.to_json()

# convert the object into a dict
aut_albo_categoria_model_dict = aut_albo_categoria_model_instance.to_dict()
# create an instance of AutAlboCategoriaModel from a dict
aut_albo_categoria_model_from_dict = AutAlboCategoriaModel.from_dict(aut_albo_categoria_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


