def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = [A[i] + B[j] for i in range(X) for j in range(Y)]
    AB.sort(reverse=True)
    ABC = [AB[i] + C[j] for i in range(min(X*Y, K)) for j in range(Z)]
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])
