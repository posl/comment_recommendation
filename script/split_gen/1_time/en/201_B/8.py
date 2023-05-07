def main():
    mountain = []
    N = int(input())
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
