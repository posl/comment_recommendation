def main():
    N = input()
    if N.count('0') > 0:
        print(-1)
        return
    if N.count('3') > 0 or N.count('6') > 0 or N.count('9') > 0:
        print(0)
        return
    if N.count('2') > 0 or N.count('5') > 0 or N.count('8') > 0:
        print(1)
        return
    print(2)
    return

if __name__ == '__main__':
    main()