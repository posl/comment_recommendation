def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            flag = True
            for k in range(i,j+1):
                if s[k] != "A" and s[k] != "C" and s[k] != "G" and s[k] != "T":
                    flag = False
            if flag:
                ans = max(ans,j-i+1)
    print(ans)
