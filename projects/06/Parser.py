'''
Parser.py

Implements a parser for the Hack Assembly language.
'''

from typing import Union
from Instruction import AInstruction, CInstruction
from SymbolTable import SymbolTable

class Parser:
    def __init__(self, filePath) -> None:
        with open(filePath, "r") as fileToParse:
            self.inputLines = fileToParse.readlines()
        fileToParse.close()
        self.currentLineNumber = 0

        self.symbolTable = SymbolTable()
        # First pass to add labels to symbol table.
        self.addLabels()


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

    # First pass where all labels and their addresses are identified. No translation yet.
    def addLabels(self) -> None:
        lineNumber = 0
        assert len(self.inputLines) > 0, "No lines to parse."

        for line in self.inputLines:
            line = line.strip()

            # Skip lines with only whitespace or comments
            if line == "" or line.startswith("//"):
                continue
                
            # Add this label to the symbol table.
            elif line.startswith('(') and line.endswith(')'):
                symbolName = line[1:-1]
                assert not self.symbolTable.contains(symbolName), "This label is already defined."
                self.symbolTable.addSymbol(symbolName, lineNumber)

            # Increment counter when you find an A or C instruction.
            else: 
                lineNumber += 1

        print(self.symbolTable.symbols)
