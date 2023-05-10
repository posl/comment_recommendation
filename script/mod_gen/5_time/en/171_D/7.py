def main():
    # Get number of elements in the list
    n = int(input())
    # Get the list
    a = list(map(int, input().split()))
    # Get number of operations to be performed
    q = int(input())
    # Get the list of operations
    b = list()
    c = list()
    for i in range(q):
        b.append(int(input()))
        c.append(int(input()))
    # Perform the operations
    for i in range(q):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]
        print(sum(a))

if __name__ == '__main__':
    main()