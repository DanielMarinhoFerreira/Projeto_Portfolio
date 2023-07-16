from dotenv import load_dotenv
import os



class Email:
    """Classe dos E-mail de Envio pelo Portifolio"""
    def __init__(self, nome:str, email:str, text:str) -> None:
        self._nome = nome
        self._email = email
        self._text = text
        
        
    def get_nome(self):
        return self.get_nome()
    
    def get_email(self):
        return self.get_email()
    
    def get_text(self):
        return self.get_text()
    
    
class EnvioGmail():
    """Classe para enviar emails"""
    load_dotenv() 
    
    def __init__(self) -> None:
        #credenciais do gmail
        self.email = os.getenv("EMAIL") 
        self.password = os.getenv("SENHA")
        self.server:str = 'smtp.gmail.com'
        self.port:int = 587
        self.tls:bool = True
        #self.ssl:bool = True
        
    def get_email(self):
        return self.email
    
    def get_server(self):
        return self.server
    
    def get_port(self):
        return self.port
    
    def get_tls(self):
        return self.tls
    
    def get_ssl(self):
        return self.ssl
    
    def get_password(self):
        return self.password
    
    def config_server(self):
        return {"MAIL_SERVER": self.get_server(),
                "MAIL_PORT": self.get_port(),
                "MAIL_USE_TLS": self.get_tls(),
                #"MAIL_USE_SSL": self.get_ssl(),
                "MAIL_USERNAME": self.get_email(),
                "MAIL_PASSWORD": self.get_password()
                }