def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    t = [A, B, C, D, E]
    t.sort()
    print((t[0] + 9) // 10 * 10 + t[1] + t[2] + t[3] + t[4])

if __name__ == '__main__':
    main()