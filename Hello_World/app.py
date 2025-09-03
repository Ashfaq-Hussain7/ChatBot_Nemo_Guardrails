# app.py
 
from nemoguardrails import RailsConfig, LLMRails
 
# Load config from ./config folder
config = RailsConfig.from_path("./config")
rails = LLMRails(config)
 
# Send a greeting message
response = rails.generate(messages=[{
    "role": "user",
    "content": "Hello!"
}])
 
# Print the bot's full reply, which will include 2 lines
print(response["content"])
 
response = rails.generate(messages=[{
    "role": "user",
    "content": "What is the capital of France?"
}])
print(response["content"])