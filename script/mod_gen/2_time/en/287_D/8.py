def solve():
    s = list(input())
    t = list(input())
    for i in range(len(t)+1):
        if s[i:i+len(t)] == t or s[i:i+len(t)] == ['?']*len(t):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()