Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')
    print()

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(*[i for i in a if i != x])

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(' '.join([str(i) for i in a if i != x]))

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [i for i in a if i != x]
    print(*b)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(*[i for i in A if i != X])

=======
Suggestion 8

def remove_element(list, element):
    for item in list:
        if item == element:
            list.remove(item)
    return list

=======
Suggestion 9

def removeX(A, X):
    A = [x for x in A if x != X]
    return A

=======
Suggestion 10

def remove_element_from_list(list, element):
    return [value for value in list if value != element]
