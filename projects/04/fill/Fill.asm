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

    

    @SCREEN
    D = A               // D = RAM[16384], the base address of the screen.

    @screenAddress
    M = D               // screenAddress = SCREEN.

    @i
    M = 0               // i = 0. Counter for fill loop.

    @64
    D = A               // D = 64

    @n
    M = D               // n = 64, number of rows to fill.

(LOOP)
    @i
    D = M                // D = i

    @n
    D = D - M            // D = i - n

    @END
    D; JGT               // Jump to END if (i - n) > 0

    @screenAddress
    A = M                // A = screenAddress
    M = -1               // fill with black at RAM[A]

    @screenAddress
    D = M                // D = screenAddress
    @32
    D = D + A           
    @screenAddress
    M = D                // screenAddress = screenAddress + 32

    @i
    M = M + 1            // i += 1

    @LOOP
    0; JMP

(END)
    @END
    0; JMP              // END, infinite loop.




