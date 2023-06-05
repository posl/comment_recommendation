def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        if (S[i] % 2 == 0):
            count += 1
    print(count)
