#Diamond Pattern
n=5
#For Upper Half
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
#For Lower Half
for i in range(1,n):
    print(" "*i,end="")
    print("*"*(8-(2*i-1)))


#Output
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *