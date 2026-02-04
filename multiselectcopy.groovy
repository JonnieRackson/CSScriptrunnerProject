import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.CustomFieldManager
import com.atlassian.jira.issue.Issue

// Define the custom field IDs
def sourceFieldName = "customfield_10001" // Replace with your source custom field 
def targetFieldName = "customfield_10002" // Replace with your target custom field ID

// Get the custom field manager
def customFieldManager = ComponentAccessor.getCustomFieldManager()

// Get the source and target custom fields
def sourceField = customFieldManager.getCustomFieldObject(sourceFieldId)
def targetField = customFieldManager.getCustomFieldObject(targetFieldId)

// Get all issues in the project 
def issueManager = ComponentAccessor.getIssueManager()
def issues = ComponentAccessor.getIssueManager().getIssueObjects()

// Iterate through the issues and copy values
issues.each { issue ->
    def sourceValues = issue.getCustomFieldValue(sourceField)

    if (sourceValues) {
        issue.setCustomFieldValue(targetField, sourceValues)
        issueManager.updateIssue(user, issue, com.atlassian.jira.event.type.EventDispatchOption.DO_NOT_DISPATCH, false)
    }
}
