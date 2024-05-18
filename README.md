# ollama-agent

 - create virtual environment (in shell)
 `python -m venv agent`
 `agent\Scripts\activate`

- installation
`pip3 install -r requirements.txt`

- to update outdated packages
`pip install pur`
`$ pur -r requirements.txt`

- install ollama
download [ollama](https://github.com/ollama/ollama)

- run `ollama run llama2`
- and `ollama run mistral` (4GB)
- if needed `pip install -U llama-index`

Note! 
`CTRL+D to close ollama terminal`

Problems ?
 - make sure the LLM is listening
`pip install llama-index qdrant_client torch transformers` `pip install llama-index-llms-ollama`
- didnt download codellama `ollama pull codellama`
- timeout error --> set request_timeout to 500.
