def main():
    n, a, b = map(int, input().split())
    print(sum([i for i in range(1, n+1) if (i%a)*(i%b)!=0]))
