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
