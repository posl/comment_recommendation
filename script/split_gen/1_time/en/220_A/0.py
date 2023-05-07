def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)
main()
I am trying to make a program that will take a string input and output the number of vowels and consonants in the string. I have made the program work, but I am getting an error when I input a string with a space in it. I have tried using .strip() and .replace() but neither of those work.
