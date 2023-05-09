def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = sorted([a + b for a in A for b in B], reverse = True)[:K]
    ABC = sorted([a + b for a in AB for b in C], reverse = True)[:K]
    print('\n'.join(map(str, ABC)))
