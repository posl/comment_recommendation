def main():
    n = input()
    ans = -1
    for i in range(2**len(n)):
        tmp = ''
        for j in range(len(n)):
            if i & (1<<j):
                tmp += n[j]
        if tmp != '' and int(tmp)%3 == 0:
            if ans == -1:
                ans = len(n) - len(tmp)
            else:
                ans = min(ans, len(n) - len(tmp))
    print(ans)
