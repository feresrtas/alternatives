# combination
#while not n:
  # if n==0:
 #    break
   #else:
n=int(input('n değeri giriniz\n'))
solution=[[]]
input=int()
num=[]
num_set=set()
for i in range(1,n+1):
    num.append(i)
#print (num)
for i in range(1,n+1):
    num_set.add(i) 
#print (num_set)
#num=[1,2,3,4,5,6]
#num_set={1,2,3,4}
#while not n:
 #   if n==0:
 #      break
 #   else:
for index in range (len(num)):
    solution=[i+[j] for i in solution for j in num_set.difference(set(i))]
print (solution)
print(f' {len(solution)} times possibilities')