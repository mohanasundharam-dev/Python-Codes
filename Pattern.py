#         ---------------Pattern Problems-------------------

# n = 5
# for i in range(1,6):
#     for j in str(i):
#         print("*"*i,end="")
#     print()

# n = 5           
# for i in range(1,n+1):
#     for x in range(i):
#         print("*",end="")
#     for j in range(n-1):
#         print(" "*i,end="")
#     print()

# # n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="")
#     print()

# for i in range(1,n+1):
#     for j in range(n+1,i,-1):
#         print("*",end="")
#     print()

# for i in range(1,n+1):
#     for k in range (i-1):
#         print(" ",end="")
#     for j in range(n+1,i,-1):
#         print("*",end="")
#     print()

# for i in range (1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for x in range((i*2)-1):
#         print("*",end="")
#     print()

# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" ",end="")
#     for k in range((n*2)-1):
#         print("*",end="")
#     n = n-1
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()
# for i in range(1,n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# n = 5

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range((i*2)-1):
#         print("*",end="")
#     print()
# for i in range(1,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(1,((n-i)*2)):
#         print("*",end="")
#     print()


#  11 - 
# for i in range(1,n):
#     for j in range(i):
#         print(" ",end="")
#     n = n-1
#     for k in range((n*2)-1):
#         print("*",end="")
#     print()

# n = 5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(((n-i)*2)-1):
#         print("*",end="")
#     print()
    
# for i in range (2,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for x in range((i*2)-1):
#         print("*",end="")
#     print()

# 12 -

# for i in range(1,n+1):
#     if ( n == i or i == n-n+1 ):
#         for j in range(n):
#             print("*",end="")
#     else:
#         for k in range(1,n+1):
#             if(n == k or k == n-n+1):
#                 print("*",end="")   
#             else:
#                 print(" ",end="")
#     print()

# 13 - 

# for i in range(1,n+1):
#     if ( n == i or i == 1 ):
#         for j in range(i):
#             print("*",end="")
#     else:
#         for k in range(1,n+1):
#             if(k == 1 or k == i):
#                 print("*",end="")   
#             else:
#                 print(" ",end="")
#     print()

#14 -

# for i in range(n,0,-1):
#     if ( n == i or i == n-n+1 ):
#         for j in range(i):
#             print("*",end="")
#     else:
#         for k in range(1,n+1):
#             if(k == 1 or k == i):
#                 print("*",end="")   
#             else:
#                 print(" ",end="")
#     print()

# 15 -
# n = 5
# for i in range (1,n+1):
#     for j in range(n-i):
#         print("-",end="")
#     for x in range((i*2)-1):
#         if ( x == 0 or x == i*2 ):
#             print("*",end="")
#         else:
#             print("-",end="") 
#     print()


