class Simpletron:
    def __init__(self):
        self.memory = [0] * 100  # Memory array with 100 elements
        self.accumulator = 0
        self.instruction_counter = 0

    def read_instruction(self):
        while True:
            try:
                value = int(input(f"{self.instruction_counter:02d} ? "))
                if value == -99999:
                    break
                self.memory[self.instruction_counter] = value
                self.instruction_counter += 1
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def execute_program(self):
        while True:
            opcode = self.memory[self.instruction_counter] // 100
            operand = self.memory[self.instruction_counter] % 100

            if opcode == 10:
                value = int(input("Please enter a value: "))
                self.memory[operand] = value
            elif opcode == 11:
                print(self.memory[operand])
            elif opcode == 20:
                self.accumulator = self.memory[operand]
            elif opcode == 21:
                self.memory[operand] = self.accumulator
            elif opcode == 30:
                self.accumulator += self.memory[operand]
            elif opcode == 31:
                self.accumulator -= self.memory[operand]
            elif opcode == 32:
                self.accumulator //= self.memory[operand]
            elif opcode == 33:
                self.accumulator *= self.memory[operand]
            elif opcode == 40:
                self.instruction_counter = operand
            elif opcode == 41:
                if self.accumulator < 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 42:
                if self.accumulator == 0:
                    self.instruction_counter = operand
                    continue
            elif opcode == 43:
                print("*** Simpletron execution terminated ***")
                break

            self.instruction_counter += 1

def main():
    simpletron = Simpletron()
    
    # Display welcome message
    print("*** Welcome to Simpletron! ***")
    print("*** Please enter your program one instruction ***")
    print("*** (or data word) at a time into the input ***")
    print("*** text field. I will display the location ***")
    print("*** number and a question mark (?). You then ***")
    print("*** type the word for that location. Enter ***")
    print("*** -99999 to stop entering your program. ***")

    simpletron.read_instruction()

    # Display program loading completion message
    print("*** Program loading completed ***")
    print("*** Program execution begins ***")
    simpletron.instruction_counter = 0
    simpletron.execute_program()

if __name__ == "__main__":
    main()
