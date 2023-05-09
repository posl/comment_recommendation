def main():
    s = input()
    atcoder = "atcoder"
    count = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            count += 1
    print(count)
