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

        # First pass to add just labels to symbol table.
        self.addLabels()


    def hasMoreCommands(self) -> bool:
        return self.currentLineNumber < len(self.inputLines)

    def getNextCommand(self) -> Union[AInstruction, CInstruction]:
        # Skip over lines with only whitespace, comments, or labels.
        while self.__getStrippedLine(self.currentLineNumber) == '':
            self.currentLineNumber += 1
        line = self.inputLines[self.currentLineNumber]

        if line.startswith('@'):
            if line[1:].isnumeric():
                cmd = AInstruction(line)
            
            # Otherwise, it's a symbol
            else:
                symbolName = line[1:]
                if not self.symbolTable.contains(symbolName):
                    self.symbolTable.addVariable(symbolName)
                
                cmd = AInstruction("@" + str(self.symbolTable.getAddress(symbolName)))
        else: 
            cmd = CInstruction(line)
        
        self.currentLineNumber += 1
        return cmd

    # Strips a line of comments and whitespace and returns it.
    def __getStrippedLine(self, lineNumber:int) -> str:
        self.inputLines[lineNumber] = self.inputLines[lineNumber].strip()

        # Returns -1 if no comments are found.
        commentStartIndex = self.inputLines[lineNumber].find("//")
        if not commentStartIndex == -1:
            self.inputLines[lineNumber] = self.inputLines[lineNumber][:commentStartIndex].strip()

        # Clears line if it's a label
        if self.inputLines[lineNumber].startswith('(') and self.inputLines[lineNumber].endswith(')'):
            self.inputLines[lineNumber] = ""

        return self.inputLines[lineNumber]

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
