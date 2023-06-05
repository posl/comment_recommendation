def main():
    str = input()
    str = str.replace("/","")
    if int(str) <= 20190430:
        print("平成")
    else:
        print("TBD")

if __name__ == '__main__':
    main()