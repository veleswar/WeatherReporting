WeatherReporting
Tools Needed:
✅ Python (for data extraction & transformation)
✅ PostgreSQL or MySQL (to store data)
✅ Apache Airflow (to automate & schedule the pipeline)

Installation Guide:
1️⃣ Install Python (if not already installed)
sudo apt update && sudo apt install python3 python3-pip -y

2️⃣ Install Required Libraries
pip install requests pandas sqlalchemy psycopg2 airflow

3️⃣ Set Up PostgreSQL Database
Install PostgreSql
sudo apt install postgresql postgresql-contrib -y
Start PostGreSql
sudo service postgresql start


🔹 Step 2: Extract Weather Data (API Call)
Use OpenWeatherMap API
1️⃣ Get a free API key from OpenWeatherMap
2️⃣ Create a Python script to extract weather data

🔹 Step 3: Transform Data (Clean & Structure)
Modify the script to clean & structure the data using pandas before storing it.

🔹 Step 4: Load Data into PostgreSQL
Modify the script to insert the transformed data into PostgreSQL.

Step 5: Automate with Apache Airflow

1️⃣ Start Apache Airflow

airflow db init

airflow standalone

2️⃣ Create an Airflow DAG (ETL Workflow)
Save this as weather_etl_dag.py in your Airflow dags folder (~/airflow/dags/)

Start Airflow scheduler & trigger DAG

Final Steps

✅ Check Airflow UI to see if the DAG runs correctly!

✅ Verify the data in PostgreSQL by running: