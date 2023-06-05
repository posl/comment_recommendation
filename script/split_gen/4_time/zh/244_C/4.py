def main():
    N = int(input())
    A = list(range(1,2*N+2))
    B = []
    while True:
        a = int(input())
        if a == 0:
            break
        A.remove(a)
        b = A.pop()
        B.append(b)
        print(b)
        A.remove(b)
main()
