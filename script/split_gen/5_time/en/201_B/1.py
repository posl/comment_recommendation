def main():
    n = int(input())
    mountains = []
    for _ in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])
