def main():
    N = int(input())
    S = list(map(int, input().split()))
    if sum(S) % 10 != 0:
        print("Yes")
        return
    for i in range(N):
        if S[i] % 10 != 0:
            print("Yes")
            return
    print("No")
