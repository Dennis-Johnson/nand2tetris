'''
SymbolTable.py

Defines a class to handle symbols encountered during the Hack assembly translation.
'''

from typing import List


class SymbolTable:
    def __init__(self) -> None:
        # Add some predefined symbols to the symbol table.
        self.symbols = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 11,
            "R11": 12,
            "R12": 13,
            "R13": 14,
            "R14": 15,
            "R15": 16,
            "SCREEN": 16384,
            "KBD": 24576
        }

        # The next RAM address to which a symbol can be assigned
        self.nextAvailableAddress = 17
    
    # Adds a (symbol, address) pair to the symbol table.
    def addSymbol(self, symbol:str, address: int) -> None:
        self.symbols[symbol] = address

    def contains(self, symbol:str) -> bool:
        return True if symbol in self.symbols else False
    
    def getAddress(self, symbol:str) -> int:
        return self.symbols[symbol]
