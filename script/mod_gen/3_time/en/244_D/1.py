def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()
    if S1 == T1 and S2 == T2 and S3 == T3:
        print("Yes")
    elif S1 == T1 and S2 == T3 and S3 == T2:
        print("Yes")
    elif S1 == T2 and S2 == T1 and S3 == T3:
        print("Yes")
    elif S1 == T2 and S2 == T3 and S3 == T1:
        print("Yes")
    elif S1 == T3 and S2 == T1 and S3 == T2:
        print("Yes")
    elif S1 == T3 and S2 == T2 and S3 == T1:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()