#!/usr/bin/env python3

def operate(n1, n2, operation):
    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        result = n1 / n2
    
    return result

def main():
    n1 = input("First number: ")
    n2 = input("Second number: ")
    
    n1 = int(n1)
    n2 = int(n2)
    
    operation = input("Operation (+,-,*,/): ")
    
    result = operate(n1, n2, operation)
    print(result)
    

if __name__ == "__main__":
    main()
