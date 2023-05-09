def main():
    print('Start')
    print('Enter number of elements in list')
    n = int(input())
    print('Enter the elements of the list')
    a = list(map(int,input().split()))
    print('Enter number of operations')
    q = int(input())
    print('Enter the elements of the list')
    b = []
    c = []
    for i in range(q):
        b.append(int(input()))
        c.append(int(input()))
    print('The list of sums after each operation is:')
    for i in range(q):
        a = [c[i] if j==b[i] else j for j in a]
        print(sum(a))
    print('End')

if __name__ == '__main__':
    main()