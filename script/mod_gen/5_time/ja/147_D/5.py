def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    #print(n)
    #print(a_list)
    sum_list = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum_list.append(a_list[i] ^ a_list[j])
    #print(sum_list)
    print(sum(sum_list) % (10**9+7))

if __name__ == '__main__':
    main()