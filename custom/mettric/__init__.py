# -*- coding: utf-8 -*-

from . import controllers
from . import models
from models import res_company
from odoo import api, SUPERUSER_ID

def execute_default (cr, registry):
    execute_default
    env = api.Environment(cr, SUPERUSER_ID, {})

    chart = env["account.chart.template"].search([('name','=','Plano de Contas Mettric')]).id
    template = env["account.account.template"].search([('code','=','1.1.1.04')], limit=1).id
    env['account.config.settings'].create({
    	"chart_template_id": chart,
        "template_transfer_account_id": template,
    }).execute()



