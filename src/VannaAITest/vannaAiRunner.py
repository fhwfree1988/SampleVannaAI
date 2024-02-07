import vanna

from vanna.remote import VannaDefault
vn = VannaDefault(model='chinook', api_key='882dc42f55b44f399a6c14f1c4fdde2e')
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')
vn.ask('What are the top 10 artists by sales?')

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()