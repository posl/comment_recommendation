def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
                return
            else:
                print("Aoki")
                return
