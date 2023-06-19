def main():
    k = int(input())
    h = 21
    m = 0
    if k >= 60:
        h = h + k // 60
        m = k % 60
    else:
        m = k
    if h >= 24:
        h = h - 24
    if h < 10:
        if m < 10:
            print("0" + str(h) + ":" + "0" + str(m))
        else:
            print("0" + str(h) + ":" + str(m))
    else:
        if m < 10:
            print(str(h) + ":" + "0" + str(m))
        else:
            print(str(h) + ":" + str(m))
