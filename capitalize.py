def solve(s):
    separate_words = s.split(' ')
    capitalized_words = [word.capitalize() for word in separate_words]
    final_string = ' '.join(capitalized_words)
    return final_string

s = input("Enter a string: ")
print(solve(s))
