def main():
    N = int(input())
    x = list(map(int,input().split()))
    x_abs = [abs(x_i) for x_i in x]
    print(sum(x_abs))
    print(sum([x_i**2 for x_i in x_abs])**(1/2))
    print(max(x_abs))
