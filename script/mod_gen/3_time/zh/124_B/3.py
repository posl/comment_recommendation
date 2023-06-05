def main():
    N = int(input())
    H = input().split()
    H = [int(i) for i in H]
    count = 0
    for i in range(1,N+1):
        if i == 1:
            count += 1
        else:
            flag = True
            for j in range(1,i):
                if H[j-1] > H[i-1]:
                    flag = False
            if flag:
                count += 1
    print(count)

if __name__ == '__main__':
    main()