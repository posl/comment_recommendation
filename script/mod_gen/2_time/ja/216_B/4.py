def main():
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                s1, t1 = input().split()
                s2, t2 = input().split()
                if s1 == s2 and t1 == t2:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()