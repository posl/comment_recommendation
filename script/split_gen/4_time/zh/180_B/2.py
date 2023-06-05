def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(x[i]) for i in range(N)]
    print(sum(x_abs))
    print(sum(map(lambda x:x*x, x_abs))**0.5)
    print(max(x_abs))
