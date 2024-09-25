import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Define a function to call the fine-tuned model
def get_summary_from_finetuned_model(prompt):
    response = openai.Completion.create(
        model="davinci:ft-your-finetuned-model-id",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['text']

# Example police report input
police_report_prompt = """Case No: 2024-12345
Date: September 15, 2024
Location: 123 Main St, New York, NY
Officer: John Doe, Badge No. 56789
Type of Incident: Vehicle Collision
Injuries: John Smith (minor neck injury)
Narrative: A collision occurred between a black sedan and a white SUV at 8:30 AM.
Summary:"""

# Get the summary from the fine-tuned model
summary = get_summary_from_finetuned_model(police_report_prompt)

print("Generated Summary:")
print(summary)
