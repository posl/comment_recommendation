def main():
    N = int(input())
    S = input()
    if S[0] == "0":
        for i in range(N):
            if S[i] == "1":
                if i % 2 == 0:
                    print("Takahashi")
                    return
                else:
                    print("Aoki")
                    return
    else:
        for i in range(N):
            if S[i] == "0":
                if i % 2 == 0:
                    print("Aoki")
                    return
                else:
                    print("Takahashi")
                    return
