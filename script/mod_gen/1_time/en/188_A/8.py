def main():
    # Write your code here
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if (X - Y) > 2:
        print("Yes")
    else:
        print("No")
main()
What is the difference between print("Yes") and print("Yes", end="")?
print("Yes") will print Yes and then move to the next line. print("Yes", end="") will print Yes and then move the cursor to the beginning of the same line. The end="" parameter is optional. If you don’t specify it, the default value is end="
", which is a new line.
What is the difference between print("Yes", end="") and print("Yes", end="
")?
print("Yes", end="") will print Yes and then move the cursor to the beginning of the same line. print("Yes", end="
") will print Yes and then move to the next line. The end="" parameter is optional. If you don’t specify it, the default value is end="
", which is a new line.
What is the difference between print("Yes", end="") and print("Yes", end=" ")?
print("Yes", end="") will print Yes and then move the cursor to the beginning of the same line. print("Yes", end=" ") will print Yes and then move the cursor to the beginning of the next line. The end="" parameter is optional. If you don’t specify it, the default value is end="
", which is a new line.
What is the difference between print("Yes", end="") and print("Yes", end=None)?
print("Yes", end="") will print Yes and then move the cursor to the beginning of the same line. print("Yes", end=None) will print Yes and then move to the next line. The end="" parameter is optional. If you don’t specify it, the default value is end="
", which is a new line.
What is the difference between print("Yes", end="") and print("Yes", end="")?
print("Yes", end="") will print Yes and then move the cursor to the beginning of the same line. print("Yes", end="") will print Yes and then move to the next line. The end="" parameter is optional. If you don’t specify it, the default

if __name__ == '__main__':
    main()