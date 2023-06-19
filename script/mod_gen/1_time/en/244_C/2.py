def main():
    N = int(input())
    declared = set()
    for i in range(1, 2*N+1):
        print(i)
        declared.add(i)
        a = int(input())
        if a == 0:
            return
        declared.add(a)
    return
main()
