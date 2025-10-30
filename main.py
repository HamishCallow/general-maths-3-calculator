
def main():
    a = float(input("enter first term: "))
    d = float(input("enter common difference: "))
    n = float(input("enter number of terms: "))
    tn = a + ((n - 1) * d)
    print(tn)

if __name__ == "__main__":
    main()
