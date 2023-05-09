def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    t = int(readline())
    for _ in range(t):
        a, s = map(int, readline().split())
        if a > s:
            print("No")
            continue
        elif a == s:
            print("Yes")
            continue
        else:
            if (s - a) & 1:
                print("No")
                continue
            else:
                print("Yes")
                continue
