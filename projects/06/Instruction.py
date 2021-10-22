'''
Instruction.py

Contains classes for the two types of instructions in Hack Assembly.
A-Instructions and C-Instructions.
'''

# Addressing Instruction
class AInstruction:
    def __init__(self, value) -> None:
        # Remove the leading '@' sign.
        self.value = int(value[1:])
    
    def __str__(self) -> str:
        return "[A]: Value: (" + str(self.value) + ')'

# Compute Instruction
class CInstruction:
    def __init__(self, line) -> None:
        destSplit = line.split("=")
        self.dest = destSplit[0].strip() if len(destSplit) > 1 else ""
        
        jumpSplit = destSplit[1].split(";")
        self.jump = jumpSplit[1].strip() if len(jumpSplit) > 1 else ""
        self.comp = jumpSplit[0]
    
    def __str__(self) -> str:
        return "[C]: Dest (" + self.dest + "), Comp (" + self.comp +"), Jump (" + self.jump + ")"