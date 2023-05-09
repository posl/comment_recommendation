def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum(map(lambda x,y: x*y, A, B)) + C > 0:
            count += 1
    print(count)
