def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    #print(A)
    c = [0]*200
    for a in A:
        c[a] += 1
    #print(c)
    ans = 0
    for i in range(200):
        ans += c[i]*(c[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()