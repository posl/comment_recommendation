def main():
    n,k = map(int,input().split())
    h_list = []
    for i in range(n):
        h_list.append(int(input()))
    h_list.sort()
    min = h_list[0]
    max = h_list[k-1]
    for i in range(n-k):
        if h_list[i+k-1] - h_list[i] < max - min:
            min = h_list[i]
            max = h_list[i+k-1]
    print(max-min)

if __name__ == '__main__':
    main()