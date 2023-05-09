def main():
    S = input()
    ans = 0
    for i in range(10000):
        str_i = str(i).zfill(4)
        for j in range(10):
            if S[j] == 'o' and str(j) not in str_i:
                break
            if S[j] == 'x' and str(j) in str_i:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()