def main():
    import sys
    import bisect
    input = sys.stdin.readline
    n = int(input())
    a = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            bisect.insort_left(a, int(query[1]))
        elif query[0] == '2':
            for _ in range(min(int(query[2]), a.count(int(query[1])))):
                a.remove(int(query[1]))
        else:
            print(a[-1] - a[0])
