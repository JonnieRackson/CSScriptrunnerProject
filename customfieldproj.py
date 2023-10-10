import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/2/field/search"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

# Define the custom field ID
custom_field_id = "customfield_XXXXX"  # Replace XXXXX with your custom field ID

# Get a list of all projects
response = requests.get(f"{url}/project", headers={"Authorization": f"Basic {api_token}"})

if response.status_code == 200:
    projects = response.json()
    
    # Initialize a counter for field usage
    total_usage_count = 0
    
    # Initialize a dictionary to store project usage counts
    project_usage_counts = {}
    
    # For each project, count how many times the custom field has been used
    for project in projects:
        project_key = project['key']
        
        # Define the JQL query to search for issues with the custom field in the specific project
        jql_query = f'cf[{custom_field_id}] is not EMPTY AND project = {project_key}'
        
        # Define parameters for the API request
        params = {
            "jql": jql_query,
            "maxResults": 1000  # Adjust as needed
        }
        
        # Make the API request to search for issues
        response = requests.get(f"{url}/search", params=params, headers={"Authorization": f"Basic {api_token}"})
        
        if response.status_code == 200:
            issues = response.json()['issues']
            field_usage_count = len(issues)
            total_usage_count += field_usage_count
            project_usage_counts[project_key] = field_usage_count
        else:
            print(f"Failed to retrieve issue data for project {project_key}. Status code: {response.status_code}")
    
    # Generate a report
    print(f"\nTotal field usage across all projects: {total_usage_count}\n")
    print("Project Usage Report:")
    for project_key, usage_count in project_usage_counts.items():
        print(f"Project {project_key}: {usage_count} usage(s)")
else:
    print(f"Failed to retrieve project data. Status code: {response.status_code}")
