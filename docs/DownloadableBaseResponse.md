# DownloadableBaseResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome_file** | **str** | Nome del file | [optional] 
**mime** | **str** | Tipo MIME del file | [optional] 
**content** | **bytearray** | Contenuto del file | [optional] 

## Example

```python
from rentri_anagrafiche.models.downloadable_base_response import DownloadableBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadableBaseResponse from a JSON string
downloadable_base_response_instance = DownloadableBaseResponse.from_json(json)
# print the JSON string representation of the object
print DownloadableBaseResponse.to_json()

# convert the object into a dict
downloadable_base_response_dict = downloadable_base_response_instance.to_dict()
# create an instance of DownloadableBaseResponse from a dict
downloadable_base_response_from_dict = DownloadableBaseResponse.from_dict(downloadable_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


