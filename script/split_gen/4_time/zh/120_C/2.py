def main():
    s = input()
    n = len(s)
    red = [0] * (n + 1)
    blue = [0] * (n + 1)
    for i in range(n):
        red[i+1] = red[i] + (s[i] == "0")
        blue[i+1] = blue[i] + (s[i] == "1")
    ans = 0
    for i in range(n):
        ans = max(ans, red[i] + blue[n] - blue[i])
    print(ans)
