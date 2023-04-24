Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = 21
    m = 0
    m = m + k
    if m > 59:
        h = h + m // 60
        m = m % 60
    if h > 23:
        h = h % 24
    if m < 10:
        print(str(h) + ":0" + str(m))
    else:
        print(str(h) + ":" + str(m))

=======
Suggestion 2

def main():
    k = int(input())
    h = 21
    m = 0
    m += k
    while m >= 60:
        m -= 60
        h += 1
    print(str(h) + ":" + str(m).zfill(2))

main()

=======
Suggestion 3

def main():
    k = int(input())
    h = 21 + k // 60
    m = k % 60
    print(f"{h:02}:{m:02}")

=======
Suggestion 4

def main():
    #Enter your code here. Read input from STDIN. Print output to STDOUT
    K = int(input())
    HH = 21
    MM = 0
    MM += K
    if MM >= 60:
        HH += MM // 60
        MM = MM % 60
    if HH >= 24:
        HH = HH % 24
    if HH < 10:
        HH = '0' + str(HH)
    if MM < 10:
        MM = '0' + str(MM)
    print(str(HH)+':'+str(MM))

=======
Suggestion 5

def main():
    k = int(input())
    hour = 21
    minute = 0
    total = k + minute
    hour += total // 60
    minute = total % 60
    print(str(hour) + ":" + str(minute).zfill(2))

=======
Suggestion 6

def time(k):
    hh = 21 + (k // 60)
    mm = k % 60
    if hh > 23:
        hh -= 24
    if mm < 10:
        mm = "0" + str(mm)
    return str(hh) + ":" + str(mm)

=======
Suggestion 7

def main():
    #write your code here
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    print(str(hour) + ":" + str(minute))

=======
Suggestion 8

def main():
    a = int(input())
    if a == 0:
        print("21:00")
    elif a >= 1 and a <= 60:
        print("21:%02d" % a)
    elif a >= 61 and a <= 99:
        print("22:%02d" % (a - 60))
    elif a == 100:
        print("22:40")

main()

The solution is pretty straight forward. You just need to make sure you follow the constraints. I used the %02d format to make sure that the output is always two digits. Otherwise, you will get an incorrect answer.

=======
Suggestion 9

def time_after_21_00(K):
    if K < 60:
        return '21:' + str(K).zfill(2)
    else:
        minutes = K % 60
        hours = (K // 60) + 21
        return str(hours) + ':' + str(minutes).zfill(2)

=======
Suggestion 10

def main():
    k = int(input())
    print("22:{}".format(k-60 if k>60 else k))
