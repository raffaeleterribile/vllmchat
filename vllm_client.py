""" Esempio di client Python per l'utilizzo di vLLM tramite l'API di OpenAI. """
from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
OPENAI_API_KEY = "EMPTY"
OPENAI_API_BASE = "http://localhost:8000/v1"

MODEL_ID = "microsoft/Phi-3-mini-128k-instruct"

# Esempio di completamento - Url di esempio: http://localhost:8000/v1/completions
client = OpenAI(
	api_key=OPENAI_API_KEY,
	base_url=OPENAI_API_BASE,
)

print(">>> Esempio di completamento")
completion = client.completions.create(model=MODEL_ID,
									   max_tokens=7,
									   temperature=0,
									   prompt="San Francisco is a")
print("Completion result:", completion)

# Esempio di chat - Url di esempio: http://localhost:8000/v1/chat/completions
print(">>> Esempio di chat")
client = OpenAI(
	api_key=OPENAI_API_KEY,
	base_url=OPENAI_API_BASE,
)

chat_response = client.chat.completions.create(model=MODEL_ID,
											   max_tokens=7,
											   temperature=0,
											   messages=[
												   {"role": "system", "content": "You are a helpful assistant."},
												   {"role": "user", "content": "Tell me a joke."}
												]
)
print("Chat response:", chat_response)

# Esempio di streaming chat - Url di esempio: http://localhost:8000/v1/chat/completions
print(">>> Esempio di streaming chat")
client = OpenAI(
	api_key=OPENAI_API_KEY,
	base_url=OPENAI_API_BASE,
)

stream = client.chat.completions.create(model=MODEL_ID,
											   max_tokens=7,
											   temperature=0,
											   stream=True,
											   messages=[
												   {"role": "system", "content": "You are a helpful assistant."},
												   {"role": "user", "content": "Tell me a joke."}
												]
)
# Print generated text from response stream
accumulated_message = ""
for chunk in stream:
	accumulated_message += (chunk.choices[0].delta.content or "")
	print(accumulated_message)

print("Streaming Chat response:", accumulated_message)
