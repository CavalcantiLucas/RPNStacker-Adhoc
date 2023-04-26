stack = []
tokens = []
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

def tokenValidation(token):
    if(token in operators or token.isnumeric()):
        return 1 #True
    return 0 #False

arq = open("examples.txt", "r")
entries = arq.read().split()

for token in entries:

    if token == "":
        continue
    if(tokenValidation(token)):
        if token in operators:
            if token == '*':
                tokens.append("type= STAR")
                tokens.append("lexeme= *")
            elif token == '/':
                tokens.append("type= SLASH")
                tokens.append("lexeme= /")
            elif token == '+':
                tokens.append("type= PLUS")
                tokens.append("lexeme= +")
            else:
                tokens.append("type= MINUS")
                tokens.append("lexeme= -")
        else:
            tokens.append("type= NUM")
            tokens.append("lexeme= " + str(token))
    else:
        print(f"{token} is invalid")


for i in range(0, len(tokens), 2):
    if tokens[i] == "type= NUM":
        stack.append(int(tokens[i+1][8:]))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(mathExecution(tokens[i+1][8:], n2, n1))

print("Resultado: " + str(stack.pop()))
