def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(list(input().split()))
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])
