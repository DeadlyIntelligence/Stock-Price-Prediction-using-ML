from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
#n for number of iteration
print("\t\t\t\tMACHINE-LEARNING")
print("\t\t\t\t\t-BY VISHWAK , JEYANDRANATH")
n=input("enter the value of n to allot spaces : ")
x1=0
y1=0
x3=0
smy=0
ssy=0
#produce value for xval to assign in y=b0+b1*xval
x=[0]*n
y=[0]*n
i2=0
while i2<n:
    print "number of time input taken : ",i2+1
    x[i2]=input("enter value of x :")
    y[i2]=input("enter value of y :")
    print "[",x[i2],",",y[i2],"]"
    i2=i2+1
xval=input("enter x-value to predict : ")
#array size dec
xcat=[0]*n
ycat=[0]*n
xcat2=[0]*n
mul=[0]*n
mul2=0
i=0   
while i<n:
    x1=float(x1+x[i])
    y1=float(y1+y[i])
    i=i+1

#print x1
#print y1
xmean = float(x1/n)
ymean = float(y1/n)
#print "mean value of x : ",xmean
#print "mean value of y : ",ymean
j=0
while j<n:
    xcat[j]=x[j]-xmean
    ycat[j]=y[j]-ymean
    #print xcat[j],ycat[j]
    j=j+1
k=0
while k<n:
    xcat2[k]=xcat[k]*xcat[k]
    #print xcat2[k]
    k=k+1
l=0
while l<n:
    x3=x3+xcat2[l]
    l=l+1
#print "the value of x3 is : ",x3    

i1=0
while i1<n:
    mul[i1]=xcat[i1]*ycat[i1]
    mul2=mul2+mul[i1]
    #print mul[i1]
    i1=i1+1

#print "the value of mul2 is : ",mul2
b1=float(mul2)/float(x3)
print "The b1 value is : ",b1
b0=float(ymean)-float(b1)*float(xmean)
print "The b0 value is : ",b0
py=float(b0)+float(b1)*xval
print "The equation to predict : y =",b0,"+",b1,"*x"
print "The predicted value is : ",py
#Below:Predicting + or - value
for i in range(0,n-1,1):
    ssy=ssy+y[i+1]-y[i]
#smy=ssy
smy=ssy+b1
if (b0!=0):
    print ("The stock price may reach between",smy+py,"or",py-smy,"If",py,"is reached") 
#append() is used to add new value to the array
x.append(xval)
y.append(py)
plt.scatter(x, y,color='b')
plt.plot(x,y)
plt.show()


