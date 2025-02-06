# RegistroModel

Registro

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**data_creazione** | **datetime** |  | [optional] 
**data_chiusura** | **datetime** |  | [optional] 
**data_modifica** | **datetime** |  | [optional] 
**num_iscr_associazione** | **str** |  | [optional] 
**identificativo_associazione** | **str** |  | [optional] 
**num_iscr_sito** | **str** |  | [optional] 
**identificativo_operatore_sito** | **str** |  | [optional] 
**operatore_sito** | **str** |  | [optional] 
**ipa_operatore_sito** | **str** |  | [optional] 
**cu_aoo_sito** | **str** |  | [optional] 
**cuu_sito** | **str** |  | [optional] 
**attivita** | [**List[Attivita]**](Attivita.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;CentroRaccolta&lt;/i&gt; - Centro di raccolta&lt;/li&gt;&lt;li&gt;&lt;i&gt;Produzione&lt;/i&gt; - Produzione di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Recupero&lt;/i&gt; - Recupero di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Smaltimento&lt;/i&gt; - Smaltimento di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;Trasporto&lt;/i&gt; - Trasporto di rifiuti&lt;/li&gt;&lt;li&gt;&lt;i&gt;IntermediazioneSenzaDetenzione&lt;/i&gt; - Intermediazione e commercio di rifiuti senza detenzione&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**attivita_rec_smalt** | [**List[OperazioniRecuperoSmaltimento]**](OperazioniRecuperoSmaltimento.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;R1&lt;/i&gt; - Utilizzazione principale come combustibile o come altro mezzo per produrre energia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R2&lt;/i&gt; - Rigenerazione/recupero di solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R3&lt;/i&gt; - Riciclo/recupero delle sostanze organiche non utilizzate come solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R4&lt;/i&gt; - Riciclo/recupero dei metalli e dei composti metallici&lt;/li&gt;&lt;li&gt;&lt;i&gt;R5&lt;/i&gt; - Riciclo/recupero di altre sostanze inorganiche&lt;/li&gt;&lt;li&gt;&lt;i&gt;R6&lt;/i&gt; - Rigenerazione degli acidi o delle basi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R7&lt;/i&gt; - Recupero dei prodotti che servono a captare gli inquinanti&lt;/li&gt;&lt;li&gt;&lt;i&gt;R8&lt;/i&gt; - Recupero dei prodotti provenienti dai catalizzatori&lt;/li&gt;&lt;li&gt;&lt;i&gt;R9&lt;/i&gt; - Rigenerazione o altri reimpieghi degli oli&lt;/li&gt;&lt;li&gt;&lt;i&gt;R10&lt;/i&gt; - Spandimento sul suolo a beneficio dell&#39;agricoltura o dell&#39;ecologia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R11&lt;/i&gt; - Utilizzazione di rifiuti ottenuti da una delle operazioni indicate da R1 a R10&lt;/li&gt;&lt;li&gt;&lt;i&gt;R12&lt;/i&gt; - Scambio di rifiuti per sottoporli a una delle operazioni indicate da R1 a R11&lt;/li&gt;&lt;li&gt;&lt;i&gt;R13&lt;/i&gt; - Messa in riserva di rifiuti per sottoporli a una delle operazioni indicate nei punti da R1 a R12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D1&lt;/i&gt; - Deposito sul o nel suolo&lt;/li&gt;&lt;li&gt;&lt;i&gt;D2&lt;/i&gt; - Trattamento in ambiente terrestre&lt;/li&gt;&lt;li&gt;&lt;i&gt;D3&lt;/i&gt; - Iniezioni in profondità&lt;/li&gt;&lt;li&gt;&lt;i&gt;D4&lt;/i&gt; - Lagunaggio&lt;/li&gt;&lt;li&gt;&lt;i&gt;D5&lt;/i&gt; - Messa in discarica specialmente allestita&lt;/li&gt;&lt;li&gt;&lt;i&gt;D6&lt;/i&gt; - Scarico dei rifiuti solidi nell&#39;ambiente idrico eccetto l&#39;immersione&lt;/li&gt;&lt;li&gt;&lt;i&gt;D7&lt;/i&gt; - Immersione, compreso il seppellimento nel sottosuolo marino&lt;/li&gt;&lt;li&gt;&lt;i&gt;D8&lt;/i&gt; - Trattamento biologico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D9&lt;/i&gt; - Trattamento fisico-chimico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D10&lt;/i&gt; - Incenerimento a terra&lt;/li&gt;&lt;li&gt;&lt;i&gt;D11&lt;/i&gt; - Incenerimento in mare&lt;/li&gt;&lt;li&gt;&lt;i&gt;D12&lt;/i&gt; - Deposito permanente&lt;/li&gt;&lt;li&gt;&lt;i&gt;D13&lt;/i&gt; - Raggruppamento preliminare prima di una delle operazioni di cui ai punti da D1 a D12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D14&lt;/i&gt; - Ricondizionamento preliminare prima di una delle operazioni di cui ai punti da D1 a D13&lt;/li&gt;&lt;li&gt;&lt;i&gt;D15&lt;/i&gt; - Deposito preliminare prima di una delle operazioni di cui ai punti da D1 a D14&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**stato** | [**Stati**](Stati.md) |  | [optional] 
**uso_locale** | **bool** |  | [optional] 
**progressivo_inziale_locale** | **int** |  | [optional] 

## Example

```python
from rentri_anagrafiche.models.registro_model import RegistroModel

# TODO update the JSON string below
json = "{}"
# create an instance of RegistroModel from a JSON string
registro_model_instance = RegistroModel.from_json(json)
# print the JSON string representation of the object
print RegistroModel.to_json()

# convert the object into a dict
registro_model_dict = registro_model_instance.to_dict()
# create an instance of RegistroModel from a dict
registro_model_from_dict = RegistroModel.from_dict(registro_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


