def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for c in C:
        for ab in AB[:K]:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])