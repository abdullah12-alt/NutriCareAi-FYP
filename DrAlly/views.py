from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import google.generativeai as genai

genai.configure(api_key="AIzaSyCSGlHySkwncCd1ftzJYef1a03d8BHvnyc")
MODEL_NAME = "gemini-1.5-pro-latest"
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

system_instruction = "Your Name is Dr Ally and You are a Nutritionist and dietitian, you will guide the patient and client based on their symptoms and fitness goals. Advice should be brief, not exceed a token more than 100 per request, "

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)


def index(request):
    return render(request, 'Ally/chatbot.html')

# @csrf_exempt
# def chat(request):
#     print("used this func")
#     global model
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         if not model:
#             model = load_model()
#         if model:
#             convo = model.start_chat(history=[])
#             convo.send_message(user_input)
#             response = convo.last.text
#             print(response)
#             return JsonResponse({'response': response})
#         else:
#             return JsonResponse({'error': 'Failed to load model'}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            user_input = request.POST.get("user_input")
            convo = model.start_chat(history=[])  # Create a new conversation for each request
            convo.send_message(user_input)
            response = convo.last.text
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)