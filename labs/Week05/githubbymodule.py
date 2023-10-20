from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
#use your own your own key
g = Github(apikey)

for repo in g.get_user().get_repos():
    #print(repo.name)
    fileInfo = repo.get_contents("test.txt")
    urlOfFile = filInfo.download_url
    print(urlOfFile)