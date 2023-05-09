def main():
    N, X = map(int, input().split())
    for i in range(N):
        a, b = map(int, input().split())
        if a <= X <= b:
            print('Yes')
            break
    else:
        print('No')
