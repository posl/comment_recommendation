def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print((sum(map(lambda i: i*i, x)))**(1/2))
    print(max(map(abs, x)))
