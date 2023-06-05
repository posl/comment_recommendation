def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    print(AB)
