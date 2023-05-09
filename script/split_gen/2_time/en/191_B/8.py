def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    print(' '.join(list(map(str, filter(lambda x: x != n, a)))))
