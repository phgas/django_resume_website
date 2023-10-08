# My Resume Website

Welcome to the GitHub repository of my personal resume website! This project is crafted with Django and initially structured on a template designed by Colorlib, which has been adeptly adjusted and simplified to cater to personal needs.

## Overview

The website is a platform where I showcase my professional journey, sharing details about my educational background, work experience, skill set, and projects. With a clean, user-friendly, and responsive design, the website aims to provide an effortless navigation experience and a comprehensive overview of my professional undertakings to potential employers, colleagues, and anyone interested in my work.

## Features

- **About**: Introduction and a brief overview of myself.
- **Resume**: A thorough section detailing my education, experience, awards and skills.
- **Projects**: Showcases a selection of my projects with descriptions and possible demo links.

## Tech Stack

- **Framework**: Django
- **Frontend**: HTML, CSS, JavaScript (Template by Colorlib)
- **Deployment**: Pythonanywhere

## Local Development

Here's a quick guide on how to run the project locally:

### Prerequisites

- Ensure that Python (3.8 or later) is installed on your system.
- Install virtualenv: `pip install virtualenv`

### Steps to Setup and Run Project

1. **Clone the Repository:**
    ```
    git clone https://github.com/YourUsername/resume-website.git
    cd resume-website
    ```
   
2. **Set Up a Virtual Environment:** (not mandatory)
    ```
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```
   
3. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```
   
4. **Apply Migrations:**
    ```
    python manage.py migrate
    ```
   
5. **Run the Development Server:**
    ```
    python manage.py runserver
    ```
   
   Open a web browser and access the application on `http://localhost:8000/`

## Deployment

- For details about deployment steps see: [Here](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- Link to the live website: [Here](https://phgas.pythonanywhere.com/)

## Acknowledgements

- [Colorlib](https://colorlib.com/wp/template/ronaldo/) for providing the initial template.