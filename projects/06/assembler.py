import argparse
from Parser import Parser

def assembler(filePath):
    print("Translating file: " + filePath)
    parser = Parser(filePath)

    while parser.hasMoreCommands():
        cmd = parser.getNextCommand()
        print(cmd)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-p", "--path", help="Path to the .hack assembly file to translate.", required=True)
    args = argparser.parse_args()

    filePath = args.path
    assembler(filePath)