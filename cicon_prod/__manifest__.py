{
    "name": "CICON Production",
    "version": "0.1",
    "author": "SA",
    "website": "http://www.cicon.ae/",
    "category": "Generic Modules/Others",
    "depends": ['mail', 'cicon_product_group_template','cicon_job_site'],
    "data": [
        'security/prod_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_project_view.xml',
        'views/customer_order_view.xml',
        'views/production_order_view.xml',
        'views/contract_lpo_view.xml',
        'wizard/change_state_wizard_view.xml',
        'wizard/report_option_wizard_view.xml',
        'views/steel_order_in_hand.xml',
        'views/customer_requisition.xml',
        'views/report.xml',
        'report/order_analysis_report_view.xml',
        'views/cicon_prod_view.xml',
        'views/delivery_order_view.xml',
        'wizard/prod_planning_wizard_view.xml',
        'views/prod_plan_report.xml'
        ],
    "description": "CICON Production Management",
    "init_xml": [],
    'update_xml': [],
    "demo_xml": [],
    'active': False,
    'installable': True,
    'application': True
}
