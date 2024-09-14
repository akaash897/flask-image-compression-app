from flask import Flask, render_template, request, send_file
import os
import numpy as np
from PIL import Image

app = Flask(__name__)

# Define the upload and download folder paths
UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Function to apply SVD compression on the image
def compress_image(path, k):
    img = Image.open(path)
    img_array = np.array(img)
    R, G, B = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]

    def compress_channel(channel, k):
        U, S, Vt = np.linalg.svd(channel, full_matrices=False)
        return np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

    R_compressed = compress_channel(R, k)
    G_compressed = compress_channel(G, k)
    B_compressed = compress_channel(B, k)

    compressed_img = np.stack((R_compressed, G_compressed, B_compressed), axis=2)
    compressed_img = np.clip(compressed_img, 0, 255).astype(np.uint8)

    compressed_path = os.path.join(DOWNLOAD_FOLDER, 'compressed.jpg')
    Image.fromarray(compressed_img).save(compressed_path)
    return compressed_path

# Main route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and compression
@app.route('/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Perform SVD compression
    k = int(request.form.get('k_value', 50))  # Get the value of k from the form
    compressed_path = compress_image(file_path, k)

    # Pass the file paths to the HTML for displaying
    return render_template('comparison.html', original_image=file.filename, compressed_image='compressed.jpg')

if __name__ == '__main__':
    app.run(debug=True)
