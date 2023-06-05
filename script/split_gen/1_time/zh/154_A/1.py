def main():
    S,T = input().split()
    A,B = input().split()
    U = input()
    if S == U:
        A = int(A) - 1
    elif T == U:
        B = int(B) - 1
    print(A,B)
