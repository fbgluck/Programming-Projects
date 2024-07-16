# Towers of Hanoi
# Move all disks from stack 1 to stack 3
# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack. In other words, a disk can only be moved if it is the uppermost disk on a stack.
# No larger disk may be placed on top of a smaller disk
#
# This is the list of moves that always leads to success
# 121 3
# 121 4
# 121 3
# 121 5
# 121 3
# 121 4
# 121 3
# 121 _
# Data Structures

# Print the three stacks of disks
def print_stack():
    for i in range(0,5):
        print (f"  {stack_1[i]}\t",end="\t")
        print (f"   {stack_2[i]}\t",end ="\t")
        print (f"   {stack_3[i]}")
    # Print the base of each tower
    print (5*"=","\t\t",5*"=","\t\t",5*"=")

def makemove (last_value):
    print("")
    

# Program starts here

# set initial stack of disks
stack_1 = [1,2,3,4,5]
stack_2 = ["|","|","|","|","|","|"]
stack_3 = ["|","|","|","|","|","|"]
print_stack()
