def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n //= -2
        else:
            ans.append(1)
            n = (n-1) // -2
    ans.reverse()
    print(''.join(map(str, ans)))
