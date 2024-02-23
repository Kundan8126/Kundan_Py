def arear(a=10,b=20):
  print(a*b)
def areat(a=20,b=30):
  print(0.5*a*b)
def areac(r=33):
  print(3.14*r*r)
ch=int(input("enter your choice to calculate the area from \n1.RECTANGLE\n2.TRIANGLE\n3.CIRCLE\n"))
if(ch==1):
    arear()
elif(ch==2):
    areat()
elif(ch==3):
    areac()
else: print("select number between 1,2 and 3 only...")