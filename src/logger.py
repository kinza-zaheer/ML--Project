import logging
"""
Python ka built-in logging module import ho raha hai.ya 
messages save karta hai
errors track karta hai
logs maintain karta hai

"""
import os
"""
OS module:
folders
paths
files
handle karta hai.
"""
from datetime import datetime #current date and time ko use krna
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #is me current time
# ko use karke unique log filename bana raha hai.
# strftime Time ko formatted string me convert karta hai.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #e path create kar raha hai.
#os.getcwd() Current working directory deta hai.
os.makedirs(logs_path,exist_ok=True) #Ye automatically folder create karega
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # is me final complete log file path
# create horha ha
logging.basicConfig( #Logging system setup karna.
    filename=LOG_FILE_PATH, #Logs kis file me save honge.
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)