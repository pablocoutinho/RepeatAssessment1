# RepeatAssessment1

Django CRUD Web Application

This is a simple full stack web application built using Django, which allows for performing CRUD (Create, Read, Update, Delete) operations on a list of products. It demonstrates the use of Django as a Python web framework, the connection to an external MySQL database, and serving a front-end application using Python.

Functionality

The web application provides the following functionality:

Display a list of products with their names, descriptions, and prices.
View the details of each individual product.
Create new products with a name, description, and price.
Update the details of existing products.
Delete products from the list.
Setup

To run the application locally, please follow these steps:

Install Django by running pip install django in your command prompt or terminal.
Clone this repository using git clone.
Change into the project directory by running cd mywebapp.
Create a virtual environment by running python -m venv .venv. Activate the virtual environment by running .venv\Scripts\activate (for Windows) or source .venv/bin/activate (for macOS/Linux).
Install the project dependencies by running pip install -r requirements.txt.
Create a MySQL database and update the DATABASES configuration in settings.py with your database credentials.
Run database migrations by running python manage.py migrate.
Start the development server by running python manage.py runserver.
Open http://localhost:8000 in your browser to access the web application.
Limitations

This application focuses on the core functionality of CRUD operations and does not incorporate complex features such as user authentication or authorization.
The front-end templates are minimalistic and can be further improved to enhance the overall user experience.
Error handling and validation could be extended to provide more user-friendly feedback in case of erroneous input or actions.
Currently, the application is served on the Django development server. To deploy it on a web server, additional configuration and setup would be required.
Future Improvements

Implement user authentication and authorization to allow secure access and management of products by authenticated users.
Enhance the front-end with better styling and responsiveness to create a more visually appealing and user-friendly interface.
Implement search and filtering functionality to allow users to find specific products based on certain criteria.
Incorporate pagination to handle large datasets more efficiently and improve performance.
Expand the unit tests to cover additional scenarios and ensure the integrity of the application.
