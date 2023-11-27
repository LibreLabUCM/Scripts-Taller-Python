#!/usr/bin/env python3

def main():
    with open("test.txt") as my_file:
        line = my_file.readline().strip()
        while line:
            print(line)
            line = my_file.readline().strip()

if __name__ == "__main__":
    main()
