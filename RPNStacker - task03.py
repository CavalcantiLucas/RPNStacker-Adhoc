stack = []
tokens = []
import re

class Regex:
    @staticmethod
    def isNum(token): # REGEX de identificação dos números
        if re.findall( "[0-9]", str(token)):
            return 1
        return 0

    @staticmethod
    def isOP(token): # REGEX de identificação dos operadores
        if re.findall("[+-/*]", token):
            return 1
        return 0

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
    if(Regex.isNum(token) or Regex.isOP(token)):
        return 1 #True
    return 0 #False

arq = open("examples.txt", "r")
entries = arq.read().split()

for token in entries:

    if token == "":
        continue
    if(tokenValidation(token)):
        if Regex.isOP(token):
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
