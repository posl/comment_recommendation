def main():
    s = input()
    k = int(input())
    l = len(s)
    if k <= l:
        print(s[k-1])
        exit()
    i = 0
    while True:
        if 2**i >= k:
            break
        i += 1
    print(s[i-1])
main()
