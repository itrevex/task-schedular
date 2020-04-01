# Google Cloud functions

## Deploying to functions

1. cd in functions folder
2. run `gcloud functions deploy function_name --runtime python37 --trigger-http`

## Testing Functions

1. visit `https://console.cloud.google.com/`
2. Under `COMPUTE` select `Cloud Functions`
3. Select the test tab and start testing by passing in the json payload
