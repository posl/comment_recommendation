def main():
    a = map(int, raw_input().split())
    i = 0
    while i < 3:
        a = a[a[i]]
        i += 1
    print a
