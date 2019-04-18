# Mapping National Parks in the US

Name

[Link to this repository](https://github.com/ruthwanglusi/SI507_final)

---

## Project Description

This project visualizes the US national parks’ location on a  choropleth map in web browser using Flask. The project will allow users to see the density of national parks in 51 states of the US. Click on the map to access a full list of national parks at the clicked state (also accessible by directly type in URLs). Update the density choropleth map as user filter through various park types.

Data Source: www.nps.gov

## How to run

1. pip install required modules from requirements.txt
2. run SI507project_tool_database

## How to use

1. Open a browser, go to address http://localhost:5000/
2. Click on the state name on the choropleth US map to see all the parks in that state
3. Return to the home page, click on one park type to see an updated choropleth US map.

## Routes in this application
- `/home` -> The overall national park density among all the US states visualized as a choropleth map.
- `/state/(state name)` -> A list of all the national parks in a specific state.
- `/type/(park type)` -> The density of a specific park type across all US states as a choropleth map.

## How to run tests
1. Find the test file SI507project_test.py
2. Run the test file

## In this repository:
- Image
  - ERD_diagram.png
- File name
- SI507project_tool_scrape.py
- SI507project_tool_app.py
- SI507SI507project_tool_db.py
- SI507project_test.py
- README.md

## Database diagram:
![](image/ERD_diagram.png)

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [X] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [X] Project includes at least 1 test suite file with reasonable tests in it.
- [X] Includes a `requirements.txt` file containing all required modules to run program
- [X] Includes a clear and readable README.md that follows this template
- [X] Includes a sample .sqlite/.db file
- [X] Includes a diagram of your database schema
- [X] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [X] Interactions with a database that has at least 2 tables
- [X] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [X] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [X] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
