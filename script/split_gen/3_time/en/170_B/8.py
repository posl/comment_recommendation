def main():
    #input
    X, Y = map(int, input().split())
    #output
    if (X*2 <= Y <= X*4):
        print("Yes")
    else:
        print("No")
