def main():
    s = input()
    k = int(input())
    # s = "XX...X.X.X."
    # k = 2
    # s = "XXXX"
    # k = 200000
    s = s.replace(".", "0")
    s = s.replace("X", "1")
    s = s.replace("0", "X")
    s = s.replace("1", "0")
    s = "0" + s + "0"
    count = 0
    max_count = 0
    for i in range(1, len(s)):
        if s[i] == "0":
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(max_count + k)
