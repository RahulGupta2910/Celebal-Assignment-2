number_of_elements = int(input("Input number of elements- "))
initial_set = set(map(int, input("Enter the numbers of the set- ").split()))
number_of_commands = int(input("Number of commands- "))

for _ in range(number_of_commands):
    command_parts = input().split()
    command = command_parts[0]

    if command == 'pop':
        initial_set.pop()
    elif command == 'remove':
        initial_set.remove(int(command_parts[1]))
    elif command == 'discard':
        initial_set.discard(int(command_parts[1]))

print(sum(initial_set))
