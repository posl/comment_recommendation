def main():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        if m == 59:
            h += 1
            m = 0
        else:
            m += 1
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    print(h + ":" + m)
