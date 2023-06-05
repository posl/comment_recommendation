def solve():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    left = []
    right = []
    for i in range(N):
        if S[i] == 'L':
            left.append(i)
        else:
            right.append(i)
    left.sort(key=lambda x: X[x])
    right.sort(key=lambda x: X[x])
    for i in range(len(left)):
        left[i] = N - 1 - left[i]
    for i in range(len(right)):
        right[i] = N - 1 - right[i]
    for i in range(len(left) - 1):
        if Y[left[i]] > Y[left[i + 1]]:
            print('Yes')
            return
    for i in range(len(right) - 1):
        if Y[right[i]] > Y[right[i + 1]]:
            print('Yes')
            return
    for i in range(len(left)):
        for j in range(len(right)):
            if X[left[i]] == X[right[j]]:
                if Y[left[i]] > Y[right[j]]:
                    print('Yes')
                    return
                else:
                    break
            elif X[left[i]] < X[right[j]]:
                break
    print('No')

if __name__ == '__main__':
    solve()