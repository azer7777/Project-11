# Project-11

# Güdlft

Güdlft is a web application of concept (POC) project to show a light-weight version of a competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.


## Installation

1. Clone the repository:
````
git clone https://github.com/azer7777/Project-11.git
````
2. Create a virtual environment and activate it:
````
python3 -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3. Install dependencies:
````
pip install -r requirements.txt
````
4. Start the development server:
````
$env:FLASK_APP = "server.py"
flask run
````
5. Access the application at `http://127.0.0.1:5000/

## Tests and reports

1. Running Tests with pytest:
````
pytest
````
To generate an HTML report:
````
pytest --html=pytest_report.html
````
2. Generating Load Tests with Locust:
````
locust -f locustfile.py
````
Access the Locust web interface at http://localhost:8089 to configure and start the load test.

3. Generating Code Coverage Report:
````
coverage run -m pytest
````
Generate the coverage report:
````
coverage html
````
Access the HTML coverage report in the htmlcov directory.

