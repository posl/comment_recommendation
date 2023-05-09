def main():
    s = list(input())
    s.append(s.pop(0))
    print("".join(s))

if __name__ == '__main__':
    main()