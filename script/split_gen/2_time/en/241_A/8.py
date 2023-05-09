def main():
    #read input
    a = input()
    a = a.split()
    #convert the input to integers
    for i in range(len(a)):
        a[i] = int(a[i])
    #set the starting value of the screen
    screen = 0
    #loop through the input 3 times
    for j in range(3):
        #set the screen to the value of the input at that index
        screen = a[screen]
    #print the final value of the screen
    print(screen)
