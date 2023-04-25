Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    print(N - sum(d) + K)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    D = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            D[A[j] - 1] = 1
    print(D.count(0))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    d = [0] * K
    for i in range(K):
        d[i] = int(input())
    a = [0] * K
    for i in range(K):
        a[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(K):
            if i+1 in a[j]:
                break
        else:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = [int(x) for x in input().split()]
    A = [0] * N
    for i in range(K):
        d = int(input())
        a = [int(x) for x in input().split()]
        for j in range(d):
            A[a[j] - 1] = 1
    print(A.count(0))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [[0] * 100 for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i][:d[i]] = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(k):
            if i in a[j][:d[j]]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int,input().split())))
    l = []
    for i in range(k):
        for j in range(d[i]):
            l.append(a[i][j])
    l = list(set(l))
    print(n-len(l))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    d = [int(input()) for _ in range(k)]
    a = [list(map(int, input().split())) for _ in range(k)]

    #print(n, k)
    #print(d)
    #print(a)

    for i in range(k):
        for j in range(d[i]):
            print(a[i][j])

main()

I am trying to make a program that will take in a list of numbers and then output the list in ascending order. I have tried to use a bubble sort but I am having trouble making the program work. I am a beginner and I am having trouble making the program work. The program will be used to sort a list of numbers that are inputted by the user.

import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the length of the list: ");
        int length = input.nextInt();
        int[] list = new int[length];
        System.out.println("Enter the list: ");
        for (int i = 0; i < list.length; i++) {
            list[i] = input.nextInt();
        }
        int temp;
        for (int i = 0; i < list.length; i++) {
            for (int j = 0; j < list.length; j++) {
                if (list[i] < list[j]) {
                    temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
        System.out.println("The list in ascending order is: ");
        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i] + " ");
        }
    }
}

I am trying to make a program that will take in a list of numbers and then output the list in ascending order. I have tried to use a bubble sort but I am having trouble making the program work. I am a beginner and I am having trouble making the program work. The program will be used to sort a list of numbers that are inputted by the user.

import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the length of the list: ");
        int length = input.nextInt

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    d = []
    for i in range(k):
        d.append(list(map(int,input().split())))
    d = [item for sublist in d for item in sublist]
    print(n-len(set(d[1:])))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split())))
    print(N - sum(d[0][1:]))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
        d.append(list(map(int, input().split())))
    print(N - sum(d[1::2]))
