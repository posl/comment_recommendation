def solve(n):
    ans = []
    while n != 0:
        if n % 2 == 0:
            n //= 2
            ans.append('B')
        else:
            n -= 1
            ans.append('A')
    return ans[::-1]
n = int(input())
print(''.join(solve(n)))

if __name__ == '__main__':
    solve()