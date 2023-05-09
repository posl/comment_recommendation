def main():
    x,y,n = map(int,input().split())
    m = n % 3
    if m == 0:
        print(n//3*y)
    elif m == 1:
        print(n//3*y+x)
    else:
        print(n//3*y+x+x)
main()
I am trying to make a program that will take a list of numbers and print out the numbers that are less than 5. I am new to python and am having trouble with the syntax. Any help would be appreciated.
