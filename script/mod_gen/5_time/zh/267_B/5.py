def solve(s):
    # Write your code here
    for i in range(1, 11):
        if s[i - 1] == "0":
            for j in range(1, 11):
                if s[j - 1] == "1":
                    if i == 1:
                        if j == 2 or j == 3 or j == 4 or j == 5:
                            if s[j] == "1":
                                return "Yes"
                    elif i == 10:
                        if j == 6 or j == 7 or j == 8 or j == 9:
                            if s[j - 2] == "1":
                                return "Yes"
                    else:
                        if j == i + 1 or j == i + 2 or j == i + 3 or j == i + 4:
                            if s[j - 2] == "1" and s[j] == "1":
                                return "Yes"
    return "No"
s = input()
print(solve(s))
