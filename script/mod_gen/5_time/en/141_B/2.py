def solve():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                return 'No'
        else:
            if S[i] == 'R':
                return 'No'
    return 'Yes'
print(solve())

if __name__ == '__main__':
    solve()