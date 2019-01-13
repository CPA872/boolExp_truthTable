# Release v1.0
# Author: Yue Pan

def replace(string, originalList, newStr):
    result = ""
    for char in string:
        if char in originalList:
            result += str(bool(int(newStr[originalList.index(char)])))
        else:
            result += char
    return result

print("Enter single letter for a input. Enter \"!\" for complement, \"+\" for or, \".\" for and.")
print("Use () for precedence. Do NOT type spaces in the expression.")
exp = input("Boolean expression: " )
inputList, outputList = [], []
cmd = ""
for char in exp:
    if char.isalpha():
        if char.upper() not in inputList:
            inputList.append(char.upper())
    if char == "!":
        cmd += " not "
    elif char == "+":
        cmd += " or "
    elif char == ".":
        cmd += " and "
    else:
        cmd += char.upper()
    
cmd = cmd.strip()
for anInput in inputList:
    print(anInput + " ", end="")
print("Out")

combinations = [] # list of strings
for number in range(0, 2**len(inputList)):
    binary = bin(number)[2:]
    combinations.append("0"*(len(inputList)-len(binary)) + binary)
    
for combination in combinations:
    tempCmd = replace(cmd, inputList, combination)
    print(" ".join(combination), end="")
    print("  " + str(int(eval(tempCmd))))
    
    
    
    
        
