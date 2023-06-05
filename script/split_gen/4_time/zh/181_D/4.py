def main():
    s = input()
    a = [0] * 10
    for i in range(len(s)):
        a[int(s[i])] += 1
    if len(s) == 1:
        if int(s) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    elif len(s) == 3:
        if int(s) % 8 == 0 or int(s[1] + s[2] + s[0]) % 8 == 0 or int(s[2] + s[0] + s[1]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    elif len(s) == 4:
        if int(s) % 8 == 0 or int(s[1] + s[2] + s[3] + s[0]) % 8 == 0 or int(s[2] + s[3] + s[0] + s[1]) % 8 == 0 or int(s[3] + s[0] + s[1] + s[2]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    elif len(s) == 5:
        if int(s) % 8 == 0 or int(s[1] + s[2] + s[3] + s[4] + s[0]) % 8 == 0 or int(s[2] + s[3] + s[4] + s[0] + s[1]) % 8 == 0 or int(s[3] + s[4] + s[0] + s[1] + s[2]) % 8 == 0 or int(s[4] + s[0] + s[1] + s[2] + s[3]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    elif len(s) == 6:
