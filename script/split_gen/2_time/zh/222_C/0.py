def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    print(sum([1 if P > a else 0 for a in A]))
