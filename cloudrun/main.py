import functions_framework
from googleapiclient.discovery import build
from google.auth import default
import datetime

PROJECT_ID = "steel-bridge-466914-e0"
REGION = "us-central1"
TEMPLATE_PATH = "gs://dataflow-templates/latest/GCS_Text_to_BigQuery"
WATCHED_FILENAME = "independent_countries.csv"

@functions_framework.cloud_event
def trigger_dataflow_job(cloud_event):
    data = cloud_event.data

    file_name = data.get("name")
    bucket_name = data.get("bucket")

    if file_name != WATCHED_FILENAME:
        print(f"Ignored file: {file_name}")
        return

    job_name = f"BQDataflow-{datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"

    parameters = {
        "inputFilePattern": f"gs://{bucket_name}/{file_name}",
        "outputTable": "steel-bridge-466914-e0:countries.independent_countries",
        "JSONPath": f"gs://{bucket_name}/countriesSchema.json",
        "bigQueryLoadingTemporaryDirectory": f"gs://{bucket_name}/temp_dir/BigQueryWriteTemp/",
        "javascriptTextTransformGcsPath": f"gs://{bucket_name}/countriesUDF.js",
        "javascriptTextTransformFunctionName": "transformCSV"
    }

    credentials, _ = default()
    service = build("dataflow", "v1b3", credentials=credentials)

    template_body = {
        "jobName": job_name,
        "parameters": parameters
    }

    request = service.projects().locations().templates().launch(
        projectId=PROJECT_ID,
        location=REGION,
        gcsPath=TEMPLATE_PATH,   # Note: `gcsPath` is the correct parameter name here
        body=template_body
    )

    response = request.execute()
    print(f"Dataflow job started: {response}")
