def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("error")
        return
    if S.count('"') % 2 == 1:
        print("error")
        return
    result = ""
    in_enclosed = False
    for c in S:
        if c == '"':
            in_enclosed = not in_enclosed
        elif c == ',' and not in_enclosed:
            result += '.'
        else:
            result += c
    print(result)

if __name__ == '__main__':
    main()