def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        for a in range(1, S[i]):
            for b in range(1, S[i]):
                if 4*a*b+3*a+3*b == S[i]:
                    count += 1
                    break
            else:
                continue
            break
    print(N-count)
