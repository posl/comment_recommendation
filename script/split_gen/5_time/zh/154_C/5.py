def main():
    n = int(input())
    a = input().split()
    b = set(a)
    if len(b) == n:
        print('YES')
    else:
        print('NO')
