def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    perms = list(permutations(range(1, N+1), N))
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))
main()
I have a list of lists and I want to find the index of a sublist. For example, I have the following list of lists:
[[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
I want to find the index of the sublist [2, 3, 4, 5]. I tried the following:
index = my_list.index([2, 3, 4, 5])
But the output is 0. I also tried the following:
index = my_list.index([2, 3, 4, 5], 1)
But the output is still 0. I also tried the following:
index = my_list.index([2, 3, 4, 5], 1, 3)
But the output is still 0. How do I find the index of a sublist?
I have a list of lists and I want to find the index of a sublist. For example, I have the following list of lists:
[[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
I want to find the index of the sublist [2, 3, 4, 5]. I tried the following:
index = my_list.index([2, 3, 4, 5])
But the output is 0. I also tried the following:
index = my_list.index([2, 3, 4, 5], 1)
But the output is still 0. I also tried the following:
index = my_list.index([2, 3, 4, 5], 1, 3)
But the output is still 0. How do I find the index of a sublist?
I have a list of lists and I want to find the index of a sublist. For example, I have the following list of lists:
[[1, 2, 3, 4], [
