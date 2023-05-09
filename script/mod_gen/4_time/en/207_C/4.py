def get_input():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    return intervals

if __name__ == '__main__':
    get_input()