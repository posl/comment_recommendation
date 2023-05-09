def main():
    X, Y, Z, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])
