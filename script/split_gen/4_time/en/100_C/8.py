def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([bin(a).count('1') for a in A]))
