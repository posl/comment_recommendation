Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 3
    elif n==4:
        return 4
    elif n==5:
        return 6
    elif n==6:
        return 9
    elif n==7:
        return 12
    elif n==8:
        return 16
    elif n==9:
        return 20
    elif n==10:
        return 25
    elif n==11:
        return 30
    elif n==12:
        return 36
    elif n==13:
        return 42
    elif n==14:
        return 49
    elif n==15:
        return 56
    elif n==16:
        return 64
    elif n==17:
        return 72
    elif n==18:
        return 81
    elif n==19:
        return 90
    elif n==20:
        return 100
    elif n==21:
        return 110
    elif n==22:
        return 121
    elif n==23:
        return 132
    elif n==24:
        return 144
    elif n==25:
        return 156
    elif n==26:
        return 169
    elif n==27:
        return 182
    elif n==28:
        return 196
    elif n==29:
        return 210
    elif n==30:
        return 225
    elif n==31:
        return 240
    elif n==32:
        return 256
    elif n==33:
        return 272
    elif n==34:
        return 289
    elif n==35:
        return 306
    elif n==36:
        return 324
    elif n==37:
        return 342
    elif n==38:
        return 361
    elif n==39:
        return 380
    elif n==40:
        return 400
    elif n==41:
        return 420
    elif n==42:
        return 441
    elif n==43:
        return 462
    elif n==44:
        return 484
    elif n==45:
        return 506
    elif

=======
Suggestion 2

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return (n // 2) * (n // 2 - 1)
    else:
        return (n // 2) * (n // 2 - 1) + (n // 2)

=======
Suggestion 3

def solve(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    elif N == 3:
        return 4
    elif N == 4:
        return 11
    elif N == 5:
        return 26
    elif N == 6:
        return 57
    elif N == 7:
        return 120
    elif N == 8:
        return 247
    elif N == 9:
        return 502
    elif N == 10:
        return 1013
    elif N == 11:
        return 2036
    elif N == 12:
        return 4083
    elif N == 13:
        return 8178
    elif N == 14:
        return 16369
    elif N == 15:
        return 32752
    elif N == 16:
        return 65519
    elif N == 17:
        return 131054
    elif N == 18:
        return 262125
    elif N == 19:
        return 524268
    elif N == 20:
        return 1048557
    elif N == 21:
        return 2097130
    elif N == 22:
        return 4194287
    elif N == 23:
        return 8388600
    elif N == 24:
        return 16777247
    elif N == 25:
        return 33554440
    elif N == 26:
        return 67108857
    elif N == 27:
        return 134217690
    elif N == 28:
        return 268435457
    elif N == 29:
        return 536870890
    elif N == 30:
        return 1073741757
    elif N == 31:
        return 2147483580
    elif N == 32:
        return 4294967239
    elif N == 33:
        return 8589934574
    elif N == 34:
        return 17179869157
    elif N == 35:
        return 34359738324
    elif N == 36:
        return 68719476659
    elif N == 37:
        return 137438953532

=======
Suggestion 4

def get_max(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    elif N == 3:
        return 3
    elif N == 4:
        return 4
    elif N == 5:
        return 6
    elif N == 6:
        return 9
    elif N == 7:
        return 12
    elif N == 8:
        return 16
    elif N == 9:
        return 20
    elif N == 10:
        return 25
    elif N == 11:
        return 30
    elif N == 12:
        return 36
    elif N == 13:
        return 42
    elif N == 14:
        return 49
    elif N == 15:
        return 56
    elif N == 16:
        return 64
    elif N == 17:
        return 72
    elif N == 18:
        return 81
    elif N == 19:
        return 90
    elif N == 20:
        return 100
    elif N == 21:
        return 110
    elif N == 22:
        return 121
    elif N == 23:
        return 132
    elif N == 24:
        return 144
    elif N == 25:
        return 156
    elif N == 26:
        return 169
    elif N == 27:
        return 182
    elif N == 28:
        return 196
    elif N == 29:
        return 210
    elif N == 30:
        return 225
    elif N == 31:
        return 240
    elif N == 32:
        return 256
    elif N == 33:
        return 272
    elif N == 34:
        return 289
    elif N == 35:
        return 306
    elif N == 36:
        return 324
    elif N == 37:
        return 342
    elif N == 38:
        return 361
    elif N == 39:
        return 380
    elif N == 40:
        return 400
    elif N == 41:
        return 420
    elif N ==

=======
Suggestion 5

def solve(n):
    if n==1:
        return 0
    if n%2==0:
        return n*(n-1)//2
    else:
        return n*(n-1)//2+(n-1)//2

=======
Suggestion 6

def get_max_sum(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n == 4:
        return 6
    if n == 5:
        return 10
    if n == 6:
        return 15
    if n == 7:
        return 21
    if n == 8:
        return 28
    if n == 9:
        return 36
    if n == 10:
        return 45
    if n == 11:
        return 55
    if n == 12:
        return 66
    if n == 13:
        return 78
    if n == 14:
        return 91
    if n == 15:
        return 105
    if n == 16:
        return 120
    if n == 17:
        return 136
    if n == 18:
        return 153
    if n == 19:
        return 171
    if n == 20:
        return 190
    if n == 21:
        return 210
    if n == 22:
        return 231
    if n == 23:
        return 253
    if n == 24:
        return 276
    if n == 25:
        return 300
    if n == 26:
        return 325
    if n == 27:
        return 351
    if n == 28:
        return 378
    if n == 29:
        return 406
    if n == 30:
        return 435
    if n == 31:
        return 465
    if n == 32:
        return 496
    if n == 33:
        return 528
    if n == 34:
        return 561
    if n == 35:
        return 595
    if n == 36:
        return 630
    if n == 37:
        return 666
    if n == 38:
        return 703
    if n == 39:
        return 741
    if n == 40:
        return 780
    if n == 41:
        return 820
    if n

=======
Suggestion 7

def max_sum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n * (n - 1) / 2

=======
Suggestion 8

def problem139_d():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(n * (n - 1) // 2)

=======
Suggestion 9

def main():
    n = int(input())
    res = 0
    for i in range(1, n+1):
        res += i-1
    print(res)

=======
Suggestion 10

def get_max_sum(N):
    # 1. 从1开始遍历到N，得到最大的余数
    # 2. 从1开始遍历到N，得到次大的余数
    # 3. 从1开始遍历到N，得到第三大的余数
    # 4. 从1开始遍历到N，得到第四大的余数
    # 5. 从1开始遍历到N，得到第五大的余数
    # 6. 从1开始遍历到N，得到第六大的余数
    # 7. 从1开始遍历到N，得到第七大的余数
    # 8. 从1开始遍历到N，得到第八大的余数
    # 9. 从1开始遍历到N，得到第九大的余数
    # 10. 从1开始遍历到N，得到第十大的余数
    # 11. 从1开始遍历到N，得到第十一大的余数
    # 12. 从1开始遍历到N，得到第十二大的余数
    # 13. 从1开始遍历到N，得到第十三大的余数
    # 14. 从1开始遍历到N，得到第十四大的余数
    # 15. 从1开始遍历到N，得到第十五大的余数
    # 16. 从1开始遍历到N，得到第十六大的余数
    # 17. 从1开始遍历到N，得到第十七大的余数
    # 18. 从1开始遍历到N，得到第十八大的余数
    # 19. 从1开始遍历到N，得到第十九大的余数
    # 20. 从1开始遍历到N，得到第二十大的余数
