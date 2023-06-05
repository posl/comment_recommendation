def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(A)
    A200 = [i%200 for i in A]
    #print(A200)
    A200_dict = {}
    for i in A200:
        if i in A200_dict:
            A200_dict[i] += 1
        else:
            A200_dict[i] = 1
    #print(A200_dict)
    sum = 0
    for i in A200_dict.keys():
        sum += A200_dict[i]*(A200_dict[i]-1)//2
    print(sum)

if __name__ == '__main__':
    main()