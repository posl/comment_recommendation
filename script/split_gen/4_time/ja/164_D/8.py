def main():
    s = input()
    n = len(s)
    ans = 0
    mod = 2019
    mod_list = [0] * mod
    mod_list[0] = 1
    num = 0
    for i in range(n):
        num = (num + int(s[n - 1 - i]) * pow(10, i, mod)) % mod
        ans += mod_list[num]
        mod_list[num] += 1
    print(ans)
