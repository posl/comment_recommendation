def main():
    N = int(input())
    cities = [0 for i in range(N+1)]
    for i in range(N-1):
        A, B = map(int, input().split())
        cities[A] += 1
        cities[B] += 1
    for i in range(1, N+1):
        print(cities[i], end=' ')
