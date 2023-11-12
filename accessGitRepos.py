# 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 \\Naman
# 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 \\Siddhi

from github import Github
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time
from tkinter import *
from tkinter import messagebox

access_token = "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"


g = Github(access_token, retry=20)

current_user = g.get_user()
print(current_user.name)
print(current_user.bio)

repos = g.get_user().get_repos()

# create window
listDisplay = Tk()
listDisplay.title("AllYourRepos")
listDisplay.geometry("600x600")

# create Listbox
myList = Listbox(listDisplay)
myList.pack(pady=15)

for repo in repos:
    myList.insert("end", repo.name)


def select(myList):
    values = myList.curselection()
    if values:
        index = values[0]
        val = myList.get(index)
        messagebox.showinfo("Selction ", val)



