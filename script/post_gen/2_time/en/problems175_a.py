Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s == "RRR":
        print(3)
    elif s == "RRS" or s == "SRR":
        print(2)
    elif s == "RSS" or s == "SRS" or s == "SSR" or s == "RSR":
        print(1)
    else:
        print(0)

=======
Suggestion 2

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 3

def main():
    S = input()
    count = 0
    maxCount = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > maxCount:
            maxCount = count
    print(maxCount)

=======
Suggestion 4

def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

main()

=======
Suggestion 5

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            if count >= max_count:
                max_count = count
            count = 0
    if count >= max_count:
        max_count = count
    print(max_count)

=======
Suggestion 6

def main():
    S = input()
    max_rain = 0
    rain = 0
    for i in range(3):
        if S[i] == 'R':
            rain += 1
            if rain > max_rain:
                max_rain = rain
        else:
            rain = 0
    print(max_rain)

=======
Suggestion 7

def main():
    # Write your code here
    S = input()
    count = 0
    max_count = 0
    for i in S:
        if i == 'R':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 8

def main():
  S = input()
  cnt = 0
  max_cnt = 0
  for i in S:
    if i == "R":
      cnt += 1
    else:
      if max_cnt < cnt:
        max_cnt = cnt
      cnt = 0
  if max_cnt < cnt:
    max_cnt = cnt
  print(max_cnt)

=======
Suggestion 9

def main():
    s = input()
    print(max(len(x) for x in s.split('S')))

=======
Suggestion 10

def main():
    #Read the input
    S = input()
    #Initialize the counter for the maximum number of consecutive rainy days
    max_rainy_days = 0
    #Initialize the counter for the current number of consecutive rainy days
    current_rainy_days = 0
    #Loop through the input string
    for i in range(len(S)):
        #Increment the counter for the current number of consecutive rainy days if the current character is R
        if S[i] == 'R':
            current_rainy_days += 1
        #Otherwise, reset the counter for the current number of consecutive rainy days
        else:
            current_rainy_days = 0
        #Update the counter for the maximum number of consecutive rainy days if the current number of consecutive rainy days is greater than the maximum number of consecutive rainy days
        if current_rainy_days > max_rainy_days:
            max_rainy_days = current_rainy_days
    #Print the output
    print(max_rainy_days)
