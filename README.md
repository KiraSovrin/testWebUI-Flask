# testWebUI-Flask
Python Web Application Development using Flask
Step 1: Setting Up the Development Environment
1.1 Install Python
Make sure you have Python installed on your machine. You can download it from the official Python website.

1.2 Create and Activate a Virtual Environment
Creating a virtual environment helps in managing dependencies for our project.

bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

1.3 Install Flask and Other Dependencies
With the virtual environment activated, we will install Flask and other necessary libraries.

# Install Flask
pip install Flask

# Install Flask extensions for database and user authentication
pip install Flask-SQLAlchemy Flask-Migrate Flask-Login Flask-Cors

