def war_or_peace():
    input1 = input("请输入N M X Y\n")
    input2 = input("请输入x_1 x_2 ... x_N\n")
    input3 = input("请输入y_1 y_2 ... y_M\n")
    input1 = input1.split()
    input2 = input2.split()
    input3 = input3.split()
    input1 = [int(i) for i in input1]
    input2 = [int(i) for i in input2]
    input3 = [int(i) for i in input3]
    x = input1[0]
    y = input1[1]
    N = input1[2]
    M = input1[3]
    input2.sort()
    input3.sort()
    if x < input2[0] and input2[0] < y and y <= input3[0]:
        print("无战争")
    else:
        print("战争")
war_or_peace()
