Regex Matching Web App Development Project

Objective:
Your task is to replicate the core functionality of the website regex101.com. This entails creating a web application that allows users to input a test string and a regular expression (regex) and displays all the matches found.

Steps:
1. Create a new directory for your project and navigate into it.

2. Set up your virtual development environment:
   - Install Flask, a Python web framework, using pip if not already installed: `pip install Flask`.

3. Initialize a new Flask application:
   - Create a new Python file named `app.py`.
   - Import Flask and create a new Flask app instance.
   - Define a route for the home page ("/") where users can input the test string and regex.
   - Render an HTML template containing a form with fields for the test string and regex, and a submit button.

4. Create the HTML template:
   - Create a new directory named `templates` within your project directory.
   - Inside the `templates` directory, create a new HTML file named `index.html`.
   - Design the HTML form with input fields for the test string and regex, and a submit button.
