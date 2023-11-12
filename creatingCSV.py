# 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

from github import Github
from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time

access_token = "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"

g = Github(access_token, retry=20)

current_user = g.get_user()
print(current_user.name)
print(current_user.bio)

repos = g.get_user().get_repos()


def extract_project_info():
    df_project = pd.DataFrame()

    for repo in repos:
        pr = repo.get_pulls(state='all')
        df_project = df_project.append({
            'Repo_ID': repo.id,
            'Project_Name': repo.name,
            'Full_name': repo.full_name,
            'Language': repo.language,
            'Forks': repo.forks_count,
            'Stars': repo.stargazers_count,
            'Watchers': repo.subscribers_count,
            'PRs_count': pr.totalCount
        }, ignore_index=True)
    df_project.to_csv('../project_dataset.csv', sep=',', encoding='utf-8', index=True)


extract_project_info()
