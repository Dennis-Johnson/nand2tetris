'''
Instruction.py

Contains classes for the two types of instructions in Hack Assembly.
A-Instructions and C-Instructions.
'''
from HackSpec import HackSpec

# Addressing Instruction
class AInstruction:
    def __init__(self, value) -> None:
        # Remove the leading '@' sign.
        self.value = int(value[1:])
    
    def __str__(self) -> str:
        return "[A]: Value: (" + str(self.value) + ')'

    def getBinaryTranslation(self) -> str:
        binStr = "{0:b}".format(self.value)
        return binStr.zfill(16)


# Compute Instruction
class CInstruction:
    def __init__(self, line) -> None:
        destSplit = line.split("=")
        self.dest = destSplit[0].strip() if len(destSplit) > 1 else "null"
        
        jumpSplit = destSplit[1].split(";")
        self.jump = jumpSplit[1].strip() if len(jumpSplit) > 1 else "null"
        self.comp = jumpSplit[0]
    
    def __str__(self) -> str:
        return "[C]: Dest (" + self.dest + "), Comp (" + self.comp +"), Jump (" + self.jump + ")"

    def getBinaryTranslation(self) -> str:
        return "111" + HackSpec.translateDestField(self.dest) + HackSpec.translateCompField(self.comp) + HackSpec.translateJumpField(self.jump)