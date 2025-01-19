# AutRecerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_autorizzazione** | [**TipiAutorizzazione**](TipiAutorizzazione.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;RecSmalArt208&lt;/i&gt; - Autorizzazione unica per i nuovi impianti di recupero/smaltimento - art. 208 decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RecSmalImpMobiliArt208&lt;/i&gt; - Autorizzazione all&#39;esercizio di operazioni di recupero e/o smaltimento dei rifiuti con impianti mobili - art.208, comma 15 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RicercaSperimentazione&lt;/i&gt; - Autorizzazione alla realizzazione di impianti di ricerca e sperimentazione - art. 211 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;AIA&lt;/i&gt; - Autorizzazione Integrata Ambientale - artt. 29-ter e 213 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RecProcSemplificata&lt;/i&gt; - Operazioni di recupero mediante Comunicazione in \&quot;Procedura Semplificata\&quot; - artt.214 e 216 del decreto legislativo 3 aprile 2006, n. 152e autorizzazione unica ambientale (AUA) - Decreto Presidente Repubblica n. 59 del 13 marzo 2013.&lt;/li&gt;&lt;li&gt;&lt;i&gt;OpBonifica&lt;/i&gt; - Provvedimenti che autorizzano le operazioni di bonifica, ai sensi del comma 7 dell’art. 242 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Straordinario&lt;/i&gt; - Autorizzazioni “straordinarie” art. 191 del decreto legislativo 3 aprile 2006, n. 152 (attività svolte in regime di ordinanza contingibile e urgente)&lt;/li&gt;&lt;li&gt;&lt;i&gt;ComTrattamentoAcqueReflue&lt;/i&gt; - Comunicazione al trattamento di rifiuti e materiali in impianti di trattamento di acque reflue urbane - art. 110 c.3 del D.Lgs. 152/2006&lt;/li&gt;&lt;li&gt;&lt;i&gt;AutTrattamentoAcqueReflue&lt;/i&gt; - Autorizzazione  al trattamento di rifiuti liquidi in impianti di trattamento di acque reflue urbane - artt. 110 c.2 con provvedimento secondo artt. 208 oppure 29-ter e 213 del D.Lgs. 152/2006&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**autorizzazione_rif** | **str** |  | [optional] 
**data_rilascio** | **datetime** |  | [optional] 
**data_scadenza** | **datetime** |  | [optional] 
**attivita_recupero_smaltimento** | [**List[OperazioniRecuperoSmaltimento]**](OperazioniRecuperoSmaltimento.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;R1&lt;/i&gt; - Utilizzazione principale come combustibile o come altro mezzo per produrre energia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R2&lt;/i&gt; - Rigenerazione/recupero di solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R3&lt;/i&gt; - Riciclo/recupero delle sostanze organiche non utilizzate come solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R4&lt;/i&gt; - Riciclo/recupero dei metalli e dei composti metallici&lt;/li&gt;&lt;li&gt;&lt;i&gt;R5&lt;/i&gt; - Riciclo/recupero di altre sostanze inorganiche&lt;/li&gt;&lt;li&gt;&lt;i&gt;R6&lt;/i&gt; - Rigenerazione degli acidi o delle basi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R7&lt;/i&gt; - Recupero dei prodotti che servono a captare gli inquinanti&lt;/li&gt;&lt;li&gt;&lt;i&gt;R8&lt;/i&gt; - Recupero dei prodotti provenienti dai catalizzatori&lt;/li&gt;&lt;li&gt;&lt;i&gt;R9&lt;/i&gt; - Rigenerazione o altri reimpieghi degli oli&lt;/li&gt;&lt;li&gt;&lt;i&gt;R10&lt;/i&gt; - Spandimento sul suolo a beneficio dell&#39;agricoltura o dell&#39;ecologia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R11&lt;/i&gt; - Utilizzazione di rifiuti ottenuti da una delle operazioni indicate da R1 a R10&lt;/li&gt;&lt;li&gt;&lt;i&gt;R12&lt;/i&gt; - Scambio di rifiuti per sottoporli a una delle operazioni indicate da R1 a R11&lt;/li&gt;&lt;li&gt;&lt;i&gt;R13&lt;/i&gt; - Messa in riserva di rifiuti per sottoporli a una delle operazioni indicate nei punti da R1 a R12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D1&lt;/i&gt; - Deposito sul o nel suolo&lt;/li&gt;&lt;li&gt;&lt;i&gt;D2&lt;/i&gt; - Trattamento in ambiente terrestre&lt;/li&gt;&lt;li&gt;&lt;i&gt;D3&lt;/i&gt; - Iniezioni in profondità&lt;/li&gt;&lt;li&gt;&lt;i&gt;D4&lt;/i&gt; - Lagunaggio&lt;/li&gt;&lt;li&gt;&lt;i&gt;D5&lt;/i&gt; - Messa in discarica specialmente allestita&lt;/li&gt;&lt;li&gt;&lt;i&gt;D6&lt;/i&gt; - Scarico dei rifiuti solidi nell&#39;ambiente idrico eccetto l&#39;immersione&lt;/li&gt;&lt;li&gt;&lt;i&gt;D7&lt;/i&gt; - Immersione, compreso il seppellimento nel sottosuolo marino&lt;/li&gt;&lt;li&gt;&lt;i&gt;D8&lt;/i&gt; - Trattamento biologico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D9&lt;/i&gt; - Trattamento fisico-chimico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D10&lt;/i&gt; - Incenerimento a terra&lt;/li&gt;&lt;li&gt;&lt;i&gt;D11&lt;/i&gt; - Incenerimento in mare&lt;/li&gt;&lt;li&gt;&lt;i&gt;D12&lt;/i&gt; - Deposito permanente&lt;/li&gt;&lt;li&gt;&lt;i&gt;D13&lt;/i&gt; - Raggruppamento preliminare prima di una delle operazioni di cui ai punti da D1 a D12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D14&lt;/i&gt; - Ricondizionamento preliminare prima di una delle operazioni di cui ai punti da D1 a D13&lt;/li&gt;&lt;li&gt;&lt;i&gt;D15&lt;/i&gt; - Deposito preliminare prima di una delle operazioni di cui ai punti da D1 a D14&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 

## Example

```python
from rentri_anagrafiche.models.aut_recer_model import AutRecerModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutRecerModel from a JSON string
aut_recer_model_instance = AutRecerModel.from_json(json)
# print the JSON string representation of the object
print(AutRecerModel.to_json())

# convert the object into a dict
aut_recer_model_dict = aut_recer_model_instance.to_dict()
# create an instance of AutRecerModel from a dict
aut_recer_model_from_dict = AutRecerModel.from_dict(aut_recer_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


