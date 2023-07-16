from model.email import EnvioGmail, Email
from flask import  Flask, flash, render_template, redirect, request, send_from_directory
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xeAc]/'

email = Mail() #class inisializadora
config = EnvioGmail() #class inisializadora

app.config.update(config.config_server())
email.init_app(app)

# Parar que ocorre erro no favicon.ico
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    error = None
    if request.method == 'POST':
        form_contato = Email(request.form['nome'], 
                             request.form['email'], 
                             request.form['mensagem']
                            )
            
        msg = Message(subject= f'{form_contato._nome} enviou um mendagem no portfólio',
                    sender= app.config.get("MAIL_USERNAME"),
                    recipients= ['daniel.marinho.ferreira.souza@gmail.com', app.config.get("MAIL_USERNAME")],
                    body = f'''{form_contato._nome} com E-mail {form_contato._email}, Enviou a seguinte mensagem:
                                {form_contato._text}
                            '''
                    )
    email.send(msg)
    flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)