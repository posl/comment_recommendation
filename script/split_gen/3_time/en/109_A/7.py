def main():
    A, B = map(int, input().split())
    C = set([1, 2, 3])
    C.remove(A)
    C.remove(B)
    C = list(C)[0]
    if (A * B * C) % 2 == 1:
        print("Yes")
    else:
        print("No")
main()
I would like to know if there is a faster way to do this.
Thanks in advance!
I am trying to create a function in python that will take a list of integers and return the list with the integers sorted by the number of 1 bits in the binary representation of the integer. For example, the list [2, 3, 1, 4, 7] should be sorted to [4, 2, 1, 3, 7].
I have tried using the bin function, but I have been unable to figure out how to sort the list based on the number of 1 bits in the binary representation of the integer.
I am trying to create a function in python that will take a list of integers and return the list with the integers sorted by the number of 1 bits in the binary representation of the integer. For example, the list [2, 3, 1, 4, 7] should be sorted to [4, 2, 1, 3, 7].
I have tried using the bin function, but I have been unable to figure out how to sort the list based on the number of 1 bits in the binary representation of the integer.
I am trying to make a program that will take a list of integers and return the list with the integers sorted by the number of 1 bits in the binary representation of the integer. For example, the list [2, 3, 1, 4, 7] should be sorted to [4, 2, 1, 3, 7].
I have tried using the bin function, but I have been unable to figure out how to sort the list based on the number of 1 bits in the binary representation of the integer.
I am trying to make a program that will take a list of integers and return the list with the integers sorted by the number of 1 bits in the binary representation of the integer. For example, the list [2, 3, 1, 4, 7] should be sorted to [
