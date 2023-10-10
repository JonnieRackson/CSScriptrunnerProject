import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/2/field/search"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

# Define custom field ID
custom_field_id = "customfield_XXXXX"  # Replace XXXXX with your custom field ID

# Define the JQL query to search for issues with non-empty custom fields
jql_query = f'cf[{custom_field_id}] is not EMPTY'

# Define parameters for the API request
params = {
    "jql": jql_query,
    "maxResults": 1000
}

# Make the API request to search for issues
response = requests.get(url, params=params, headers={"Authorization": f"Basic {api_token}"})

if response.status_code == 200:
    issues = response.json()['issues']
    total_count = len(issues)
    print(f"The custom field with ID {custom_field_id} has been used in {total_count} non-empty issues.")
else:
    print(f"Failed to retrieve issue data. Status code: {response.status_code}")