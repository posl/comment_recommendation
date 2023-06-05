def main():
    n = int(input())
    mountain = []
    for i in range(n):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
