def main():
    N, A, B = map(int, input().split())
    ans = []
    for i in range(A*N):
        ans.append([])
        for j in range(B*N):
            if (i//A+j//B)%2 == 0:
                ans[i].append('.')
            else:
                ans[i].append('#')
    for i in range(A*N):
        print(''.join(ans[i]))

if __name__ == '__main__':
    main()