def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) != n:
        print('NO')
    else:
        print('YES')
main()
