#!/usr/bin/env python3

def main():
    file1 = open("test.txt","w")
    file1.write("Hello World\n")
    file1.close()
    
    file2 = open("test.txt","a")
    file2.write("Hello World 2\n")
    file2.close()
    
    file3 = open("test.txt","r")
    line = file3.readline()
    file3.close()
    print(line)
    

if __name__ == "__main__":
    main()
