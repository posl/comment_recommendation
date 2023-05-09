def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # create a list of numbers from 1 to N
    numbers = list(range(1, N + 1))
    # create a list of all permutations of the list of numbers
    perms = list(itertools.permutations(numbers))
    # get the index of the permutation P in the list of all permutations
    i1 = perms.index(tuple(P))
    # get the index of the permutation Q in the list of all permutations
    i2 = perms.index(tuple(Q))
    # print the difference of the indices
    print(abs(i1 - i2))
