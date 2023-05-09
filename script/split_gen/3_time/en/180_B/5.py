def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(N)]))
    print((sum([x[i]**2 for i in range(N)]))**0.5)
    print(max([abs(x[i]) for i in range(N)]))
