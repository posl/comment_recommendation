def main():
    s = input()
    cnt = [0] * 10
    for c in s:
        cnt[int(c)] += 1
    ans = "No"
    for i in range(1, 10):
        if cnt[i] == 0:
            continue
        cnt[i] -= 1
        for j in range(1, 10):
            if cnt[j] == 0:
                continue
            cnt[j] -= 1
            for k in range(1, 10):
                if cnt[k] == 0:
                    continue
                cnt[k] -= 1
                if (i*100+j*10+k) % 8 == 0:
                    ans = "Yes"
                cnt[k] += 1
            cnt[j] += 1
        cnt[i] += 1
    print(ans)

if __name__ == '__main__':
    main()