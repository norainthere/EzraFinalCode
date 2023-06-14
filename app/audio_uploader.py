import os
import audiofile
import streamlit as st

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac', 'm4a', 'aac'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(upload_folder, uploaded_file):
    try:
        with open(os.path.join(upload_folder, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        print(e)
        return False

st.title('Upload new Audio File')
uploaded_file = st.file_uploader("Choose an audio file", type=ALLOWED_EXTENSIONS)

if uploaded_file is not None:
    if allowed_file(uploaded_file.name):
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        if save_uploaded_file(UPLOAD_FOLDER, uploaded_file):
            st.success("File {} has been uploaded successfully".format(uploaded_file.name))
            # Read the uploaded audio file
            signal, sampling_rate = audiofile.read(os.path.join(UPLOAD_FOLDER, uploaded_file.name))
            # TODO: Pass the signal to the AI model for analysis
        else:
            st.error("Failed to save file.")
    else:
        st.error("This file extension is not allowed. Please upload a valid audio file.")
