def is_valid_regex(pattern):
    repeat_operators = {'*', '+', '?'}
    for i in range(1, len(pattern)):
        if pattern[i] in repeat_operators and pattern[i - 1] in repeat_operators and pattern[i - 1] != '\\':
            return False
        if pattern[i] in repeat_operators and pattern[i - 1] == '\\':
            continue
    return True

n = int(input("Enter the number of test cases- "))
for _ in range(n):
    pattern = input("Enter the pattern- ")
    print("True" if is_valid_regex(pattern) else "False")
