# importing libraries
from github import Github
from config import config as cfg
import requests

# retrieing the key from the config file
apikey = cfg["githubkey"]
#use your own your own key
g = Github(apikey)

# accessing and printing the repository URL
repo = g.get_repo("G00232918/aprivateone")
print(repo.clone_url)

# accessing the content
fileInfo = repo.get_contents("assign4.txt")
# getting the download url
urlOfFile = fileInfo.download_url
print(urlOfFile)

# sending the get request to down the file
response = requests.get(urlOfFile)
# extracting the content
contentOfFile = response.text
print(contentOfFile)


# replace "Andrew" with "James" in the content of the text file
# reference - https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
newContents = contentOfFile.replace("Andrew", "James")
print(newContents)

# updating the text file contents and a commit statement
change_result = repo.update_file(fileInfo.path, "replaced Andrew with James", newContents, fileInfo.sha, branch="main")
print(change_result)

