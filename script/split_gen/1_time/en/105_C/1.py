def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N != 0:
        if N % 2 == 0:
            ans.append(0)
            N //= -2
        else:
            ans.append(1)
            N = (N - 1) // -2
    print(''.join(map(str, ans[::-1])))
