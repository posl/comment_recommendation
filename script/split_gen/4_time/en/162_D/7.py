def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            for k in range(j+1, N):
                if S[i] == S[k] or S[j] == S[k]:
                    continue
                if j-i != k-j:
                    count += 1
    print(count)
