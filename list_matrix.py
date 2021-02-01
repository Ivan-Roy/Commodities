mlist=[]
sm=0
sm1=0
m=int(input("Enter number of lists:"))
n=int(input("Enter number of elements:"))
for i in range(m):
      a=[]
      print("Enter the elements")
      for j in range(n):
          x=int(input())
          a.append(x)
      mlist.append(a)
for i in mlist:
    for j in i:
        print(j,"\t",end=" ")
    print()
t=1
for i in mlist:
    for j in i:
        sm+=j
    print("Client",t,"sells:",sm,"commodities")
    sm=0
    t+=1
h=1
while h<=n:
    sm1=0
    for i in mlist:
        for j in i:
            sm1+=j
            i.remove(j)
            break
    print("Commodity",h,"sold by each client is:",sm1)
    h+=1
