'''
Classes for the two instruction types in Hack Assembly.
A-Instructions and C-Instructions.
'''

class AInstruction:
    def __init__(self, value) -> None:
        # Remove the leading '@' sign.
        self.value = value[1:]
    
    def __str__(self) -> str:
        return "AInstr: " + self.value

class CInstruction:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return "CInstr: " + self.value