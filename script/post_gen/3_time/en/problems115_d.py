#Problem Statement
#In some other world, today is Christmas.
#Mr. Takaha decides to make a multi-dimensional burger in his party. A level-L burger (L is an integer greater than or equal to 0) is the following thing:
#A level-0 burger is a patty.
#A level-L burger (L ≧ 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
#For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
#The burger Mr. Takaha will make is a level-N burger. Lunlun the Dachshund will eat X layers from the bottom of this burger (a layer is a patty or a bun). How many patties will she eat?
#
#Constraints
#1 ≦ N ≦ 50
#1 ≦ X ≦ ( the total number of layers in a level-N burger )
#N and X are integers.
#
#Input
#Input is given from Standard Input in the following format:
#N X
#
#Output
#Print the number of patties in the bottom-most X layers from the bottom of a level-N burger.
#
#Sample Input 1
#2 7
#
#Sample Output 1
#4
#There are 4 patties in the bottom-most 7 layers of a level-2 burger (BBPPPBPBPPPBB).
#
#Sample Input 2
#1 1
#
#Sample Output 2
#0
#The bottom-most layer of a level-1 burger is a bun.
#
#Sample Input 3
#50 4321098765432109
#
#Sample Output 3
#2160549382716056
#A level-50 burger is rather thick, to the extent that the number of its layers does not fit into a 32-bit integer.

def 