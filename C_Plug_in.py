string = input()
stack = []

for char in string:
    if len(stack) !=0 and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

print(''.join(stack))
