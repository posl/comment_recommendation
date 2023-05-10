def main():
    k = int(input())
    if k <= 9:
        print(k)
        return
    k -= 9
    cnt = 9
    for i in range(10, 10**9):
        if k <= cnt * 2:
            k -= 1
            s = str(i)
            print(s[k])
            return
        else:
            k -= cnt * 2
            cnt *= 10
