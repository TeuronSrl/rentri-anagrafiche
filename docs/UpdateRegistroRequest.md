# UpdateRegistroRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descrizione** | **str** | Descrizione del registro | 

## Example

```python
from rentri_anagrafiche.models.update_registro_request import UpdateRegistroRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRegistroRequest from a JSON string
update_registro_request_instance = UpdateRegistroRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRegistroRequest.to_json())

# convert the object into a dict
update_registro_request_dict = update_registro_request_instance.to_dict()
# create an instance of UpdateRegistroRequest from a dict
update_registro_request_from_dict = UpdateRegistroRequest.from_dict(update_registro_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


