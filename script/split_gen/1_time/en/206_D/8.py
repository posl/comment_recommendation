def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. Make a dictionary of the numbers and how many times they appear
    # 2. If the number appears an odd number of times, add it to a list of odd numbers
    # 3. If the number appears an even number of times, add it to a list of even numbers
    # 4. If the number appears an odd number of times, it can be used to make a palindrome
    # 5. If the number appears an even number of times, it can be used to make a palindrome
    # 6. If the number appears an odd number of times, we can use it to make a palindrome
    #    and we can use it to make a palindrome with another number
    # 7. If the number appears an even number of times, we can use it to make a palindrome
    #    and we can use it to make a palindrome with another number
    # 8. The number of operations to make a palindrome is the number of odd numbers - 1
    #    (because we can use one odd number to make a palindrome with another odd number)
    # 9. If the number of odd numbers is 0, then the number of operations is 0
    # 1.
    D = {}
    for a in A:
        if a in D:
            D[a] += 1
        else:
            D[a] = 1
    # 2.
    odd = []
    for k in D:
        if D[k] % 2 == 1:
            odd.append(k)
    # 8.
    print(len(odd) - 1)
