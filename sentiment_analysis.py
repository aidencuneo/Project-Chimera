import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.utils import pad_sequences
from keras import Sequential
from keras._tf_keras.keras.utils import to_categorical, pad_sequences
from keras._tf_keras.keras.layers import Dense, SimpleRNN, Embedding, Flatten


def sentiment_to_int(sentiment):
    return {'positive': 0, 'negative': 1}.get(sentiment, 2)


def predict_sentiment(text):
    new_text_seq = tokenizer.texts_to_sequences([text])
    new_text_padded = pad_sequences(new_text_seq, padding='post', maxlen=35) # Use the max_len determined during training
    predictions = model.predict(new_text_padded)
    predicted_class_index = predictions.argmax(axis=-1)

    if predicted_class_index[0] == 0:
        return 'Postive Sentiment'
    elif predicted_class_index[0] == 1:
        return 'Negative Sentiment'
    else:
        return 'Neutral Sentiment'


train_ds = pd.read_csv('sentiment-analysis-dataset/train.csv', encoding='latin1')
validation_ds = pd.read_csv('sentiment-analysis-dataset/test.csv', encoding='latin1')
train_ds = train_ds[['text', 'sentiment']]
validation_ds = validation_ds[['text', 'sentiment']]
train_ds['text'].fillna('', inplace=True)
validation_ds['text'].fillna('', inplace=True)

train_ds['sentiment'] = train_ds['sentiment'].apply(sentiment_to_int)
validation_ds['sentiment'] = validation_ds['sentiment'].apply(sentiment_to_int)

x_train = np.array(train_ds['text'].tolist())
y_train = np.array(train_ds['sentiment'].tolist())
x_test = np.array(validation_ds['text'].tolist())
y_test = np.array(validation_ds['sentiment'].tolist())

y_train = to_categorical(y_train, 3)
y_test = to_categorical(y_test, 3)

tokenizer = Tokenizer(num_words=20000)
tokenizer.fit_on_texts(x_train)
tokenizer.fit_on_texts(x_test)

x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

x_train = pad_sequences(x_train, padding='post', maxlen=35) # Set maxlen to 35
x_test = pad_sequences(x_test, padding='post', maxlen=35)  

model = Sequential()

model.add(Embedding(input_dim=20000, output_dim=5, input_length=35))
model.add(SimpleRNN(32, return_sequences=False))
model.add(Dense(3, activation='softmax'))

if os.path.exists('sentiment_model.weights.h5'):
    model.load_weights('sentiment_model.weights.h5', skip_mismatch=True)
else:
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.save_weights('sentiment_model.weights.h5')

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()

# Positive
print(predict_sentiment('The movie was great, would recommend'))

# Negative
print(predict_sentiment('The movie sucked, would not recommend'))

# Neutral
print(predict_sentiment('Hey, how are you?'))
