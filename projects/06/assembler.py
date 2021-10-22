"""
assembler.py

Translates a .asm file to a binary .hack file.
"""
import argparse
from Parser import Parser

def assembler(filePath):
    print("Translating file: " + filePath + "\n")

    # Get file name
    fileName = filePath.split(".")[0].split('/')[-1]

    parser = Parser(filePath)
    translatedLines = []

    while parser.hasMoreCommands():
        cmd = parser.getNextCommand()
        print(cmd.__str__() + " --> " + cmd.getBinaryTranslation())
        translatedLines.append(cmd.getBinaryTranslation())

    # Write translated lines to the .hack file"
    with open(fileName + ".hack", "w") as binFile:
        for line in translatedLines:
            print(line, file = binFile)
    binFile.close()

    print("\nSuccess --> " + fileName + ".hack created")

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-p", "--path", help="Path to the .hack assembly file to translate.", required=True)
    args = argparser.parse_args()

    filePath = args.path
    assembler(filePath)