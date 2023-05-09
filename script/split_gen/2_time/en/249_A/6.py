def jog (a, b, c, d, e, f, x):
    takahashi = (a + c) * b
    aoki = d * e
    if (takahashi > aoki):
        print("Takahashi")
    elif (takahashi < aoki):
        print("Aoki")
    else:
        print("Draw")
a, b, c, d, e, f, x = map(int, input().split())
jog(a, b, c, d, e, f, x)
I am trying to understand the logic behind the following code. I have a list of strings and for each string I want to create a dictionary where the key is the string and the value is the length of the string. I am having a hard time understanding the following code.
