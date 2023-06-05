def main():
    input1 = input().split()
    input2 = input().split()
    n = int(input1[0])
    x = int(input1[1])
    sum = 0
    for i in range(n):
        if i%2 == 0:
            sum += int(input2[i])
        else:
            sum += int(input2[i]) - 1
    if sum <= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()