def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain = sorted(mountain, key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
