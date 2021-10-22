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
        # Only comp and jump field, no dest field.
        if line.find('=') == -1:
            self.dest = "null"
            jumpSplit = line.split(';')
            self.comp = jumpSplit[0].strip()
            self.jump = jumpSplit[1].strip()

        # Only comp and dest field, no jump field.
        else:
            self.jump = "null"
            destSplit = line.split('=')
            self.dest = destSplit[0].strip()
            self.comp = destSplit[1].strip()

    
    def __str__(self) -> str:
        return "[C]: Dest (" + self.dest + "), Comp (" + self.comp +"), Jump (" + self.jump + ")"

    def getBinaryTranslation(self) -> str:
        return "111" + HackSpec.translateCompField(self.comp) + HackSpec.translateDestField(self.dest) + HackSpec.translateJumpField(self.jump)