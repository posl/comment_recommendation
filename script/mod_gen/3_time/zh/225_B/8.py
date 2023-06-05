def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    ans = 'No'
    for i in range(1, N+1):
        if i == 1:
            for j in range(N-1):
                if ab[j][0] == i:
                    ans = 'Yes'
                    break
        else:
            for j in range(N-1):
                if ab[j][0] == i:
                    ans = 'No'
                    break
        if ans == 'No':
            break
    print(ans)
main()
