def main():
    #input
    k = int(input())
    
    #calculate
    h = 21
    m = 0
    m += k
    if m >= 60:
        h += m // 60
        m = m % 60
    if h >= 24:
        h = h % 24
    
    #output
    print(str(h).zfill(2) + ":" + str(m).zfill(2))
    
    return

if __name__ == '__main__':
    main()