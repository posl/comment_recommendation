def main():
    S = input()
    K = int(input())
    i = 0
    while i < K:
        if S[i] != "1":
            break
        i += 1
    print(S[i])
