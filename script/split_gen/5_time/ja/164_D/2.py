def main():
    s = input()
    mod = 2019
    s_len = len(s)
    count = 0
    for i in range(s_len):
        for j in range(i+1,s_len):
            if int(s[i:j+1]) % mod == 0:
                count += 1
    print(count)
