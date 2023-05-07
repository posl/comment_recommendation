def main():
    #Get the input
    n = int(input())
    #Check the range
    if -2147483648 <= n <= 2147483647:
        print("Yes")
    else:
        print("No")
