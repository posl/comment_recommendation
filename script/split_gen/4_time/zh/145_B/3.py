def main():
    N = int(input())
    S = input()
    T = S[:int(N/2)]
    if S == T + T:
        print("Yes")
    else:
        print("No")
