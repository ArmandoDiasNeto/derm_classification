from flask import Flask
from flask import jsonify
from flask import request
from PIL import Image
import  numpy as np
import os 
#from tensorflow.keras.models import load_model
#import tensorflow as tf
from flask_cors import CORS

home_path = os.path.dirname(os.path.realpath(__file__))
model_dir=os.path.join(home_path, 'models', 'fitzpatrick_ddi_pad_v1')
print('model_dir ', model_dir)

m_ckpt = os.path.join(model_dir, 'model_checkpoint')
#model = load_model(m_ckpt, options=tf.saved_model.LoadOptions(allow_partial_checkpoint=True))

IMG_SHAPE=(512, 512)

class_names = ['carcinoma','nao-carcinoma']

app = Flask(__name__)
CORS(app) 


def predict_model(img_arr):
    pass

@app.route('/', methods=['GET', 'POST'])
def main():

    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    print("Imagem carregada")

    img = Image.open(file.stream)
    img_arr = np.asarray(img)
    print(img_arr.shape)

    #image_resize = tf.image.resize(img_arr, IMG_SHAPE)
    #print(image_resize.shape)


    #img_batch = np.expand_dims(image_resize, axis=0)
    #img = img_batch[:, :, :,:3]
    #scores = model.predict(img)
    #print('scores ', scores)

    #max_score = np.max(scores)
    #pred_class = [class_names[np.argmax(s)] for s in scores][0]

    #log =  zip(class_names, scores[0])
    #print(dict(log))
    
    #return jsonify({'pred': str(pred_class), 'score':str(max_score), })

    # Exemplificando um predicao da classe "nao-carcinoma"
    pred_class = "nao-caricinoma"
    max_score = 93.07


    # Trativa para caso a imagem seja nao-carcinoma:
    if pred_class == "caricinoma":
        return jsonify({'message': f'The skin lesion detected has a {max_score} of score to be a {pred_class} category lesion. It is recommended to evaluate with a doctor.'})
    else:
        # Prevendo a categoria com o modelo II:
        #scores = model.predict(img)
        #print('scores ', scores)

        #max_score = np.max(scores)
        #pred_class_II = [class_names[np.argmax(s)] for s in scores][0]

        # Exemplificando um predicao da classe "nao-carcinoma" e classe "psoriasis"
        max_score = 89.14
        pred_class_II = "psoriasis"

        return jsonify({'message': f'The lesion is not a carcinoma and betwen the non-carciona lesions, it has big probably to be {pred_class_II} with score of {max_score}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
