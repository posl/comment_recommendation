def main():
    A,B = map(int,input().split())
    g = 1
    time = 0
    while(True):
        if A >= (B * time) / (g ** (1/2)):
            time += 1
            g += 1
        else:
            break
    time -= 1
    print((time + (A / (g ** (1/2)))))

if __name__ == '__main__':
    main()