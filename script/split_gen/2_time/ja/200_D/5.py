def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    for i in range(1 << N):
        x = [a for a, b in zip(A, format(i, 'b').zfill(N)) if b == '1']
        y = [a for a, b in zip(A, format(i, 'b').zfill(N)) if b == '0']
        if len(x) > 0 and len(y) > 0 and sum(x) % 200 == sum(y) % 200:
            print('Yes')
            print(len(x), *x)
            print(len(y), *y)
            break
    else:
        print('No')
