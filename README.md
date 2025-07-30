# ETL Project with Data Flow, Airflow, Cloud Function and BigQuery



This repository contains code and configuration files for an ETL project that extracts data from an API — the Independent Country API, which lists all independent countries along with their capitals and languages. The data is loaded into GCS, which triggers a Dataflow job via a Cloud Function to load the data into BigQuery, and is finally visualized in Looker.


## Overview
The project aims to perform the following tasks:

Data Extraction: Extract data using python from the Independet country API and load to a GCS bucket.
Job Trigger : Once the CSV land in GCS bucket , trigger a dataflow job using a Cloud Function.
Data Loading: The Data Flow jpb loads the data into Biquery and is finally visualized in Looker.
Orchestration: Kick start the entitre flow using Apache Airflow.


## Architecture
![ETL with Data Flow](https://github.com/user-attachments/assets/e59d3d7d-230a-40b6-829c-16bd234da655)



## System Design

### Iteration 1

1. Begin by locating the data end point of independent country - use a python script to get data from this API, clean the data and load in GCS bucket as a CSV file
2. Create a data flow job to load the data into Big query
3. Create a dashboard in Looker to visulaise the data for insights

Do the above and trigger manully to test.

### Iteration 2

Create a cloud Function to trigger the dataflow job once a CSV is extracted into GCS

### Iteration 3

Create Cloud Compuser instance , setting up the groundwork for orchestarction with AirFlow
Use Airflow to kickstart the Python extract script to Load data into GCS > cloud function to trigger Dataflow job > This job to load data into BigQuery > visulaise data in Looker.


## Notes

1. Languages Field is of string type, handle this is UDF to extract and Schema with REPEATED type.
<img width="815" height="217" alt="image" src="https://github.com/user-attachments/assets/60f23fc5-8d46-4b88-8b39-7d4c7490f2db" />
2. Mention Entry point to cloud function
<img width="1073" height="216" alt="image" src="https://github.com/user-attachments/assets/83d1b32a-6b4c-44ee-a7c1-1fa8708eefb5" />


## Apendix 
1. Sample data from API [independent_countries.csv](/independent_countries.csv)
2. Python script to fetch data from API and load to GCS [extract.py](/extract.py)
3. Cloud Function to trigger Data Flow job [cloudrun.py](cloudrun)
4. Bigquery Schema [countriesSchema.json](countriesSchema.json)
5. UDF function to trasnform and handle data [countriesUDF.js](countriesUDF.js)
6. AirFlow DAG [countries_DAG.py](countries_DAG.py)











