def count(s):
    count_for = 0
    count_against = 0
    for i in s:
        if i == "For":
            count_for += 1
        else:
            count_against += 1
    if count_for > count_against:
        return "Yes"
    else:
        return "No"
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(count(s))
