def main():
    k = int(input())
    h = 21
    m = 0
    while k > 0:
        if m == 60:
            h += 1
            m = 0
        k -= 1
        m += 1
    print(str(h).zfill(2) + ":" + str(m).zfill(2))
