def main():
    N = int(input())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)

if __name__ == '__main__':
    main()