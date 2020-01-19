# -*- coding: utf-8 -*-
"""Copy of Apexio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gHfA3vScO_ZdhSZErH3AXmHq011DM8Pr

extensions to edit: .pdf, .txt, .docx
"""

# Commented out IPython magic to ensure Python compatibility.
# import stuff
# %load_ext autoreload
# %autoreload 2
# %matplotlib inline

import numpy as np
import random as rand
import os, re, json, nltk, argparse, random, torch, pickle
import tensorflow as tf
import tensorflow_hub as hub
from random import randint
from tensorflow.keras.layers import Input, Dense, Add, Dropout, Concatenate
from tensorflow.keras.models import Model
from models import Infersent

nltk.download('punkt')

# This is the big file so run this once to download to your drive
#!mkdir 'drive/My Drive/ApexioData/GloVe'
#!curl -Lo 'drive/My Drive/ApexioData/GloVe/glove.840B.300d.zip' http://nlp.stanford.edu/data/glove.840B.300d.zip
#!unzip 'drive/My Drive/ApexioData/GloVe/glove.840B.300d.zip' -d 'drive/My Drive/ApexioData/GloVe/'

# Run every time to download on the colab runtime
#!mkdir encoder
#!curl -Lo encoder/infersent1.pkl https://dl.fbaipublicfiles.com/infersent/infersent1.pkl

# Load model

model_version = 1
MODEL_PATH = "encoder/infersent%s.pkl" % model_version
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': model_version}
model = InferSent(params_model)
model.load_state_dict(torch.load(MODEL_PATH))

model = model.cuda()

W2V_PATH = 'drive/My Drive/ApexioData/GloVe/glove.840B.300d.txt'
model.set_w2v_path(W2V_PATH)

model.build_vocab_k_words(K=100000)

def get_doc2vec(text):
  sents = nltk.sent_tokenize(text)
  emb = model.encode(sents)
  sum = None
  for e in emb:
    if sum is None:
      sum = e
    else:
      sum += e
  return sum / len(sents)

def generate_pairs(dat):
  pairs = []
  for i in range(len(dat)):
    for j in range(i+1,len(dat)):
      pairs.append((dat[i],dat[j]))
  return pairs

def generate_X_y_from_pairs(pairs):
  X = [[],[]]
  y = []
  for pair in pairs:
    X[0].append(pair[0][3])
    X[1].append(pair[1][3])
    y.append(1.0 if pair[0][4] == pair[1][4] else 0)
  return [np.array(x) for x in X], np.array(y)

def generate_X_y_from_dat(dat):
  X = [[],[]]
  y = []
  for i in range(len(dat)):
    for j in range(i+1,len(dat)):
      X[0].append(dat[i][3])
      X[1].append(dat[j][3])
      y.append(1.0 if dat[i][4] == dat[j][4] else 0)
  return [np.array(x) for x in X], np.array(y)

def get_dirs(path):
  dirs = []
  for r, d, f in os.walk(path):
    if len(d) != 0:
      dirs += d
  return dirs

def get_files(path, dirs):
  tarr = []
  vecs = []
  for i in range(len(dirs)):
    dir = dirs[i]
    print(dir)
    files = grab_files(path+dir+'/')
    for f in files:
      r = f.split(r'/'+dir+'/')[1]
      ext = r.split(r'.')[1]
      try:
        extr = extract(f)
        vecs.append(get_doc2vec(extr))
        tarr.append([r, ext, extr, vecs[-1],dir])
      except:
        print(f'File {r} not readable')
  return tarr

def generate_quads(names, contents, dirs):
    tarr = []
    for i in range(len(names)):
        ext = names[i].split(r'.')[1]
        try:
          vecs.append(get_doc2vec(contents[i]))
          tarr.append([names[i], ext, contents[i], vecs[-1],dirs[i]])
        except:
          print(f'File {r} not readable')
    return tarr

def main():
    parser = argparse.ArgumentParser(description='Apexio Data Organization Model')
    fname, content, and parent directory
    parser.add_argument('-n', dest='data_fname', required=True, help='List of file names')
    parser.add_argument('-c', dest='data_content', required=True, help='List of file contents')
    parser.add_argument('-d', dest='data_dir', required=True, help='List of file directory')
    args = parser.parse_args()
    quads = generate_quads(args.data_fname, args.data_content, args.data_dir)
    # PUT UR ARGS INTO GENERATE_QUADS
    rand.shuffle(pairs)
    train_pairs = pairs[:int(len(pairs) * 0.8)]
    test_pairs = pairs[int(len(pairs) * 0.8):]
    X_train, y_train = generate_X_y_from_pairs(train_pairs)
    X_test, y_test = generate_X_y_from_pairs(test_pairs)
    X_whole, X_whole = generate_X_y_from_pairs(pairs)
    whole_pairs = pairs

    input_1 = Input((4096,), dtype=tf.float32)
    input_2 = Input((4096,), dtype=tf.float32)
    reduce_dim_1 = Dense(1000, activation='relu')
    con = Concatenate()([reduce_dim_1(input_1),reduce_dim_1(input_2)])
    x_1 = Dense(1000, activation='relu')(con)
    x_2 = Dense(500, activation='relu')(x_1)
    x_3 = Dense(100, activation='relu')(x_2)
    x_4 = Dense(25, activation='relu')(x_3)
    out = Dense(1, activation='sigmoid')(x_4)
    dual_model = Model(inputs=[input_1, input_2], outputs=out)
    dual_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    dual_model.fit(X_train, y_train, epochs=10)
    dual_model.save('Model.pickle')
