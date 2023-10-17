# BusinessBots

## What's the idea ?

The idea is to provide a python api that can provide customer support for busineess. It can be powerd by GPT 4 or any other compatible open source LLM. For each business an AI agent will be created that is trained specificaly with necessary and not confidential business details just like an customer support human agent. This AI agent should also store the conversation history for each customer in MongoDB in chat format.

## How this api is going to generate revenue ?

Business will be charged according to the tokens generated through LLM. If we are using GPT 4 then the cost will be higher compared to open source LLM. To reduce the cost we can use their locla machines if they have any to power this AI agent. 
