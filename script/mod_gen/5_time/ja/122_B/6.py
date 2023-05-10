def main():
    s = input()
    s = s.replace("A", "1")
    s = s.replace("T", "1")
    s = s.replace("C", "1")
    s = s.replace("G", "1")
    s = s.replace("1", " ")
    s = s.split()
    print(len(max(s, key=len)))

if __name__ == '__main__':
    main()