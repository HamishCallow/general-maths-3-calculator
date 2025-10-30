
def main():
    a = float(input("enter first term: "))
    d = float(input("enter common difference: "))
    n = int(input("enter number of terms: "))
    sequence = []
    for i in range(n):
        tn = a + i * d
        sequence.append(tn)
    print(sequence)

if __name__ == "__main__":
    main()
