from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI  # If using OpenAI API

# Create FastAPI app
app = FastAPI()

# OpenAI API Key (Replace with your own API key)
OPENAI_API_KEY = "your-api-key"
client = OpenAI(api_key=OPENAI_API_KEY)

# Define request model
class LessonRequest(BaseModel):
    topic: str
    year_group: str
    objectives: str
    spatial_focus: str
    duration: str

# Function to generate lesson plans using AI
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

    response = client.Completion.create(
        model="gpt-4",  # Use "gpt-4" or change to an open-source model if needed
        prompt=prompt,
        max_tokens=500
    )

    return response["choices"][0]["text"].strip()

# API endpoint to generate a lesson plan
@app.post("/generate_lesson")
async def create_lesson(request: LessonRequest):
    lesson_plan = generate_lesson(
        request.topic, request.year_group, request.objectives, request.spatial_focus, request.duration
    )
    return {"lesson_plan": lesson_plan}
