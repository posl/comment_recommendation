def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    count = 0
    while N != 1:
        N = P[N]
        count += 1
    print(count)
