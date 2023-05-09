def main():
    #read the input
    A, B, C = map(int, input().split())
    #calculate the number of times
    if A * C > B:
        print(B // A)
    else:
        print(C)
