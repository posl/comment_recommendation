def main():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            count += 1
            a[i] /= 2
    print(count)
