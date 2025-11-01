
def arithmetic_series():
    a = float(input("enter first term: "))
    d = float(input("enter common difference: "))
    n = int(input("enter number of terms: "))
    series = []
    for i in range(1, n + 1):
        sn = (i / 2) * (2 * a + (i - 1) * d)
        series.append(sn)
    print(series)

