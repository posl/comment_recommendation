def main():
    A, B = map(int, input().split())
    #print(A, B)
    if A > B:
        print(0)
    else:
        print(B - A + 1)
