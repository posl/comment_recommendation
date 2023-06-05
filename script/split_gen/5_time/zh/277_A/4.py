def main():
    n, x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    for i in range(n):
        if p[i] == x:
            print i + 1
            break
