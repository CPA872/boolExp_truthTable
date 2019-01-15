# Release v1.1
# v1.1 eliminated the use of a redundant list
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
inputList = []
cmd = "" # translate userinput into python command to be executed
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
# the headings
for anInput in inputList: 
    print(anInput + " ", end="")
print("Out")

for number in range(0, 2**len(inputList)):
    binary = bin(number)[2:]
    combination = "0" * (len(inputList) - len(binary)) + binary
    tempCmd = replace(cmd, inputList, combination)
    print(" ".join(combination), end="")
    print("  " + str(int(eval(tempCmd))))
    
    
    
    
        
