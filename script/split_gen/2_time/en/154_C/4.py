def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) != len(set(A)):
        print('NO')
    else:
        print('YES')
