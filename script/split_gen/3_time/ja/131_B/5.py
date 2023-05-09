def main():
    N, L = map(int, input().split())
    apples = [L+i-1 for i in range(1, N+1)]
    eaten = apples.pop(apples.index(min(apples, key=abs)))
    print(sum(apples))
