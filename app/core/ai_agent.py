from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings

import app.core.ai_agent as aa
print("USING ai_agent.py FROM:", aa.__file__)

def get_response_from_ai_agents(llm_id , query , allow_search ,system_prompt):

    llm = ChatGroq(
    model=llm_id,
    temperature=0.3
)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    user_text = query[0] if isinstance(query, list) and len(query) > 0 else str(query)
    
    state = {"messages": [{"role": "user", "content": user_text}]}

    response = agent.invoke(state)

    messages = response.get("messages", [])
    
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
    
    return ai_messages[-1] if ai_messages else ""

    # messages = response.get("messages")

    # ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    # return ai_messages[-1]





