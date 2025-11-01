
scenario1 = """
This scenario captures the event of a new employee joining/hired in the organization. 
"""

scenario2 = """
This scenario captures the event of a new employee leaving/resigned from the organization. 
"""

prompt = f"""
You have to identify the scenario which is being discussed. The query would contain some type of indication that would align with the scenarios. 

For matching the scenarios discussed in queries, descriptions of different scenarios is given.

1. Identify the scenario type from the input text. The input may correspond to any of the defined scenarios such as:
   - scenario1(new hire): {scenario1}
   - scenario2(resignation): {scenario2}

2. Once the scenario type is identified, just return the scenario name as output. Example: "scenario1" or "scenario2"

<IMPORTANT>
IF YOU CAN NOT DETERMINE THE SCENARIO FOR THE INPUT RETURN "human" AS OUTPUT NO EXPLAIN IS NEEDED. 
</IMPORTANT>
"""