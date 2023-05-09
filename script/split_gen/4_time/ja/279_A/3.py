def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            count += 1
    print(count * (count - 1) // 2)
