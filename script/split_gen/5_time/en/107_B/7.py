def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    a = [a[i] for i in range(h) if '#' in a[i]]
    a = [list(a[i]) for i in range(len(a)) if '#' in a[i]]
    for i in range(len(a)):
        print(''.join(a[i]))
