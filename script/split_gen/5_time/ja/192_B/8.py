def main():
    s = input()
    ans = 'Yes'
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower() == False:
                ans = 'No'
                break
        else:
            if s[i].isupper() == False:
                ans = 'No'
                break
    print(ans)
