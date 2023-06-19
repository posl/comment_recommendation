def main():
    S, T = input().split()
    A, B = input().split()
    U = input()
    if S == U:
        print(int(A)-1, B)
    else:
        print(A, int(B)-1)
