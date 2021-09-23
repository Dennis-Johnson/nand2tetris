// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    @i
    M = 0     // i = 0

    @prod
    M = 0     // prod = 0

(LOOP)
    @i
    D = M     // D = i

    @R0
    D = D- M    //  D = i - R0

    @STORE 
    D; JGE      // JMP to STORE if (i - R0) >= 0

    @R1
    D = M       // D = R1

    @prod
    M = D + M   // prod = R1 + prod


    @i
    M = M + 1   // i = i + 1

    @LOOP
    0; JMP

(STORE)
    @prod
    D = M       // D = prod
    
    @R2
    M = D       // R2 = prod

(END)
    @END
    0; JMP





