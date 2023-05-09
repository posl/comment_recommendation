def main():
    n = int(input())
    print(n + sum([1/i for i in range(2, n)]))
