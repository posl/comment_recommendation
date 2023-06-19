def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N != 0:
        if N % -2 == 0:
            ans.append(0)
            N = N // -2
        else:
            ans.append(1)
            N = N // -2 + 1
    ans.reverse()
    print(''.join([str(a) for a in ans]))
main()
