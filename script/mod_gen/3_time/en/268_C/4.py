def main():
    N = int(input())
    p = list(map(int, input().split()))
    happy = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == i or p[i] == (i+1)%N:
            happy += 1
    print(happy)

if __name__ == '__main__':
    main()