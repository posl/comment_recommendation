def add_comma(num):
    if num < 1000:
        return str(num)
    else:
        return add_comma(num//1000) + ',' + '{:03d}'.format(num%1000)
n = int(input())
print(len(add_comma(n).split(','))-1)
