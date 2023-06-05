def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)
    words.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if words[i] == words[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
