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

    

(LOOP)
    @SCREEN
    D = A    // D = 16384, base address of the screen in RAM.

    @screen
    M = D     // screen = 16384
    
    @KBD  
    D = M   // Poll RAM[24576] for keyboard scan code.

    @fillValue
    M = 0   // Default fillValue is 0. Used to fill white screen

    @FILL
    D; JEQ  // Jump to FILL if Keyboard scancode == 0. No key was pressed.

    @fillValue
    M = -1      // Set fillValue to -1, which is black in 2s complement binary (1111111..) 

(FILL)
    @screen
    D = M   // i = 0

    @256
    // Loop exit condtion




