def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum([abs(i) for i in a]))
    else:
        print(sum([abs(i) for i in a]) - 2 * abs(a[0]))
