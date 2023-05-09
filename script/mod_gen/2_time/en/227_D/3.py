def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K == 1:
        print(1)
        return
    if K == N:
        print(A[-1])
        return
    #print(A)
    #print(N, K)
    #print(A)
    #print(A[K-1])
    #print(A[K])
    if A[K-1] == A[K]:
        print(1)
        return
    if A[K-1] < A[K]:
        print(A[K-1])
        return
    if A[K-1] > A[K]:
        print(1)
        return
main()
I am trying to understand how to do a simple python script. I have a script that reads a file that has the following format:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
I want to read the file and add the first and second column, then add the third and fourth column, and add the two sums together. The output should be:
6 22
14 30
22 38
30 46
I have tried the following:
import sys
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        line = line.split()
        sum1 = int(line[0]) + int(line[1])
        sum2 = int(line[2]) + int(line[3])
        print(sum1, sum2)
This works but it prints out the sums one by one instead of printing out the sums together on the same line. I am not sure how to get the sums to print out together on the same line. I have tried using sys.stdout.write() but that did not work. Any help would be appreciated.
I am trying to create a function that would allow me to get the number of words in a sentence, and then print out the number of words in the sentence.

if __name__ == '__main__':
    main()