def main():
    # Get the number of people
    n = int(input())
    # Get the family and given names
    names = [input().split() for _ in range(n)]
    # Check if there are any duplicated names
    for i in range(n):
        for j in range(i+1, n):
            if names[i] == names[j]:
                print('Yes')
                return
    # If there are no duplicated names, print 'No'
    print('No')
    return

if __name__ == '__main__':
    main()