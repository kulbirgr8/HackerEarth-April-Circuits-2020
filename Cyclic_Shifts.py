'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
for i in range(n):
    num=[]
    num= list(input(). split())
    n1=bin(int(num[0])).replace("0b", "")
    n1=("0"*(16-len(n1)))+n1
    n2=int(num[0])
    n3=int(num[1])
    if num[2]=='L':
        print(int(n1[n3:]+n1[:n3],2))
    else:
        print(int(n1[-n3:]+n1[:16-n3],2))