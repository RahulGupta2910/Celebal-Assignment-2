def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i+k]
        seen = set()
        result = ''
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch
        print(result)

input_string = input("Enter the string: ")
segment_length = int(input("Enter the segment length (k): "))

merge_the_tools(input_string, segment_length)
