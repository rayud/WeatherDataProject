# WeatherDataProject

WeatherDataProject is a Django API application which extracted  weather data from various files.

## Features

- **Data Collection**: Collects weather data from multiple files.
- **Data Storage**: Stores weather data in a structured format.

- **API**: Offers an API for accessing weather data  programmatically.


## Python Version
WeatherDataProject is developed using Python 3.12.4

## Data Ingestion Job: 

We have different weather data files stored in the folder: /WeatherDataProject/wx_data

### How to run Data Ingestion Job: 

```bash
cd WeatherDataProject\wx_data
python ETL_Job.PY
```
The Above will use the pandas library to perform data analysis on the data from different files and store the data in Database

It won't create duplicates, If you run the ETL run more than once. It usese atomic transaction and bulk create in Django ORM. 



## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rayud/WeatherDataProject.git
   cd WeatherDataProject
   ```

2. **Setup Environment**

   It's recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**

   Open your web browser and go to `http://localhost:8000`.

## Usage

- **Admin Panel**: Use Django admin interface at `http://localhost:8000/admin/` to manage weather data.
- **API Documentation**: Explore API endpoints and documentation at `http://localhost:8000/swagger/`.