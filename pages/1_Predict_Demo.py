import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def preprocess_image(image):
    # Resize image to target size
    image = image.resize((170, 170))
    # Convert image to array
    image = np.asarray(image) / 255.0
    # Expand dimensions to match model input shape
    image = np.expand_dims(image, axis=0)
    return image

def predict(model, image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Perform prediction
    prediction = model.predict(processed_image)
    return prediction

def get_class_label(prediction):
    classes = ["COVID-19", "Normal", "Pneumonia Virus"]
    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(prediction)
    # Get the corresponding class label
    predicted_class_label = classes[predicted_class_index]
    return predicted_class_label

def main():
    st.title(":hospital: Prediksi COVID-19 dari Gambar X-ray Dada")
    st.write("Silakan unggah gambar X-ray dada untuk melakukan prediksi apakah pasien terinfeksi COVID-19 atau tidak.")
    
    sidebar_icon = ":bar_chart:"
    st.sidebar.markdown(f"## :microscope: Covid Detection")
    st.sidebar.write("Selamat datang di aplikasi deteksi COVID-19.")
    st.sidebar.write("Silakan unggah gambar X-ray dada di panel utama untuk memulai prediksi.")

    # Icon untuk upload gambar
    upload_icon = ":camera:"
    uploaded_file = st.file_uploader(f"{upload_icon} Unggah Gambar X-ray Dada", type=["jpg", "jpeg", "png"])

    # Load the trained model
    model_path = "model/chestxray.h5"  # Ganti dengan path model Anda
    model = load_model(model_path)

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar X-ray Dada', use_column_width=True)

        # Perform prediction
        prediction = predict(model, image)

        # Get the predicted class label
        predicted_class_label = get_class_label(prediction)

        # Icon untuk prediksi
        prediction_icon = ":brain:"
        # Display prediction result
        st.write(f"{prediction_icon} Prediksi: Kondisi Pasien adalah **{predicted_class_label}**.")

if __name__ == "__main__":
    main()