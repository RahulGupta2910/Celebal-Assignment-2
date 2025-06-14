def print_rangoli(size):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    width = 4 * size - 3
    pattern = []

    for i in range(size):
        left = alphabets[size-1:size-1-i:-1]
        right = alphabets[size-1-i:size]
        row = left + right
        line = '-'.join(row)
        pattern.append(line.center(width, '-'))

    for i in range(size-2, -1, -1):
        pattern.append(pattern[i])

    print('\n'.join(pattern))


n = int(input("Enter the size of rangoli you want- "))
print_rangoli(n)
