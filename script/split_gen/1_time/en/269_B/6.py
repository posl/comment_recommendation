def main():
    s = []
    for i in range(10):
        s.append(input())
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                a = i + 1
                break
        if a != 0:
            break
    for i in range(10):
        for j in range(10):
            if s[i][9 - j] == '#':
                b = 10 - j
                break
        if b != 0:
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == '#':
                c = i + 1
                break
        if c != 0:
            break
    for i in range(10):
        for j in range(10):
            if s[9 - j][i] == '#':
                d = 10 - j
                break
        if d != 0:
            break
    print(a, b)
    print(c, d)
main()
I have a problem with my code. I am trying to find the largest number of a list and add it to a new list. I am using the append function to add the largest number to the new list. It works fine when the list is a list of 3 numbers. But when I try to do it for a list of 10 numbers, it gives me an error. I think it is because I am using the append function to add the largest number to the new list, but I don't know how to fix it. Here is my code:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = []
for i in range(10):
    new_numbers.append(max(numbers))
    numbers.remove(max(numbers))
print(new_numbers)
I'm trying to make a program that will take a list of numbers and then find the largest number in the list and then print that number. I have tried using the max function, but it doesn't work. Here is my code:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(numbers))
I have a list
