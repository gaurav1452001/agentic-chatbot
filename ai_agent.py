import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults


from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_ai_response(llm_id,query,allow_search,system_prompt,provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    tools=[TavilySearchResults(max_results=2)] if allow_search else []
 
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state={"messages":query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[msg.content for msg in messages if isinstance(msg, AIMessage)]
    return ai_messages[-1]