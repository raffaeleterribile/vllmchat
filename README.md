# vLLM Chat

Progetto di prova per studiare vLLM

Avviare il server vLLM con:

vllm serve facebook/opt-125m

Esempi di usi con curl

Elenco dei modelli
curl http://localhost:8000/v1/models

Esempio di completamento
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "facebook/opt-125m",
        "prompt": "San Francisco is a",
        "max_tokens": 7,
        "temperature": 0
    }'

Esempio di chat
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "Qwen/Qwen2.5-1.5B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'
