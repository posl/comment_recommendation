def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            count += 1
    print(count)
