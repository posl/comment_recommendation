def main():
    a = map(int, raw_input().split())
    cnt = 0
    while cnt < 3:
        cnt += 1
        a = a[a[0]]
    print a[0]
