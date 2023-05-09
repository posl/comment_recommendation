def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            print("Aoki" if i % 2 == 0 else "Takahashi")
            break
