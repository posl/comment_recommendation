def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if L <= 0 and 0 <= L+N-1:
        print(sum(apple)-0)
    elif L < 0:
        print(sum(apple)-apple[0])
    else:
        print(sum(apple)-apple[-1])
