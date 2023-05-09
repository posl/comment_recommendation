def main():
    A,B,C = map(int,input().split())
    if A < 0 and C%2 == 0:
        A = abs(A)
    if B < 0 and C%2 == 0:
        B = abs(B)
    if A == B:
        print("=")
    elif A < B:
        print("<")
    else:
        print(">")
