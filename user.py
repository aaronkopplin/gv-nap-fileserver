class User:
    username = ""
    files = []

    def __init__(self, username):
        self.username = username
        self.files = []

    def addFile(self, fileName):
        self.files.append(fileName)

    def getUsername(self):
        return self.username