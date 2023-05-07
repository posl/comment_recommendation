def main():
    s = input()
    s_len = len(s)
    count = 0
    for i in range(s_len):
        for j in range(i+3, s_len+1):
            if int(s[i:j]) % 2019 == 0:
                count += 1
    print(count)
