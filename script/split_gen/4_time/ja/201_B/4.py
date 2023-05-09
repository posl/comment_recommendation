def main():
    n = int(input())
    mountains = [input().split() for _ in range(n)]
    mountains.sort(key=lambda x:int(x[1]), reverse=True)
    print(mountains[1][0])
