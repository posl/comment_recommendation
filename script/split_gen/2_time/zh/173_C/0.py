def main():
    num = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(num):
        s = input()
        if s == "AC":
            a += 1
        elif s == "WA":
            b += 1
        elif s == "TLE":
            c += 1
        elif s == "RE":
            d += 1
    print("AC x " + str(a))
    print("WA x " + str(b))
    print("TLE x " + str(c))
    print("RE x " + str(d))
