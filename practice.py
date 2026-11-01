"""
*
* *
* * *
* * * *
* * * * *
"""
''' USING FOR LOOP'''
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    
'''USING WHILE LOOP'''
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
""" USING FOR LOOP"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

""" USING WHILE LOOP"""
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print()
#     i=i+1

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

"""
""" USING FOR LOOP"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ",end=" ")
#         j+=1
#     for k in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()
#     i+=1

'''USING WHILE LOOP'''
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end=" ")
#         j+=1
#     k=1
#     while k<=i:
#         print(k,end=" ")
#         k+=1
#     print()
#     i=i+1

''' 
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1 

'''
'''USING FOR LOOP'''
# n=int(input())
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     print()

'''USING WHILE LOOP'''
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end=" ")
#         j+=1
#     k=i
#     while k>=1:
#         print(k,end=" ")
#         k-=1
#     print()
#     i+=1

"""
FLOYD TRIANGLE
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
  
"""

# n=int (input())
# i = 1
# c = 1
# while i<= n:
#     x = 1
#     while x <= i:
#         if x==i:
#             print(c, end="")
#         else:
#             print(c, end=" ")
#         c += 1
#         x += 1
#     print()
            
#     i += 1

"""
1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4
"""
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     m=[]
#     while j<=n:
#         if j<=i:
#             m.append(str(i))
#         else:
#             m.append(str(j))
#         j+=1
#     i+=1
#     print(" ".join(m))

"""
CHECKER BOARD
#.#.
.#.#
#.#.
"""
# R,C=map(int,input().split())
# i=0
# while i<R:
#     j=0
#     while j<C:
#         if (i+j)%2==0:
#             print("#",end="")
#         else:
#             print(".",end="")
#         j+=1
#     print()
#     i+=1

""" 
BINARY TRIANGLE
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
# n=int(input())
# i=1
# while i<=n:
#     m=[]
#     j=1
#     while j<=i:
#         if i%2==0:
#             if j%2==0:
#                 m.append('1')
#             else:
#                 m.append('0')
#         else:
#             if j%2==0:
#                 m.append("0")
#             else:
#                 m.append('1')
#         j+=1
#     print(" ".join(m))
#     i+=1

"""
PASCAL TRIANGLE
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""
# n=int(input())
# i=1
# c=1
# m=[1]
# i=0
# while i<n:
#     j=0
#     new=[1]
#     while j<len(m)-1:
#         new.append(m[j]+m[j+1])
#         j+=1
#     new.append(1)
#     i+=1
#     print(" ".join(map(str,m)))
#     m=new

""" 
MATRIX TOTAL
"""
# x,y=map(int,input().split())
# i=0
# m=[]
# while i<x:
#     c=input().split()
#     m.append(c)
#     i+=1
# k=0
# s=0
# while k<x:
#     u=0
#     while u<y:
#         s=s+int(m[k][u])
#         u=u+1
#     k=k+1
# print(s)

"""
ROWS SUM AND COLUMN
"""
# # Write your reference solution here
# x,y=map(int,input().split())
# i=0
# m=[]
# while i<x:
#     c=input().split()
#     m.append(c)
#     i+=1
# j=0
# while j<x:
#     s=0
#     z=0
#     while z<y:
#         s=s+int(m[j][z])
#         z+=1
#     if j==x-1:
#         print(s)
#     else:
#         print(s,end=" ")
#     j+=1

# j=0
# while j<y:
#     s=0
#     z=0
#     while z<x:
#         s=s+int(m[z][j])
#         z+=1
#     if j==y-1:
#         print(s)
#     else:
#         print(s,end=" ")
#     j+=1


"""
MATRIX DIAGONAL SUK
"""

# x=int(input())
# i=0
# m=[]
# while i<x:
#     c=input().split()
#     m.append(c)
#     i+=1
# s=0
# j=0
# c=0
# while j<x:
#     s=s+int(m[j][j])
#     c=c+int(m[j][x-1-j])
#     j+=1
# print(s,end=" ")
# print(c)

"""
TRANSPOSE OF A MATRIX
"""
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