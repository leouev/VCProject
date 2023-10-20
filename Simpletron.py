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

    def read_file(self, program_file):
        with open(program_file, "r") as file:
            for line in file:
                instruction = int(line.strip())
                self.memory[self.instruction_counter] = instruction
                self.instruction_counter +=1

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

    def memory_dump(self):
        print("REGISTERS:")
        print(f"accumulator\t\t\t\t{self.format_4digit(self.accumulator)}")
        print(f"instruction_counter\t\t\t{self.format_2digit(self.instruction_counter)}")
        print(f"instruction_register\t\t\t{self.format_4digit(self.memory[self.instruction_counter])}")
        opcode, operand = divmod(self.memory[self.instruction_counter], 100)
        print(f"opcode\t\t\t\t\t{self.format_2digit(opcode)}")
        print(f"operand\t\t\t\t\t{self.format_2digit(operand)}\n")

        print("Memory:")
        print("{:3}".format(""), end="")
        for i in range(10):
            print(f"{i:7}", end="")
        print()

        for i in range(0, 100, 10):
            print(f"{i:2}", end="   ")
            for j in range(i, i + 10):
                print(self.format_4digit(self.memory[j]), end="  ")
            print()

    def format_4digit(self, word):
        if word >= 0:
            return f"+{word:04d}"
        if word < 0:
            return f"{word:05d}"
        
    def format_2digit(self, word):
        return f"{word:02d}"

def main():
    simpletron = Simpletron()
    
    # Display welcome message
    print("*** Welcome to Simpletron! ***")
    print("*** Please Choose an option: ***")
    print("1. Enter program manually")
    print("2. Load program from a file")
    choice = input ("Enter your choice: ")
    if choice == "1":
        print("*** Please enter your program one instruction ***")
        print("*** (or data word) at a time into the input ***")
        print("*** text field. I will display the location ***")
        print("*** number and a question mark (?). You then ***")
        print("*** type the word for that location. Enter ***")
        print("*** -99999 to stop entering your program. ***")
        simpletron.read_instruction()
    elif choice == "2":
        program_file = input("Enter the name of the program file: ")
        simpletron.read_file(program_file)
    # Display program loading completion message
    print("*** Program loading completed ***")
    print("*** Program execution begins ***")
    simpletron.instruction_counter = 0
    simpletron.execute_program()
    simpletron.memory_dump()

if __name__ == "__main__":
    main()
