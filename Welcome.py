import streamlit as st

def main():
    st.snow()
    st.title("Deteksi COVID-19 dari X-ray Dada menggunakan CNN")
    st.write("Proyek ini bertujuan untuk mengembangkan model Convolutional Neural Network (CNN) dari awal untuk mendeteksi adanya COVID-19 dari gambar X-ray dada.")
    
    st.header("Business Understanding")
    st.subheader("Problem Statements :thinking:")
    st.write("Diberikan kumpulan gambar X-ray dada pasien yang terinfeksi COVID-19 dan sehat. Tujuan proyek ini adalah untuk mengembangkan model yang dapat membedakan antara gambar X-ray dada pasien yang terinfeksi COVID-19 dan yang sehat.")

    st.subheader("Goals :dart:")
    st.write("- Mengembangkan model CNN dari awal untuk deteksi COVID-19 dari gambar X-ray dada.")
    st.write("- Membuat aplikasi yang dapat digunakan untuk memprediksi apakah seseorang terinfeksi COVID-19 atau tidak berdasarkan X-ray dada.")

    st.subheader("Solution Statements :computer:")
    st.write("Berdasarkan problem statements yang ada, saya akan mengimplementasikan model CNN dari awal menggunakan TensorFlow atau PyTorch. Setelah model terlatih, saya akan membuat aplikasi web menggunakan Streamlit untuk memprediksi apakah seseorang terinfeksi COVID-19 atau tidak berdasarkan gambar X-ray dada yang diunggah.")

    st.write("Untuk menjalankan aplikasi, Anda dapat melihat sidebar di sebelah kiri. Di sana, Anda akan menemukan kolom untuk mengunggah gambar X-ray dada, dan aplikasi akan memprediksi apakah pasien terinfeksi COVID-19 atau tidak.")

if __name__ == "__main__":
    main()
