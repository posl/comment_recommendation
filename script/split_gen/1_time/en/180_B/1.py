def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(abs(i) for i in x))
    print((sum(i**2 for i in x))**0.5)
    print(max(abs(i) for i in x))
