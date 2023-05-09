def main():
    N = int(input())
    L = list(range(1, 2*N+2))
    for i in range(N):
        print(L.pop(0))
        print(L.pop(-1))
        a = int(input())
        if a == 0:
            break
        b = int(input())
        if b == 0:
            break
        L.remove(a)
        L.remove(b)
