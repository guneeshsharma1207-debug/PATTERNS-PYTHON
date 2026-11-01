# n=int(input())
# i=1
# while i<=n:
#     j=1                                  1
#     while j<=i:                          1 2
#         if j<i:                          1 2 3
#             print(j,end=" ")             1 2 3 4  
#         if j==i:
#             print(j,end="")
#         j+=1
#     print()
#     i+=1

# n=int(input())
# i=1
# while i<=n:
#     j=1
#     # print spaces n-i
#     while j<=n-i:                                 1
#         print(" ",end=" ")                      1 2
#         j+=1                                  1 2 3
#     # prints seq from (1...i)               1 2 3 4
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1
    
# # Alternate method

# n=int(input())
# i=1
# while i<=n:                                 
#     print(" "*(n-i),end="")               
#     j=i                                   
#     while j>=1:                          
#         print(j,end='')
#         if j<1:
#             print(" ",end="")
#         j-=1
#     print()
#     i+=1   
    
# question 3
# n=int(input())
# i=1
# while i<=n:                                  1
#     print(" "*(n-i),end="")                 21
#     j=i                                    321
#     while j>=1:                           4321
#         print(j,end='')
#         j-=1
#     print()
#     i+=1   

# question 4
#      1
#    1 2 1 
#  1 2 3 2 1
#1 2 3 4 3 2 1

# n=int(input())
# i=1
# while i<=n:
#     j=n-i
#     # print spaces n-i            from line 63 to 74 it prints
#     while j>=1:                            1    
#         print(" ",end=" ")               1 2          
#         j-=1                           1 2 3
#     j=1                              1 2 3 4
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     c=i-1                         from line 75 to 78
    # while c>=1:                           1
    #     print(c,end=" ")                  2 1
    #     c-=1                              3 2 1
    # print()
    # i+=1
    
    
    
    
    
""" TRANSPOSE OF A MATRIX """

# Write your reference solution here
# R,C=map(int,input().split())
# i=0
# m=[]
# while i<R:
#     c=input().split()
#     m.append(c)
#     i+=1
# j=0
# while j<C:
#     k=[]
#     i=0
#     while i<R:
#         k.append(m[i][j])
#         i+=1
#     print(" ".join(k))
#     j+=1