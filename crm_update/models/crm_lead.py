

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, tools


class CRMLead(models.Model):
  
    _inherit = "crm.lead"
    
     
    check_one= fields.Boolean('CheckBox 1', tracking=True)
    check_two= fields.Boolean('CheckBox 2', tracking=True)
    check_tree= fields.Boolean('CheckBox 3', tracking=True)
    check_four= fields.Boolean('CheckBox 4', tracking=True)
    
    check_progress_rate = fields.Float('Check Progress',  store=True,
                                               compute="_check_progress_calculator",)
    
    @api.depends('check_one','check_two','check_tree','check_four')
    def _check_progress_calculator(self):
        
        check_progress_rate=0
        #counts=self.search_count([('check_one', '=', True),('check_two', '=', True),
                           #('check_tree', '=', True),('check_four', '=', True), ])
        
        
        
        for line in self:
            if line.check_one:
                check_progress_rate=check_progress_rate+1
            if line.check_two:
                check_progress_rate=check_progress_rate+1
            if line.check_tree:
                check_progress_rate=check_progress_rate+1
                
            if line.check_four:
                check_progress_rate=check_progress_rate+1
                
        if check_progress_rate:
            self.check_progress_rate=(check_progress_rate/4)*100   
         
            
        
    
    