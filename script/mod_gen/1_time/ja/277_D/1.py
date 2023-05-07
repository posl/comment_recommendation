def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 2:
        print(N//2)
        return
    if M == 3:
        print(A.count(0) + (N-A.count(0))//3)
        return
    if M == 4:
        print(A.count(0)//2 + (N-A.count(0))//4)
        return
    if M == 5:
        print(A.count(0)//2 + A.count(1)//2 + (N-A.count(0)-A.count(1))//5)
        return
    if M == 6:
        print(A.count(0)//3 + A.count(1)//2 + A.count(2)//3 + (N-A.count(0)-A.count(1)-A.count(2))//6)
        return
    if M == 7:
        print(A.count(0)//3 + A.count(1)//3 + A.count(2)//3 + A.count(3)//3 + (N-A.count(0)-A.count(1)-A.count(2)-A.count(3))//7)
        return
    if M == 8:
        print(A.count(0)//3 + A.count(1)//3 + A.count(2)//3 + A.count(3)//3 + A.count(4)//3 + (N-A.count(0)-A.count(1)-A.count(2)-A.count(3)-A.count(4))//8)
        return
    if M == 9:
        print(A.count(0)//3 + A.count(1)//3 + A.count(2)//3 + A.count(3)//3 + A.count(4)//3 + A.count(5)//3 + (N-A.count(0)-A.count(1)-A.count(2)-A.count(3)-A.count(4)-A.count(5))//9)
        return
    if M == 10:
        print(A.count(0)//4 + A.count(1)//4 + A.count(2)//4 + A.count(3)//4 + A.count(4)//4 + A.count(5)//4 + A.count(6)//4 + (N-A.count(0)-A

if __name__ == '__main__':
    main()