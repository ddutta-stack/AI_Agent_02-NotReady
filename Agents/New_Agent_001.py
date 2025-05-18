# New Agents   
# This is a new agent that will be used for testing purposes.
# It is a simple agent that will respond to user input with a predefined message.
from selenium import webdriver
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome()
driver.get("https://www.example.com")
driver.implicitly_wait(10)
# Define the agent's response

