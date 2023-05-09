def main():
    N = int(input())
    S = input()
    T = S[:N//2]
    U = S[N//2:]
    if T == U:
        print("Yes")
    else:
        print("No")
