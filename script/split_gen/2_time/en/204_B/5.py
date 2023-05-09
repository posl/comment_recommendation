def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([max(0, a - 10) for a in A]))
