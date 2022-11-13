import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

###
# deep classifier project
###
model = tf.keras.models.load_model("model.h5")
upload_file = st.file_uploader("choose a file")
if upload_file is not None:
    
    img = Image.open(upload_file)
    img = img.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array,axis=0) # [batch_size, row,col,channel]
    result = model.predict(img_array)
    argmax_index = np.argmax(result,axis=1)
    if argmax_index[0] == 0:
        st.image(image,caption="predicted: cat")
    else:
        st.image(image,caption="predicted: dog")
