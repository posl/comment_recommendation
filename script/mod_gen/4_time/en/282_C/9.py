def main():
    n = int(input())
    s = input()
    s = s.replace(",",".")
    s = s.replace("\"","")
    s = s.replace(".","\",")
    print("\""+s)

if __name__ == '__main__':
    main()