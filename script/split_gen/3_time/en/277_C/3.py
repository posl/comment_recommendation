def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    print(ladders[-1][1])
