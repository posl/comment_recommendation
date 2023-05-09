def name(n):
    if n <= 26:
        return chr(96+n)
    else:
        return name((n-1)//26) + chr(96 + (n-1)%26 + 1)
n = int(input())
print(name(n))
I was a bit confused by the problem statement. It was not clear if the numbering started at 1 or at 0. I tried to solve it using a base 26 system, where each letter is a digit. I thought that the first 26 dogs would be named a, b, c, ..., z, but the problem statement said that the dogs numbered 1,2,...,26 were respectively given the names a, b, ..., z. I was not sure if the numbering started at 0 or at 1. I tried to solve the problem using both interpretations, and they both worked. I chose the one that started at 1 because it was more intuitive to me.

if __name__ == '__main__':
    name()