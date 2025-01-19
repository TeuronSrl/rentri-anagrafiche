# UpdateRegistroResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.update_registro_response import UpdateRegistroResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRegistroResponse from a JSON string
update_registro_response_instance = UpdateRegistroResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRegistroResponse.to_json())

# convert the object into a dict
update_registro_response_dict = update_registro_response_instance.to_dict()
# create an instance of UpdateRegistroResponse from a dict
update_registro_response_from_dict = UpdateRegistroResponse.from_dict(update_registro_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


