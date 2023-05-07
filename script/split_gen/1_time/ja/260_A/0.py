def main():
    s = input()
    ans = -1
    for i in s:
        if s.count(i) == 1:
            ans = i
            break
    print(ans)
