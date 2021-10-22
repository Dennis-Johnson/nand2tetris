'''
HackSpec.py

Class to lookup binary values for mnemonics in the Hack Assembly specification.
'''

class HackSpec:
    # Comp field with bits a-c-c-c-c-c-c
    compField = {
        "0":  "0101010",
        "1":  "0111111",
        "-1": "0111010",
        "D":  "0001100",
        "A":  "0110000",
        "M":  "1110000",
        "!D": "0001101",
        "!A": "0110001",
        "!M": "1110001",
        "-D": "0001111",
        "-A": "0110011",
        "-M": "1110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "M-1": "1110010",
        "D+A": "0000010",
        "D+M": "1000010",
        "D-A": "0010011",
        "D-M": "1010011",
        "A-D": "0000111", 
        "M-D": "1000111",
        "D&A": "0000000",
        "D&M": "1000000",
        "D|A": "0010101",
        "D|M": "1010101",
    }

    # Destination field with bits d1-d2-d3
    destField = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }

    # Jump field with bits j1-j2-j3
    jumpField = {
        "null":"000",
        "JGT":"001",
        "JEQ":"010",
        "JGE":"011",
        "JLT":"100",
        "JNE":"101",
        "JLE":"110",
        "JMP":"111",
    }
    
    @staticmethod
    def translateCompField(compKey: str) -> str:
        if compKey in HackSpec.compField:
            return HackSpec.compField[compKey]
        
        raise KeyError("The comp mnemonic " + compKey + " is invalid.")
    
    @staticmethod
    def translateDestField(destKey: str) -> str:
        if destKey in HackSpec.destField:
            return HackSpec.destField[destKey]
        
        raise KeyError("The dest mnemonic " + destKey + " is invalid.")
        
    @staticmethod
    def translateJumpField(jumpKey: str) -> str:
        if jumpKey in HackSpec.jumpField:
            return HackSpec.jumpField[jumpKey]
        
        raise KeyError("The jump mnemonic " + jumpKey + " is invalid.")