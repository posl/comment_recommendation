def main():
    #input
    A,B = map(int,input().split())
    #output
    if A*B%2 == 0:
        print("No")
    else:
        print("Yes")
