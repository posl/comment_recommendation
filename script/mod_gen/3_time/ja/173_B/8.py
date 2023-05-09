def main():
    n = int(input())
    s = [input() for i in range(n)]
    s_count = [0,0,0,0]
    for i in range(n):
        if s[i] == "AC":
            s_count[0] += 1
        elif s[i] == "WA":
            s_count[1] += 1
        elif s[i] == "TLE":
            s_count[2] += 1
        elif s[i] == "RE":
            s_count[3] += 1
    print("AC x " + str(s_count[0]))
    print("WA x " + str(s_count[1]))
    print("TLE x " + str(s_count[2]))
    print("RE x " + str(s_count[3]))

if __name__ == '__main__':
    main()