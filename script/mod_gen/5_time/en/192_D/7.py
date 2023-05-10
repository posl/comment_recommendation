def base_n(x, n):
    ans = 0
    for i in range(len(x)):
        ans += int(x[-i-1]) * pow(n, i)
    return ans
x = input()
m = int(input())

if __name__ == '__main__':
    base_n()