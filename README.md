This is a simple Flask web application that performs image compression using Singular Value Decomposition (SVD). Users can upload an image and specify the compression level, and the app will show a side-by-side comparison of the original and compressed images.

Features:-
Upload an image.
Choose the compression level.
Display original vs. compressed image side by side.
Works locally using Flask.

Prerequisites:-
Ensure you have the following installed:
Python 3.x
Pip (Python package installer)
Getting Started
Follow these steps to get the Flask app up and running locally.

1. Clone the Repository
First, clone the repository to your local machine:

bash
git clone https://github.com/your-username/flask-image-compression-app.git
cd flask-image-compression-app
2. Set Up the Virtual Environment (Optional)
It’s a good idea to create a virtual environment to isolate your dependencies. Run the following commands:

bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Install the required Python packages listed in the requirements.txt file:

bash

pip install -r requirements.txt
This will install:
Flask
NumPy
Pillow (PIL for image processing)
Matplotlib

4. Running the App
Now, you’re ready to run the Flask app:

bash
python app.py

After running the command, the app will be available at http://127.0.0.1:5000/. Open this URL in your web browser.

5. Using the Web App

Navigate to the homepage at http://127.0.0.1:5000/.
Upload an image and specify the compression level (k value).
Click the "Compress Image" button.
After processing, you'll be taken to a page showing the original and compressed images side by side.

7. Project Structure
Here’s a quick overview of the project structure:

flask-image-compression-app/
│
├── app.py                  # Main Flask app file
├── requirements.txt        # Project dependencies
├── static/
│   ├── uploads/            # Folder for uploaded images
│   └── downloads/          # Folder for compressed images
├── templates/
│   ├── index.html          # HTML file for image upload
│   └── comparison.html     # HTML file for image comparison
└── README.md               # This readme file

7. How It Works
The app uses Singular Value Decomposition (SVD) to compress images. Based on the value of k provided by the user, the app reduces the image’s rank while maintaining as much visual information as possible.
The app.py file defines two main routes:
/: Renders the image upload form (index.html).
/compress: Handles the image compression and renders the comparison page (comparison.html).

9. License
This project is licensed under the MIT License - see the LICENSE file for details.
