def main():
    S = input()
    #print(S)
    num = []
    for i in S:
        num.append(int(i))
    #print(num)
    if len(num) == 1:
        if num[0] == 8:
            print("Yes")
        else:
            print("No")
    elif len(num) == 2:
        if num[0] == 8 or num[1] == 8:
            print("Yes")
        else:
            if (num[0]*10 + num[1]) % 8 == 0:
                print("Yes")
            else:
                print("No")
    else:
        count = [0] * 10
        for i in num:
            count[i] += 1
        #print(count)
        for i in range(112, 1000, 8):
            c = [0] * 10
            for j in str(i):
                c[int(j)] += 1
            #print(c)
            flag = True
            for j in range(10):
                if count[j] < c[j]:
                    flag = False
                    break
            if flag:
                print("Yes")
                return
        print("No")
main()
