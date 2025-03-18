from openai import OpenAI
import openai  # Ensure you import this

# Set up OpenAI API Key (Make sure you have this as an environment variable in Render)
client = openai.ChatCompletion  # Correct way to call the OpenAI API

# Function to generate lesson plans
def generate_lesson(topic, year_group, objectives, spatial_focus, duration):
    prompt = f"""
    Generate a structured lesson plan for a {year_group} class on {topic}.
    - Duration: {duration}
    - Learning Objectives: {objectives}
    - Spatial Thinking Strategies: {spatial_focus}

    The lesson plan should include:
    1. **Introduction**: Context and spatial reasoning introduction.
    2. **Main Activity**: Engaging activities using {spatial_focus}.
    3. **Teacher Role**: How to use gestures, boardwork (bansho), or dynamic tools.
    4. **Student Engagement**: Ways to encourage spatial reasoning.
    5. **Assessment**: Evaluating students’ use of spatial thinking.
    6. **Extensions**: Further activities, digital tools, or real-world applications.

    Structure the response in a clear, readable format.
    """

    response = client.create(
        model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
        messages=[{"role": "system", "content": "You are an expert in maths education."},
                  {"role": "user", "content": prompt}],
        max_tokens=500
    )

    return response["choices"][0]["message"]["content"].strip()
