def main():
    N = int(input())
    mountain = [input().split() for _ in range(N)]
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
