def main():
    N = int(input())
    declared = set()
    for i in range(1, N+1):
        print(i)
        print(i+N+1)
        declared.add(i)
        declared.add(i+N+1)
        aoki = int(input())
        if aoki == 0:
            return
        declared.add(aoki)
    print(N+1)
    print(0)
main()
