def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x_i) for x_i in x]))
    print((sum([x_i**2 for x_i in x]))**(1/2))
    print(max([abs(x_i) for x_i in x]))
