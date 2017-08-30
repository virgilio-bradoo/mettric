# -*- coding: utf-8 -*-
{
    'name': "mettric",

    'summary': """
        Módulo que carrega os módulos básicos e dados básicos da Mettric
        """,

    'description': """
        Módulo que carrega os módulos base: Contabilidade, NFse, Localização Brasileira, Boleto e CNAB
    """,

    'author': "Virgílio Santos, BradooTech",
    'website': "http://www.bradootech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'br_cnab', 'br_zip', 'br_account_einvoice',
                'br_data_account', 'br_base', 'br_account', 'br_nfe',
                'br_nfse', 'br_boleto', 'sync_numero_nfse_bradoo',
                'coa_bradoo', 'ir_csll_bradoo', 'reemissao_nfs_bradoo'
                ],

    # always loaded
    'data': [
        'data/res_company.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'post_init_hook': 'execute_default',
}