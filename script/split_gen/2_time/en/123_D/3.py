def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = sorted([a + b for a in A for b in B], reverse=True)
    ABC = sorted([ab + c for ab in AB[:K] for c in C], reverse=True)
    for i in range(K):
        print(ABC[i])
