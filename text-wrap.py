import textwrap

def wrap(string, max_width):
    result = ''
    for i in range(0, len(string), max_width):
        line = string[i:i+max_width]
        if i + max_width >= len(string):  
            result += line
        else:
            result += line + '\n'
    return result

string = input("Enter the string: ")
max_width = int(input("Enter max width: "))

print(wrap(string, max_width))
