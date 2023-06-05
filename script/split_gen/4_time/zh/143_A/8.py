def main():
    A,B = map(int,input().split())
    if A < B:
        print(0)
    else:
        print(A-2*B)
