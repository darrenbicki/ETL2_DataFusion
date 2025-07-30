import requests
import csv
import io
from google.cloud import storage

# API endpoint
url = "https://restcountries.com/v3.1/independent?status=true&fields=languages,capital,name"

from google.cloud import storage

storage_client = storage.Client(project='steel-bridge-466914-e0')
bucket = storage_client.bucket('bkt_countries')
# proceed with upload



# GCS bucket and file name
BUCKET_NAME = "bkt_countries"
DESTINATION_BLOB_NAME = "independent_countries.csv"

# Step 1: Fetch data
response = requests.get(url)
response.raise_for_status()
countries = response.json()

# Step 2: Write CSV to in-memory string buffer
output = io.StringIO()
fieldnames = ["country_name", "capital", "languages"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()

for country in countries:
    name = country.get("name", {}).get("common", "Unknown")
    capital = "| ".join(country.get("capital", [])) if "capital" in country else "N/A"
    languages = "| ".join(country.get("languages", {}).values()) if "languages" in country else "N/A"
    writer.writerow({
        "country_name": name,
        "capital": capital,
        "languages": languages
    })

# Step 3: Upload CSV string to GCS
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)
blob = bucket.blob(DESTINATION_BLOB_NAME)

blob.upload_from_string(output.getvalue(), content_type="text/csv")

print(f"✅ CSV uploaded to gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}")
