def main():
    s = input()
    k = int(input())
    cnt = 0
    for i in range(len(s)):
        if s[i] != "1":
            cnt += 1
            if cnt == k:
                print(s[i])
                return
        else:
            cnt = 0
            if cnt == k:
                print(1)
                return
    print(1)
    return
