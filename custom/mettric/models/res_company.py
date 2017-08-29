# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OriginPartner(models.Model):
    _inherit = 'res.company'

    '''
    Metodo chamado por data, que seta as configurações padrão da company
    '''
    @api.model
    def _set_default_company(self):
        country = self.env['res.country'].search([('name','=','Brasil')]).id
        state = self.env['res.country.state'].search([('name','=','São Paulo')]).id
        city = self.env['res.state.city'].search([('name','=','São Paulo')]).id
        currency = self.env['res.currency'].search([('name','=','BRL')]).id

        self.search([('id','=',1)]).write({
            'name': 'Mettric',
            'rml_header1':'Mettric Certificados Digitais',
            'legal_name': 'METTRIC CERTIFICADOS DIGITAIS EIRELI',
            'zip':'01311-000',
            'street': 'Avenida Paulista',
            'number':1471,
            'street2':'CONJ 601',
            'district':'Bela Vista',
            'phone':'(11) 3141­0605',
            'email':'',
            'cnpj_cpf':'96584743000125',
            'website':'http://www.mettric.com.br',
            'country_id':country,
            'state_id':state,
            'city_id':city,
            'currency_id':currency,
            'inscr_mun':21573867,
        })