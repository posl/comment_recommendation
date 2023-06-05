def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a
    a_sum = sum(a)
    if a_sum%200 == 0:
        print('Yes')
        print(1,1)
        print(1,2)
    else:
        print('No')

if __name__ == '__main__':
    main()