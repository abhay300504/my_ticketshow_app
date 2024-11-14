# Starting of the app
from flask import Flask
from backend.models import db

app=None   #app name

def setup_app():    #create instance of the app, #1 step function is performing initial setup, #2 create flask object, #3 connecting sqlite, #4 allowing your appilication to interact with other module, #5 debugging development environment is on
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///ticket_show.sqlite3" # Having db file
    db.init_app(app)  #flask app connect to db, #Pending here is sqlite connection 
    app.app_context().push() # Direct access to other modules
    app.debug=True
    print("Ticket Show app is started...")

#Call the setup
setup_app()

from backend.controllers import *    #import controller from controller.py

if __name__=="__main__":    #name static
    app.run(debug=True)



#Many controllers/routers here