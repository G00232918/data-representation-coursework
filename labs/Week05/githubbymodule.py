from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
#use your own your own key
g = Github(apikey)

repo = g.get_repo("G00232918/aprivateone")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)
newContents = contentOfFile + "more stuff \n"
#print(newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents,fileInfo.sha)
print (gitHubResponse)
