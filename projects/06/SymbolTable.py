'''
SymbolTable.py

Defines a class to handle symbols encountered during the Hack assembly translation.
'''

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
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576
        }

        # The next RAM address to which a symbol can be assigned
        self.nextAvailableAddress = 16
    
    # Adds a (symbol, address) pair to the symbol table. Used for labels.
    def addSymbol(self, symbol:str, address: int) -> None:
        assert self.nextAvailableAddress < 16384, "Symbol Table is full" 
        self.symbols[symbol] = address

    # Adds a (symbol, address) pair to the symbol table. Used for variables.
    def addVariable(self, symbol:str) -> None:
        assert self.nextAvailableAddress < 16384, "Symbol Table is full" 
        self.symbols[symbol] = self.nextAvailableAddress
        self.nextAvailableAddress += 1

    def contains(self, symbol:str) -> bool:
        return True if symbol in self.symbols else False
    
    def getAddress(self, symbol:str) -> int:
        return self.symbols[symbol]
