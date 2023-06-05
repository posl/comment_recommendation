def main():
    s = input()
    k = int(input())
    cnt = 0
    for i in range(len(s)):
        if s[i] != '1':
            cnt += int(s[i]) - 1
            if cnt >= k:
                print(s[i])
                exit()
        else:
            cnt += 1
            if cnt >= k:
                print(1)
                exit()
    print(1)
