import streamlit as st
from functions import load_trained_model, preprocess_image, predict_gesture

# Filepath for the trained model
MODEL_PATH = r"D:\gesture_recognition_project\best_model.keras"

# Load the model
st.title("Gesture Recognition App")
st.sidebar.title("Options")
st.sidebar.write("Upload an image to predict the gesture.")

model = load_trained_model(MODEL_PATH)
if model is None:
    st.error("Model could not be loaded. Please check the file path.")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with st.spinner("Processing image..."):
        # Save the uploaded file temporarily
        temp_file_path = f"temp_image.{uploaded_file.name.split('.')[-1]}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Preprocess the image
        preprocessed_image = preprocess_image(temp_file_path)
        if preprocessed_image is None:
            st.error("Error in preprocessing the image.")
        else:
            # Predict the gesture
            prediction = predict_gesture(model, preprocessed_image)
            if prediction is not None:
                st.success(f"Predicted Gesture: {chr(prediction+65)}")
            else:
                st.error("Error in predicting the gesture.")
