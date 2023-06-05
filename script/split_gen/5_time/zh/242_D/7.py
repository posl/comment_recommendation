def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        for j in range(t):
            k = (k + 1) % len(s)
            if s[k] == "a":
                s = s[:k] + "bc" + s[k+1:]
            elif s[k] == "b":
                s = s[:k] + "ca" + s[k+1:]
            else:
                s = s[:k] + "ab" + s[k+1:]
        print(s[k])
