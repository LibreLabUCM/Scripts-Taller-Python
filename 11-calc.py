#!/usr/bin/env python3

def operate(n1, n2, operation):
    
    n1 = int(n1)
    n2 = int(n2)
    
    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        if n2 == 0:
            raise Exception("Can not divide by zero")
        result = n1 / n2
    else:
        raise Exception("Unknown operation")
    
    return result

def main():
    n1 = input("First number: ")
    n2 = input("Second number: ")
    
    operation = input("Operation (+,-,*,/): ")
    
    try:
        result = operate(n1, n2, operation)
        print(result)
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()
