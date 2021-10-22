import argparse

class Command:
    def __init__(self, cmdType, value) -> None:
        self.type = cmdType
        self.value = value
    
    def __str__(self) -> str:
        return self.type + ": " + self.value

class Parser:
    def __init__(self, filePath) -> None:
        with open(filePath, "r") as fileToParse:
            self.inputLines = fileToParse.readlines()
        fileToParse.close()

        self.currentLineNumber = 0

    def hasMoreCommands(self) -> bool:
        return self.currentLineNumber < len(self.inputLines)

    def getNextCommand(self) -> Command:
        # Skip over lines with only whitespace or comments.
        while self.__getStrippedLine(self.currentLineNumber) == '':
            self.currentLineNumber += 1
        line = self.inputLines[self.currentLineNumber]

        cmd = Command("CMD", line)  
        self.currentLineNumber += 1

        return cmd

    # Strips a line of comments and whitespace and returns it.
    def __getStrippedLine(self, lineNumber:int) -> str:
        self.inputLines[lineNumber] = self.inputLines[lineNumber].strip()

        # Returns -1 if no comments are found.
        commentStartIndex = self.inputLines[lineNumber].find("//")
        return self.inputLines[lineNumber] if commentStartIndex == -1 else self.inputLines[lineNumber][:commentStartIndex]

    def __del__(self) -> None:
        pass


def assembler(filePath):
    print("Translating file: " + filePath)
    parser = Parser(filePath)

    while parser.hasMoreCommands():
        cmd = parser.getNextCommand()
        print("LINE: " + cmd.__str__())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-p", "--path", help="Path to the .hack assembly file to translate.", required=True)
    args = argparser.parse_args()

    filePath = args.path
    assembler(filePath)