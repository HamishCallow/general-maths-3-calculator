
def geometric_sequence():
    a = float(input("enter first term: "))
    r = float(input("enter common ratio: "))
    n = int(input("enter number of terms: "))
    sequence = []
    for i in range(n):
        tn = a * r ** i
        sequence.append(tn)
    print(sequence)