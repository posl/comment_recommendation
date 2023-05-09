def main():
    N, A, B = map(int, input().split())
    ans = []
    for i in range(A*N):
        ans.append([])
        for j in range(B*N):
            ans[i].append('.')
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 0:
                for k in range(A):
                    for l in range(B):
                        ans[A*i+k][B*j+l] = '#'
    for i in range(A*N):
        print(''.join(ans[i]))

if __name__ == '__main__':
    main()