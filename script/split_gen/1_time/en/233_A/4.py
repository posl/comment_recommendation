def main():
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x%10 == 0:
        x = x + 10
    else:
        x = x + (10 - x%10)
    count = 0
    while x < y:
        x = x + 10
        count = count + 1
    print(count)
