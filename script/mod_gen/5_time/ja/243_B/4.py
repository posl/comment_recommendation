def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a_and_b = 0
    a_and_b_diff = 0
    for i in range(n):
        if a[i] == b[i]:
            a_and_b += 1
        else:
            for j in range(n):
                if a[i] == b[j]:
                    a_and_b_diff += 1
                    break
    print(a_and_b)
    print(a_and_b_diff)

if __name__ == '__main__':
    main()