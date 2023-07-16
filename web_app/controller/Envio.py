
from flask_mail import Mail
        
class Connertion:
    
    def __init__(self) -> None:
        pass
    
    
    def conn_email(self, app):
        email = Mail()
        email.init_app(app)
        return email
    