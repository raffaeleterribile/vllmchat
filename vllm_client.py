from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

MODEL_ID = "microsoft/Phi-3-mini-128k-instruct"

# Esempio di completamento - Url di esempio: http://localhost:8000/v1/completions
client = OpenAI(
	api_key=openai_api_key,
	base_url=openai_api_base,
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
	api_key=openai_api_key,
	base_url=openai_api_base,
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
	api_key=openai_api_key,
	base_url=openai_api_base,
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
partial_message = ""
for chunk in stream:
	partial_message += (chunk.choices[0].delta.content or "")
	print(partial_message)

print("Streaming Chat response:", partial_message)
