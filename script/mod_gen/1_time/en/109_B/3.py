def solve():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    for i in range(N-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True

if __name__ == '__main__':
    solve()