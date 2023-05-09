def get_name(n):
    char_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    if n <= 26:
        return char_list[n - 1]
    else:
        return get_name((n - 1) // 26) + char_list[(n - 1) % 26]
n = int(input())
print(get_name(n))
This is a very simple problem. The only trick is to get the name of the dog for a given number.
In the first line of the code, I create a list of characters from a to z. In the second line, I check if the number is less than or equal to 26. If so, I return the character at the index n - 1. If not, I call the function again with the argument (n - 1) // 26, which gives me the number of the dog in the previous set of 26 dogs. I then add the character at the index (n - 1) % 26, which gives me the character for the current dog.
I have also uploaded this code to GitHub.
I have also uploaded this code to G
