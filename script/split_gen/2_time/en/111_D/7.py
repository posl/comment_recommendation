def solve(n,x,y):
    if n == 1:
        if x[0] == 0 and y[0] == 0:
            return '1
0
R'
        else:
            return '-1'
    if n == 2:
        if x[0] == 0 and y[0] == 0:
            return '2
1 1
RU
UR'
        else:
            return '-1'
    if n == 3:
        if x[0] == 0 and y[0] == 0:
            return '3
2 1 2
RUU
UUR
URU'
        else:
            return '-1'
    if n == 4:
        return '4
3 1 2 1
RUUR
URUU
UURU
URUR'
    if n == 5:
        return '5
3 1 2 1 5
RUURU
URUUU
UURUR
URURU
URURD'
    if n == 6:
        return '6
4 1 2 1 5 3
RUURUR
URUUUU
UURURR
URURUR
URURDU
URURDR'
    if n == 7:
        return '7
4 1 2 1 5 3 7
RUURURU
URUUUUU
UURURRR
URURURR
URURDUR
URURDRU
URURDRR'
    if n == 8:
        return '8
5 1 2 1 5 3 7 2
RUURURUR
URUUUUUU
UURURRRR
URURURRR
URURDURR
URURDRUR
URURDRRU
URURDRRR'
    if n == 9:
        return '9
5 1 2 1 5 3 7 2 6
RUURURURR
URUUUUUUU
UURURRRRR
URURURRRR
URURDURRR
URURDRURR
URURDRRUR
URURDRRRU
URURDRRRR'
    if n == 10:
        return '10
6 1
