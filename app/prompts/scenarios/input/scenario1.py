prompt = """
You are provided information about a new employee joining the organization. Your task is to generate a JSON body that captures all relevant details about the hired employee in a structured format from the natural language input.

<IMPORTANT>
If any field is not provided in the input or natural language query, keep its value as an empty string .
</IMPORTANT>

If any field is not provided in the input or natural language query, keep its value as an empty string "".

Input data may include: candidate name, position or title, department, start date, reporting manager, employment type (full-time, part-time, contract), location, compensation information, and any remarks from HR or management.

Below is a sample JSON body to represent the data structure:

{
  "candidate_name": "John Smith",
  "position_title": "Software Engineer",
  "department": "Technology",
  "start_date": "2025-11-10",
  "reporting_manager": "Jane Doe",
  "employment_type": "Full-time",
  "location": "New York Office",
  "compensation_details": "$80,000 per annum",
  "remarks": "John brings 5 years of experience in backend systems."
}

Generate a formatted JSON body based on the input provided, ensuring all relevant fields are included.

"""