// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(OUTERLOOP)
    @fillValue
    M = 0               // Default fillValue is 0. Used to fill white screen

    @KBD
    D = M               // Poll RAM[24576] for keyboard scan code.

    @FILL
    D; JEQ              // Jump to FILL if Keyboard scancode == 0. No key was pressed.

    @fillValue
    M = -1              // Set fillValue to -1, which is black in 2s complement binary (1111111111111111)

(FILL)
    @SCREEN
    D = A               // D = RAM[16384], the base address of the screen.

    @screenAddress
    M = D               // screenAddress = SCREEN.

    @i
    M = 0               // i = 0. Counter for fill loop.

    @8191
    D = A               // D = 8K

    @n
    M = D               // n = 8K, the whole screen.

(DRAWLOOP)
    @i
    D = M                // D = i

    @n
    D = D - M            // D = i - n

    @OUTERLOOP
    D; JGT               // Jump to OUTERLOOP if (i - n) > 0. Done filling the screen.

    @fillValue  
    D = M                // D = fillValue

    @screenAddress
    A = M                // A = screenAddress
    M = D                // fill with the fillValue

    @screenAddress
    D = M                // D = screenAddress      
    M = D + 1            // screenAddress += 1

    @i
    M = M + 1            // i += 1

    @DRAWLOOP
    0; JMP

(END)
    @END
    0; JMP              // END, infinite loop.




