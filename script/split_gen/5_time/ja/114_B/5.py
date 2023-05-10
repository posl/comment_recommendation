def main():
    s = input()
    ans = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < ans:
            ans = abs(x-753)
    print(ans)
