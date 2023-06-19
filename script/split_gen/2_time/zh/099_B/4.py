def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    x = b - a
    i = 1
    while True:
        if i*(i+1)/2 >= x:
            break
        i += 1
    print(int(i*(i+1)/2-x))
