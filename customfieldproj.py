import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/2/field/search"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

headers = {
    "Accept": "application/json"
}

# Define the custom field ID
custom_field_id = "customfield_XXXXX"  # Replace XXXXX with your custom field 

# Get a list of all projects
projects_url = "https://your-jira-instance/rest/api/2/project"
projects_response = requests.request(
    "GET",
    projects_url,
    headers=headers,
    auth=auth
)

if projects_response.status_code == 200:
    projects = projects_response.json()
    total_count = 0
    
    for project in projects:
        project_key = project['key']
        jql_query = f'project = {project_key} AND cf["{custom_field_id}"] is not EMPTY'
        
        # Define parameters for the API request
        params = {
            "jql": jql_query,
            "maxResults": 1000  # Adjust as needed
        }

        # Make the API request to search for issues
        project_response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth,
            params=params  # Include the params in the request
        )

        if project_response.status_code == 200:
            issues = project_response.json()['issues']
            total_count += len(issues)
        else:
            print(f"Failed to retrieve issue data for project {project_key}. Status code: {project_response.status_code}")
    
    print(f"The custom field with ID {custom_field_id} has been used in {total_count} issues across all projects.")
else:
    print(f"Failed to retrieve project data. Status code: {projects_response.status_code}")
