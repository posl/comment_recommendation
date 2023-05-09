def problem173_b():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    print("AC x " + str(s_list.count("AC")))
    print("WA x " + str(s_list.count("WA")))
    print("TLE x " + str(s_list.count("TLE")))
    print("RE x " + str(s_list.count("RE")))
