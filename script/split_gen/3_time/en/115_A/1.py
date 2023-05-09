def main():
    d = int(input())
    if d == 25:
        print("Christmas")
    elif d == 24:
        print("Christmas Eve")
    elif d == 23:
        print("Christmas Eve Eve")
    elif d == 22:
        print("Christmas Eve Eve Eve")
main()
I’m learning Python and I’m trying to make a program that will convert a number into a word. For example, if the user inputs the number 2, the program should output “Two”. I have a list of numbers and another list of words, and I’m trying to make a program that will compare the input with the numbers list and output the corresponding word from the words list. However, I’m having a hard time figuring out how to make the program compare the input with the numbers list. I’ve tried using the “in” operator, but it didn’t work. Here’s the code:
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
words = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty"]
input = int(input("Enter a number: "))
