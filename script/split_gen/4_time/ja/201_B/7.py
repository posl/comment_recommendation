def main():
    N = int(input())
    mountain = []
    for _ in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: x[1], reverse=True)
    print(mountain[1][0])
