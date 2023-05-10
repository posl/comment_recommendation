def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    count += 1
    print(count)
