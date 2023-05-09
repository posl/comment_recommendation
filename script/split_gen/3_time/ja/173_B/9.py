def main():
    #入力
    n = int(input())
    s = [input() for i in range(n)]
    #AC,WA,TLE,REのカウント
    count = [0,0,0,0]
    for i in s:
        if i == "AC":
            count[0] += 1
        elif i == "WA":
            count[1] += 1
        elif i == "TLE":
            count[2] += 1
        elif i == "RE":
            count[3] += 1
    #出力
    print("AC x " + str(count[0]))
    print("WA x " + str(count[1]))
    print("TLE x " + str(count[2]))
    print("RE x " + str(count[3]))
