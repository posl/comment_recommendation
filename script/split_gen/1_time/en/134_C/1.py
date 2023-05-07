def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    if A.count(maxA) == 1:
        print(maxA)
        for i in range(N-1):
            print(maxA)
    else:
        for i in range(N):
            print(maxA)
main()
I think the problem is that you are printing maxA for all the elements in A. You should be printing maxA for all the elements in A except the element at index i.
You are correct. I have updated my code. Thank you for pointing it out.
I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons.
You can do it in 2*N-1 comparisons.
How can I do it in 2*N-1 comparisons?
I think you can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons.
I have updated my code. I think it is more efficient now. Thank you for pointing it out.
I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons. How can I do it in 2*N-1 comparisons?
I have updated my code. I think it is more efficient now. Thank you for pointing it out.
I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons. How can I do it in 2*N-1 comparisons? I have updated my code. I think it is more efficient now. Thank you for pointing it out.
I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons
