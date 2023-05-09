def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1
        l = len(s)
        if t % 3 == 1:
            print(s[k % l])
        elif t % 3 == 2:
            print(s[(k + l // 3) % l])
        else:
            print(s[(k + 2 * l // 3) % l])
