def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if M == 0:
        print('Yes')
        return
    for i in range(M):
        for j in range(M):
            if A[i] == A[j] and B[i] == B[j]:
                if C[i] != C[j] or D[i] != D[j]:
                    print('No')
                    return
            elif A[i] == B[j] and B[i] == A[j]:
                if C[i] != D[j] or D[i] != C[j]:
                    print('No')
                    return
    print('Yes')
main()
I am trying to write a program that will allow the user to input a number and then print out the corresponding month. I have been trying to use a dictionary to store the number and month, but I am having trouble getting the program to work. I have tried using the get function, but it is not working. Here is what I have so far:
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month = int(input('Enter a number: '))
print(months.get(month))
I know that I am missing something simple, but I just can't figure it out. Any help would be appreciated.
I have a list of dictionaries like this:
[{1: 'a'}, {2: 'b'}, {3: 'c'}]
I want to get a list of values from the dictionary, like this:
['a', 'b', 'c']
How can I do this?
I have a list of dictionaries like this:
[{1: 'a'}, {2: 'b'}, {3: 'c'}]
I want to get a list of values from the dictionary, like this:
['a', '

if __name__ == '__main__':
    main()