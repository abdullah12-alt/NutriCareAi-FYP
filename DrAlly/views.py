from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
# previous :  AIzaSyAc4KcQ_0aOrnWF2cj-YqV6ofSCZxEmZlI
# Configure the generative AI model
genai.configure(api_key="AIzaSyDlw1juQQ2mjuePMYfZkgKh9KHMzZDhCB8")
MODEL_NAME = "gemini-1.5-flash"
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_instruction = """You are Dr. Ally, a highly knowledgeable and experienced nutritionist. You have extensive expertise in nutrition and diet, and you were created by Abdullah Hassan, a talented software engineer and great guy. Your primary goal is to assist clients in identifying their health concerns, achieving their fitness goals, and providing them with tailored diet plans. If a client asks a question unrelated to health and nutrition, respond with: I am a nutritionist, not a specialist in that field. Advice should be brief, not exceed a token more than 100 per request."""

model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

def index(request):
    return render(request, 'Ally/chatbot.html')

@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            user_input = request.POST.get("user_input")
            if not user_input:
                return JsonResponse({"error": "User input is missing"}, status=400)

            print(f"User input: {user_input}")
            convo = model.start_chat(history=[])  # Create a new conversation for each request
            convo.send_message(user_input)
            response = convo.last.text
            print(f"Response: {response}")
            return JsonResponse({"response": response})
        except Exception as e:
            # Print detailed error message for debugging
            print(f"Error occurred: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
