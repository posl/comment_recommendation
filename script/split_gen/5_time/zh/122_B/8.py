def main():
    s = input()
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if (j-i) > max_len and check(s[i:j]):
                max_len = j-i
    print(max_len)
