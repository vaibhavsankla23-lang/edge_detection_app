import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Image Edge Detection App")

st.write("import an image and apply image edge filters.")

uploaded_file = st.file_uploader("choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img = np.array(image)

    #cover to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #appling filters
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    laplacian = cv2.convertScaleAbs(laplacian)

    #covert to displayable format 
    sobelx = cv2.convertScaleAbs(sobelx)
    sobelx = cv2.convertScaleAbs(sobelx)
    laplacian = cv2.convertScaleAbs(laplacian)

    #show image
    st.subheader("Original Image")
    st.image(image, width=500)

    st.subheader("Grayscale")
    st.image(gray, width=500)

    st.subheader("Sobel X (Vertical Edges)")
    st.image(sobelx, width=500)

    st.subheader("Sobel Y (Horizontal Edges)")
    st.image(sobely, width=500)

    st.subheader("Laplacian (All Edges)")
    st.image(laplacian, width=500)



































































































