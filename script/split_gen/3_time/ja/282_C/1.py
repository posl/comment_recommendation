def main():
    N = int(input())
    S = list(input())
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
            if cnt % 2 == 0:
                S[i] = "."
    print("".join(S))
