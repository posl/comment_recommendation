def main():
    n = int(input())
    ai = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if ai[i] > 10:
            sum += ai[i] - 10
    print(sum)
