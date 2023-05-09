def main():
    s = input()
    if s == "RRR":
        print(3)
    elif s == "RRS" or s == "SRR":
        print(2)
    elif s == "RSS" or s == "SRS" or s == "SSR" or s == "RSR":
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()