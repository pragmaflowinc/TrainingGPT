from chatgpt_memory.datastore import RedisDataStoreConfig, RedisDataStore
import os
 
 
redis_datastore_config = RedisDataStoreConfig(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASSWORD'),
)
redis_datastore = RedisDataStore(config=redis_datastore_config)

api_key = os.getenv('OPENAI_API_KEY')

from chatgpt_memory.llm_client import EmbeddingConfig, EmbeddingClient
 
embedding_config = EmbeddingConfig(api_key)
embed_client = EmbeddingClient(config=embedding_config)

from chatgpt_memory.memory.manager import MemoryManager
 
memory_manager = MemoryManager(
    datastore=redis_datastore,
    embed_client=embed_client,
    topk=1
)

from chatgpt_memory.llm_client import ChatGPTClient, ChatGPTConfig
 
chat_gpt_client = ChatGPTClient(
    config=ChatGPTConfig(api_key, verbose=True),
    memory_manager=memory_manager
)

conversation_id = None
while True:
    user_message = input("\n Please enter your message: ")
    response = chat_gpt_client.converse(
        message=user_message,
        conversation_id=conversation_id
    )
    conversation_id = response.conversation_id
    print(response.chat_gpt_answer)