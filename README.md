# Automation Project

The aim of this project is to implement automation testing for few API's collection related to Rijksmuseum.

P.S: Few tests (MARKED AS SKIPPED) are failing because of an unexpected behaviour, the response is seen 200 even there is a typo with parameter names in the request.

# Technologies and Languages

- Python: The project is written in Python, a programming language known for its simplicity and readability.

- Pytest: Pytest is used as the testing framework, providing a robust set of features for writing and running tests with ease.

- IntelliJ IDEA: The project can be run locally using IntelliJ IDEA, a popular integrated development environment (IDE) that offers advanced features for Python development and debugging.

- GitHub Actions: The CI/CD pipeline is set up using GitHub Actions, automating the build, test, and deployment processes directly from your GitHub repository.

# Directories and Files

This project contains:

	- config directory: this directory contains the environment config class.

    - results directory: in this directory the reports (html and xml) are generated.

    - src directory: this directory contains the classes responsible for interacting with the Rijksmuseum API to retrieve data.

    - tests directory: this directory contains the classes where API Test functions are created.

    - .github/workflows directory: this directory contains this file includes the Pipeline that defines a series of steps that are executed in a specific order to automate a software development process.

# Getting started

To download and install pytest, run this command from the terminal : pip install pytest

To download and install requests, run this command from the terminal : pip install requests

To ensure all dependencies are resolved in a CI environment, in one go, add them to a requirements.txt file.

Then run the following command : pip install -r requirements.txt

# Running Tests

Tests are contained inside a folder 'Tests', then run the following command : pytest

To generate xml results, run the following command : pytest --junitxml="results/result.xml"

To generate html  results, run the following command : pytest -v --html=results/report.html

# Pipeline YAML Script

This pipeline is created to automate the testing and deployment process for the project. 

The pipeline is triggered automatically on pushes to the main branch, ensuring that code changes are thoroughly tested before deployment.

## How it Works
The pipeline consists of the following steps:

- Checkout code: Fetches the latest code from the repository.
- Set up Python: Configures the Python environment for running tests.
- Install dependencies: Installs project dependencies specified in requirements.txt.
- Run tests: Executes automated tests using pytest and generates test reports.
- Upload test reports: Uploads test reports to the GitHub Actions artifacts for easy access.
- Build and deploy: Executes deployment steps to the target environment (e.g., staging or production).

## Usage

To contribute to the project or modify the pipeline:

- Make changes to the pipeline YAML (pipeline.yml) or other project files.
- Submit a pull request to propose your changes.
- Monitoring : Monitor the pipeline's execution and status through the GitHub Actions dashboard. View logs, check for errors, and track job progress.
- After a pipeline run is completed, you can find the generated test reports in the Artifacts section of the GitHub Actions interface.