def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        count = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                count += 1
        print(count)
