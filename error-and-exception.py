t = int(input("Enter the number of test cases- "))

for _ in range(t):
    print("Enter the value of A and B- ")
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
