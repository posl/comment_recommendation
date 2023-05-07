def main():
    N = int(input())
    S = input()
    T = S[:N//2]
    if N%2 == 1:
        print("No")
        return
    if S == T + T:
        print("Yes")
    else:
        print("No")
