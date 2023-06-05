def main():
    n = int(input())
    d_list = [int(i) for i in input().split()]
    d_list.sort()
    #print(d_list)
    #print(d_list[n//2])
    print(d_list[n//2]-d_list[n//2-1])

if __name__ == '__main__':
    main()