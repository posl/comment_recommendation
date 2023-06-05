def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("是")
        else:
            print("否")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(s) == 3:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0 or int(s[2] + s[1] + s[0]) % 8 == 0 or int(s[1] + s[0] + s[2]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(s) >= 4:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("是")
            return
        for i in range(100, 1000):
            if i % 8 == 0:
                if str(i)[0] in s and str(i)[1] in s and str(i)[2] in s:
                    print("是")
                    return
        print("否")
