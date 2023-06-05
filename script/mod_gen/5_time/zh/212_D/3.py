def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    bag = []
    for i in range(n):
        if arr[i][0] == 1:
            bag.append(arr[i][1])
        elif arr[i][0] == 2:
            for j in range(len(bag)):
                bag[j] += arr[i][1]
        else:
            print(min(bag))
            bag.remove(min(bag))

if __name__ == '__main__':
    main()