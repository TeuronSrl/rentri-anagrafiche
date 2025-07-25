# coding: utf-8

# flake8: noqa

"""
    anagrafiche

    Servizio Anagrafica RENTRI

    The version of the OpenAPI document: 1.0.20250114-603
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from rentri_anagrafiche.api.operatore_api import OperatoreApi
from rentri_anagrafiche.api.soggetto_delegato_api import SoggettoDelegatoApi
from rentri_anagrafiche.api.default_api import DefaultApi

# import ApiClient
from rentri_anagrafiche.api_response import ApiResponse
from rentri_anagrafiche.api_client import ApiClient
from rentri_anagrafiche.configuration import Configuration
from rentri_anagrafiche.exceptions import OpenApiException
from rentri_anagrafiche.exceptions import ApiTypeError
from rentri_anagrafiche.exceptions import ApiValueError
from rentri_anagrafiche.exceptions import ApiKeyError
from rentri_anagrafiche.exceptions import ApiAttributeError
from rentri_anagrafiche.exceptions import ApiException

# import models into sdk package
from rentri_anagrafiche.models.attivita import Attivita
from rentri_anagrafiche.models.aut_albo_categoria_model import AutAlboCategoriaModel
from rentri_anagrafiche.models.aut_albo_model import AutAlboModel
from rentri_anagrafiche.models.aut_recer_model import AutRecerModel
from rentri_anagrafiche.models.create_registro_request import CreateRegistroRequest
from rentri_anagrafiche.models.create_registro_response import CreateRegistroResponse
from rentri_anagrafiche.models.create_registro_soggetto_delegato_request import CreateRegistroSoggettoDelegatoRequest
from rentri_anagrafiche.models.downloadable_base_response import DownloadableBaseResponse
from rentri_anagrafiche.models.operatore_model import OperatoreModel
from rentri_anagrafiche.models.operazioni_recupero_smaltimento import OperazioniRecuperoSmaltimento
from rentri_anagrafiche.models.problem_details import ProblemDetails
from rentri_anagrafiche.models.profili_soggetto import ProfiliSoggetto
from rentri_anagrafiche.models.registro_model import RegistroModel
from rentri_anagrafiche.models.sito_delega_ass_model import SitoDelegaAssModel
from rentri_anagrafiche.models.sito_model import SitoModel
from rentri_anagrafiche.models.stati import Stati
from rentri_anagrafiche.models.stati_cat_albo import StatiCatAlbo
from rentri_anagrafiche.models.tipi_autorizzazione import TipiAutorizzazione
from rentri_anagrafiche.models.update_registro_operatore_request import UpdateRegistroOperatoreRequest
from rentri_anagrafiche.models.update_registro_request import UpdateRegistroRequest
from rentri_anagrafiche.models.update_registro_response import UpdateRegistroResponse
