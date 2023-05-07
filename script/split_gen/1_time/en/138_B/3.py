def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    print(1/sum([1/a for a in A]))
