def main():
    n, l = map(int, input().split())
    apple = []
    for i in range(1, n+1):
        apple.append(l+i-1)
    print(sum(apple)-min(apple, key=abs))
