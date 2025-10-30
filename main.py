from arithmeticsequence import arithmetic_sequence
from geometricsequence import geometric_sequence

def main():
    functions = {
        1: ("arithmetic_sequence", arithmetic_sequence),
        2: ("geometric_sequence", geometric_sequence)
    }

    print("Available formulas")
    for key, (name, _) in functions.items():
        print(f"[{key}] - {name}")

    option = input("select formula to use by typing the number in the square brakets: ")
    
    if not option.isdigit():
        print(f"Error {option} is not a number. Please type a number in the square brakets")
        return

    option = int(option)

    if option in functions:
        _, func = functions[option]
        func()
    else:
        print(f"Error {option} is not in list of formulas. Please type a number in the square brakets")
        return

if __name__ == "__main__":
    main()