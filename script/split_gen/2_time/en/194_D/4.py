def main():
    n = int(input())
    print(sum([i * (1/n)**i for i in range(1, n+1)]))
