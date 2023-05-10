def main():
    s = input()
    k = int(input())
    s = s.replace('.', ' ')
    s = s.split()
    ans = 0
    for i in s:
        ans += len(i) - k
    print(ans)
