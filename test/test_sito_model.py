# coding: utf-8

"""
    anagrafiche

    Servizio Anagrafica RENTRI

    The version of the OpenAPI document: 1.0.20250114-603
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rentri_anagrafiche.models.sito_model import SitoModel

class TestSitoModel(unittest.TestCase):
    """SitoModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SitoModel:
        """Test SitoModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SitoModel`
        """
        model = SitoModel()
        if include_optional:
            return SitoModel(
                num_iscr_sito = '',
                num_iscr_operatore = '',
                denominazione_operatore = '',
                identificativo_operatore = '',
                ipa_operatore = '',
                nome = '',
                is_sede_legale = True,
                comune_id = '',
                provincia_id = '',
                indirizzo = '',
                civico = '',
                cciaari = '',
                progressivo_ri = 56,
                cu_aoo = '',
                cuu = '',
                deleghe_ass = [
                    rentri_anagrafiche.models.sito_delega_ass_model.SitoDelegaAssModel(
                        num_iscr_associazione = '', 
                        stato_delega_ass = null, 
                        data_conferma = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        data_revoca = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        da_associazione = True, )
                    ],
                attivita = [
                    'CentroRaccolta'
                    ],
                data_iscrizione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data_cancellazione = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SitoModel(
        )
        """

    def testSitoModel(self):
        """Test SitoModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
