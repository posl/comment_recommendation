def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = set(A)
    for i in range(2001):
        if i not in A:
            print(i)
            break
main()
This is a problem from the AtCoder Beginner Contest 245. The problem statement can be found here.
The problem is simple enough. Given a sequence of integers, find the smallest non-negative integer not in the sequence.
The first thing that comes to mind is to sort the sequence and then iterate through it, keeping track of the smallest non-negative integer not in the sequence. However, sorting the sequence is not necessary. We can use a set to keep track of the integers in the sequence. This way, we can iterate through a range of integers and see if the integer is in the set. If it isn’t, then we have found the smallest non-negative integer not in the sequence.
The time complexity is O(N) and the space complexity is O(N).
This is a problem from the AtCoder Beginner Contest 244. The problem statement can be found here.
The problem is simple enough. Given a sequence of integers, find the smallest non-negative integer not in the sequence.
The first thing that comes to mind is to sort the sequence and then iterate through it, keeping track of the smallest non-negative integer not in the sequence. However, sorting the sequence is not necessary. We can use a set to keep track of the integers in the sequence. This way, we can iterate through a range of integers and see if the integer is in the set. If it isn’t, then we have found the smallest non-negative integer not in the sequence.
The time complexity is O(N) and the space complexity is O(N).
This is a problem from the AtCoder Beginner Contest 243. The problem statement can be found here.
The problem is simple enough. Given a sequence of integers, find the smallest non-negative integer not in the sequence.
The first thing that comes to mind is to sort the sequence and then iterate through it, keeping track of the smallest non-negative integer not in the sequence. However, sorting the sequence is not necessary. We can use a set to keep track of the integers in the sequence. This way, we can iterate through a range of integers and see if the integer is in the set. If it isn’t, then we have found the smallest non-negative integer not in the sequence.
The time complexity
