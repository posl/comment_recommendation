def count_possible_pin(s):
    count = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in pin:
                break
            if s[j] == 'x' and str(j) in pin:
                break
        else:
            count += 1
    return count
s = input()
print(count_possible_pin(s))
I was trying to make the code more efficient and found out that I can use itertools.product() to generate all possible combinations of characters.
from itertools import product
