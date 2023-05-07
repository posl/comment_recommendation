def main():
    N = int(input())
    ans = 0
    #桁数を求める
    digit = 0
    while 10**digit <= N:
        digit += 1
    #print(digit)
    #各桁の数を求める
    digit_num = [0]*digit
    for i in range(digit):
        digit_num[i] = (N//10**(i+1))*10**i + max(0, N%10**i+1-10**i)
    #print(digit_num)
    #各桁の数の総和を求める
    digit_total = [0]*digit
    for i in range(digit):
        if i == 0:
            digit_total[i] = digit_num[i]
        else:
            digit_total[i] = digit_total[i-1] + digit_num[i]
    #print(digit_total)
    #答えを求める
    for i in range(digit):
        if i == 0:
            ans += digit_total[i]
        else:
            ans += digit_total[i]*2
    print(ans)
