def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("No")
    else:
        T = S[:N//2]
        if T + T == S:
            print("Yes")
        else:
            print("No")
