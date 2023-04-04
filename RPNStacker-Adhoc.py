stack = []
operators = ['*', '/', '+', '-']

def mathExecution(operator, num1, num2):
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2

print("End operation loop with the word STOP")

while 1:
    element = input()
    if element in operators:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(mathExecution(element, n1, n2))
    elif element == 'STOP':
        print(f"answer = {stack.pop()}")
        break
    else:
        stack.append(float(element))
