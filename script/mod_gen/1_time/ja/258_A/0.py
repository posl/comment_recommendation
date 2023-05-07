def main():
    k = int(input())
    h = 21
    m = k
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    print(f"{h:02}:{m:02}")

if __name__ == '__main__':
    main()