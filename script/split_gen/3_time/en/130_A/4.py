def main():
    #X and A are integers between 0 and 9 (inclusive).
    #If X is less than A, print 0; if X is not less than A, print 10.
    inp = input().split()
    X = int(inp[0])
    A = int(inp[1])
    if X < A:
        print(0)
    else:
        print(10)
