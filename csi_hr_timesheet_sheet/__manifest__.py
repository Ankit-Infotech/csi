# -*- coding: utf-8 -*-

{
    'name': "CSI HR Timesheet",
    'summary': "Customise HR Timesheet",
    'description': """
        Customise HR Timesheet for some modification:
            - Hide Approve button when current user look, own timesheet(Used attrs in inherit form view).
      """,
    'author': "Ankit H Gandhi",
    'website': " ",
    'category': "customise",
    'version': "1.0",
    'depends': [
        'hr_timesheet_sheet'
    ],
    'data': [
        'views/inherited_hr_timesheet_sheet_views.xml'
    ],
}