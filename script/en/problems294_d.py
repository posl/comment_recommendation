#Problem Statement
#N people, with ID numbers 1, 2, ..., N, are lining up in front of a bank.
#There will be Q events. The following three kinds of events can happen.
#1 : The teller calls the person with the smallest ID number who has not been called.
#2 x : The person with the ID number x comes to the teller for the first time. (Here, person x has already been called by the teller at least once.)
#3 : The teller again calls the person with the smallest ID number who has already been called but has not come.
#Print the ID numbers of the people called by the teller in events of the third kind.
#
#Constraints
#1 ≦ N ≦ 5 × 10^5
#2 ≦ Q ≦ 5 × 10^5
#There will not be an event of the first kind when all people have already been called at least once.
#For each event of the second kind, the person with the ID number x has already been called by the teller at least once.
#For each event of the second kind, the person with the ID number x will not come to the teller more than once.
#There will not be an event of the third kind when all people who have already been called have come to the teller.
#There is at least one event of the third kind.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format, where event_i denotes the i-th event:
#N Q
#event_1
#event_2
#.
#.
#.
#event_Q
#The description of each event is in one of the following formats:
#1
#2 x
#3
#
#Output
#Print X lines, where X is the number of events of the third kind.
#The i-th line should contain the ID number of the person called in the i-th event of the third kind.
#
#Sample Input 1
#4 10
#1
#1
#3
#2 1
#1
#2 3
#3
#1
#2 2
#3
#
#Sample Output 1
#1
#2
#4
#For each i = 1, 2, ..., Q, shown below is the set of people who have already been called but have not come just before the i-th event.
#i=1 : {}
#i=2 : {1}
#i=3 : {1,2}
#i=4 : {1,2}
#i=5 : {2}
#i=6 : {2,3}
#i=7 : {2}
#i=8 : {2}
#i=9 : {2,4}
#i=10 : {4}
#The events for i=3,7,10 are of the third kind, so you should print the persons with the smallest ID numbers in the sets for those events: 1, 2, 4.

def 