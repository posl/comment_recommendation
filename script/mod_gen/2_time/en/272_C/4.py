def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
        return
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)
main()
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is no such number, output -1.
The first line of the input contains an integer N.  The second line contains N integers A_1, A_2, ..., A_N.
The output should contain the maximum even number represented as the sum of two different elements of A.  If there is

if __name__ == '__main__':
    main()