'''
Parser.py

Implements a basic parser for the Hack Assembly language.
'''
from typing import Union
from Instruction import AInstruction, CInstruction

class Parser:
    def __init__(self, filePath) -> None:
        with open(filePath, "r") as fileToParse:
            self.inputLines = fileToParse.readlines()
        fileToParse.close()

        self.currentLineNumber = 0

    def hasMoreCommands(self) -> bool:
        return self.currentLineNumber < len(self.inputLines)

    def getNextCommand(self) -> Union[AInstruction, CInstruction]:
        # Skip over lines with only whitespace or comments.
        while self.__getStrippedLine(self.currentLineNumber) == '':
            self.currentLineNumber += 1
        line = self.inputLines[self.currentLineNumber]

        cmd = AInstruction(line) if line[0] == '@' else CInstruction(line)
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