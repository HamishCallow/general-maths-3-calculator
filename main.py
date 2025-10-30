from arithmaticsequence import arithmatic_sequence
from geometricsequence import geometric_sequence

def main():
    print(f"[1] - arithmatic sequence")
    print(f"[2] - geometric sequence")
    option = int(input("select formula to use (number): "))
    if option == 1:
        arithmatic_sequence()
    if option == 2:
        geometric_sequence()
    else:
        print(f"{option} is not in list of fuctions")

if __name__ == "__main__":
    main()