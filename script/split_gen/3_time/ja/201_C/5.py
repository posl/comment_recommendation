def main():
    S = input()
    ans = 0
    for i in range(10000):
        num = str(i).zfill(4)
        for j in range(4):
            if S[int(num[j])] == 'o' and num[j] != str(j):
                break
            if S[int(num[j])] == 'x' and num[j] == str(j):
                break
        else:
            ans += 1
    print(ans)
main()
