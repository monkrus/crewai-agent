from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate

llm = Ollama(model="mistral", request_timeout=30.0)

result = llm.complete("Hello world")
print(result)
