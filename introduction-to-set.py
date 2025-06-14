def average(array):
    s = set(array)
    total = sum(s)
    length = len(s)
    return float(total / length)

arr = list(map(int, input("Enter space-separated integers: ").split()))
print(average(arr))
