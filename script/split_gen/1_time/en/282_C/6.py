def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("error")
        return
    cnt = 0
    for i in range(N):
        if S[i] == "\"":
            cnt += 1
        if S[i] == "," and cnt % 2 == 0:
            S = S[:i] + "." + S[i+1:]
    print(S)
