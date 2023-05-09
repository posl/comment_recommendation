def main():
    Q = int(input())
    A = [-1] * 2**20
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % len(A)] != -1:
                h += 1
            A[h % len(A)] = x
        else:
            print(A[x % len(A)])
main()
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
The second query should be A_2 = 1 instead of A_2 = 1048577.
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577
@DaisukeMatsuzaki Thank you for pointing it out. I fixed it.
I think the second query should be A_2 = 1 instead of A_2 = 1048577

if __name__ == '__main__':
    main()