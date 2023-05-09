def main():
    h, m = map(int, input().split())
    if m == 59:
        if h == 23:
            print("0 0")
        else:
            print(str(h+1)+" 0")
    else:
        print(str(h)+" "+str(m+1))
