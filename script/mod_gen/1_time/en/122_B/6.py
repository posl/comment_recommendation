def longest_ACGT(s):
    a = 0
    b = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            a += 1
        else:
            if a > b:
                b = a
            a = 0
    if a > b:
        b = a
    return b
s = input()
print(longest_ACGT(s))
I have a list of strings, and I want to find the longest string that is a substring of another string. For example, if I have the list of strings ["ATC", "ATAGA", "TCO"] and the string "ATCODER", then I want to find the longest string in the list that is a substring of the string "ATCODER", which is "ATC". I can write a function that takes in a list of strings and a string and returns the longest string in the list that is a substring of the string, but I can't figure out how to make it so that I can call this function without passing in the list of strings every time. For example, I want to be able to call the function like this:
longest_ACGT("ATCODER")
and have it return "ATC". I'm not sure how to do this. I've tried using a global variable to store the list of strings, but I can't figure out how to make it so that I can call the function without passing in the list of strings every time.
Here is my code so far:

if __name__ == '__main__':
    longest_ACGT()