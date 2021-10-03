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

// Put your code here.
  @SCREEN
  D=A
  @1 // 何点塗るか
  D=A+D
  @full
  M=D+A
(LOOP_KBD)
  @SCREEN
  D=A
  @position
  M=D
  @KBD
  D=M
  @WHITE
  D;JEQ
  @BLACK
  0;JMP
(WHITE)
  @color
  M=0
  @PAINT
  0;JMP
(BLACK)
  @color
  M=1
  @PAINT
  0;JMP
(PAINT)
  @full
  D=M
  @position
  D=D-M
  @END
  D;JEQ
  @color
  D=M
  @position
  A=M
  M=D
  @position
  M=M+1
  @PAINT
  0;JMP
(END)
  @LOOP_KBD
  0;JMP