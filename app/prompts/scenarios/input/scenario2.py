prompt = """
You are provided information about an employee who is leaving the organization. Your task is to generate a JSON body that captures all relevant details about the employee's resignation in a structured format from the natural language input.

<IMPORTANT>
If any field is not provided in the input or natural language query, keep its value as an empty string .
</IMPORTANT>

Input data may include: employee name, current position or title, department, last working day, reporting manager, reason for resignation, handover or transition details, and any optional farewell message from HR or management.

Below is a sample JSON body to represent the data structure:

{
  "employee_name": "Sarah Taylor",
  "current_position": "Marketing Manager",
  "department": "Marketing",
  "last_working_day": "2025-11-15",
  "reporting_manager": "David Brooks",
  "reason_for_resignation": "Pursuing higher education",
  "handover_details": "Work will be transitioned to Alex Green",
  "farewell_message": "We thank Sarah for her dedication and wish her success in her future endeavors."
}

Generate a formatted JSON body based on the input provided, ensuring all relevant fields are included.

"""