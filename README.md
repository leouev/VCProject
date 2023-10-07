# VCProject
This is a CISC 594 project for software configuration management project
Based on the problem descriptions from the text book "Visual C# How to Program, 5th Edition" by Paul Deitel and Harvey Deitel.

Problem descriptions can be find at 8.31, 8.32, 8.33. The programming language for this project will be in Python 3.12.0

# v1.0:
all operations needed for the following:
 ## input/output operations:
  - const int READ = 10; Read a word from the key board into a specific location in memory.
  - const int WRITE = 11; Write a word from a specific location in memory to the screen.
 ## load/store operations:
  - const int LOAD = 20; Load a word from specific location in memeory into the accumulator.
  - const int STORE = 21; Store a word from accumulator into a specific location in memory
 ## Arithmetic operations:
  - const int ADD = 30; Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).
  - const int SUBTRACT = 31; Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
  - const int DIVIDE = 32; Divide a word from a speicific location in memory into the word in the accumulator (leave the result in the accumulator)
  - const int MULTIPLY = 33; Multiply a word from a specific location in memory by the word in the accumulator (leave the result in the accumulator)
 ## Transfer of control operations:
  - const int BRANCH = 40; Branch to a specific location in memory
  - const int BRANCHNEG = 41; Branch to a specific location in memory if the accumulator is negative
  - const int BRANCHZERO = 42; Branch to a specific location in memoery if the accumulator is zero
  - const int HALT = 43; Halt. The program has completed its task.

