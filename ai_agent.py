import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

agent=create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt
)

query="tell me about the latest news on AI"
state={"messages":query}
response=agent.invoke(state)
messages=response.get("messages")
ai_messages=[msg.content for msg in messages if isinstance(msg, AIMessage)]
print(ai_messages[-1])