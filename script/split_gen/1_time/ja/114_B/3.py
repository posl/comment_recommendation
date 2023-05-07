def main():
    s = input()
    ans = 1000
    for i in range(len(s) - 2):
        x = abs(753 - int(s[i:i + 3]))
        if x < ans:
            ans = x
    print(ans)
