def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    happy = 0
    for i in range(N):
        if p[i] == (p[(i-1)%N]+1)%N or p[i] == (p[(i+1)%N]-1)%N:
            happy += 1
    print(happy)

if __name__ == '__main__':
    main()