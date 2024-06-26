#Problem Statement
#There is a cave.
#The cave has N rooms and M passages. The rooms are numbered 1 to N, and the passages are numbered 1 to M. Passage i connects Room A_i and Room B_i bidirectionally. One can travel between any two rooms by traversing passages. Room 1 is a special room with an entrance from the outside.
#It is dark in the cave, so we have decided to place a signpost in each room except Room 1. The signpost in each room will point to one of the rooms directly connected to that room with a passage.
#Since it is dangerous in the cave, our objective is to satisfy the condition below for each room except Room 1.
#If you start in that room and repeatedly move to the room indicated by the signpost in the room you are in, you will reach Room 1 after traversing the minimum number of passages possible.
#Determine whether there is a way to place signposts satisfying our objective, and print one such way if it exists.
#
#Constraints
#All values in input are integers.
#2 ≦ N ≦ 10^5
#1 ≦ M ≦ 2 × 10^5
#1 ≦ A_i, B_i ≦ N (1 ≦ i ≦ M)
#A_i ≠ B_i (1 ≦ i ≦ M)
#One can travel between any two rooms by traversing passages.
#
#Input
#Input is given from Standard Input in the following format:
#N M
#A_1 B_1
#:
#A_M B_M
#
#Output
#If there is no way to place signposts satisfying the objective, print No.
#Otherwise, print N lines. The first line should contain Yes, and the i-th line (2 ≦ i ≦ N) should contain the integer representing the room indicated by the signpost in Room i.
#
#Sample Input 1
#4 4
#1 2
#2 3
#3 4
#4 2
#
#Sample Output 1
#Yes
#1
#2
#2
#If we place the signposts as described in the sample output, the following happens:
#Starting in Room 2, you will reach Room 1 after traversing one passage: (2) -> 1. This is the minimum number of passages possible.
#Starting in Room 3, you will reach Room 1 after traversing two passages: (3) -> 2 -> 1. This is the minimum number of passages possible.
#Starting in Room 4, you will reach Room 1 after traversing two passages: (4) -> 2 -> 1. This is the minimum number of passages possible.
#Thus, the objective is satisfied.
#
#Sample Input 2
#6 9
#3 4
#6 1
#2 4
#5 3
#4 6
#1 5
#6 2
#4 5
#5 6
#
#Sample Output 2
#Yes
#6
#5
#5
#1
#1
#If there are multiple solutions, any of them will be accepted.

def 