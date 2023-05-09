def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    print(sum([max(V[i]-C[i],0) for i in range(N)]))
