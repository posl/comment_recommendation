def main():
    N = int(input())
    sum = 0
    for i in range(0, N):
        a, b = map(int, input().split())
        sum += (b-a+1)*(a+b)//2
    print(sum)

if __name__ == '__main__':
    main()