def main():
    s = input()
    print(s.rfind("a")+1 if s.rfind("a")!=-1 else -1)

if __name__ == '__main__':
    main()