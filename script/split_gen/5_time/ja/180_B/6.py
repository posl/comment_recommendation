def main():
    N = int(input())
    x = list(map(int,input().split()))
    x = [abs(x[i]) for i in range(N)]
    print(sum(x))
    print(sum([x[i]**2 for i in range(N)])**0.5)
    print(max(x))
