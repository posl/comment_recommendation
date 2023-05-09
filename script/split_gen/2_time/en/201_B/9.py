def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key = lambda x: int(x[1]))
    print(mountain[N-2][0])
