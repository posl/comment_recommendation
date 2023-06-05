def solve(N, K, AB):
    AB.sort(key=lambda x: x[0])
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    return K

if __name__ == '__main__':
    solve()