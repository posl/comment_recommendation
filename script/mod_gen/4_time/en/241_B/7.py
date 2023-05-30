def main():
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    n, m = 1, 1
    a = [1000000000]
    b = [1]
    if m > n:
        print('No')
    else:
        if len(set(b)) != len(b):
            print('No')
        else:
            for i in range(m):
                if b[i] not in a:
                    print('No')
                    break
            else:
                print('Yes')
main()
