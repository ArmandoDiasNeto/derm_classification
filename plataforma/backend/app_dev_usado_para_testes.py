from flask import Flask, request, jsonify
from flask_cors import CORS


from PIL import Image
import  numpy as np
import os 
import tensorflow
#from tensorflow.keras.models import load_model
#import tensorflow as tf

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo vazio'}), 400

    # Aqui você pode salvar ou processar o arquivo conforme necessário.
    # Neste exemplo, apenas retornamos uma mensagem.

    print("Imagem carregada")
    
    return jsonify({'message': 'Obrigado pela imagem'})

if __name__ == '__main__':
    app.run(debug=True)
