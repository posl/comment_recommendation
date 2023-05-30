def reverse_string(string, start, end):
    string = string[:start-1] + string[start-1:end][::-1] + string[end:]
    return string
L, R = map(int, input().split())
S = input()
print(reverse_string(S, L, R))
