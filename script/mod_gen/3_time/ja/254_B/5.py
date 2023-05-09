def pascal(N):
    if N == 1:
        return [1]
    else:
        row = []
        for i in range(N):
            if i == 0 or i == N - 1:
                row.append(1)
            else:
                row.append(pascal(N-1)[i-1] + pascal(N-1)[i])
        return row
N = int(input())
for i in range(1, N+1):
    print(*pascal(i))

if __name__ == '__main__':
    pascal()