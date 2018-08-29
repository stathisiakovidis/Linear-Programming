import re
import sys
import numpy as np
file = open('test.txt', 'r')

linec = 0


c=[]
A={}
Eqin={}
B={}
j=0
MinMax=0

for line in file:
    if(linec == 0):
        matches = re.finditer( '(^(min|max)[ ]*(\-|\+)?[ ]*(\d*)[x](\d*))|([ ]*(\+|\-){1}[ ]*(\d*)[ ]*[x][ ]*(\d*)[ ]*)|([\S]+)', line)
        for match in matches:
            if(match.group(10)):
                exit()
            else:
                if(linec==0):
                    if(match.group(1)):
                        if (match.group(2)=='min'):
                            MinMax=-1
                        else:
                            MinMax=1

                        if(int(match.group(5))-1!=len(c)):
                            for i  in range (0,int(match.group(5))-1):
                                c.append(0)
                        newNumber="+"
                        if(match.group(3)):
                            if(match.group(3)=="-"):
                                newNumber="-"
                        if(match.group(4)):
                            newNumber= newNumber+match.group(4)
                        else:
                            newNumber= newNumber+"1"
                        c.append(int(newNumber))
                        linec=1
                elif(linec==1):
                    newNumber="+"
                    if(match.group(7)):
                        if(match.group(7)=="-"):
                            newNumber="-"
                    if(match.group(8)):
                        newNumber= newNumber+match.group(8)
                    else:
                        newNumber= newNumber+"1"
                    c.append(int(newNumber))
    elif(linec > 0):
        a=[]
        for i in range(0,len(c)):
            a.append(0)  
        matches = re.finditer( '(x\d*\s*\>\=\s*0)|(^(st|s\.t\.|subject)?[ ]*(\-|\+)?[ ]*(\d*)[ ]*[x][ ]*(\d+))|([ ]*(\+|\-){1}[ ]*(\d*)[ ]*[x][ ]*(\d+))|([ ]*(\>\=|\<\=|\=)[ ]*(\+|\-)?[ ]*(\d+))[ ]*|([\S]+)', line)
        for match in matches:
            if(match.group(15)):
                exit()
            else:
                if(linec==1):
                    if(match.group(3)):
                        newNumber="+"
                        if(match.group(4)):
                            if(match.group(4)=="-"):
                                newNumber="-"
                        if(match.group(5)==""):
                            newNumber= newNumber+"1"
                        else:
                            newNumber= newNumber+match.group(5)
                        a[int(match.group(6))-1]=int(newNumber)
                        linec=2
                    else:
                        exit()
                elif(linec==2):
                    if(match.group(2)):
                        newNumber="+"
                        if(match.group(4)):
                            if(match.group(4)=="-"):
                                newNumber="-"
                        if(match.group(5)==""):
                            newNumber= newNumber+"1"
                        else:
                            newNumber= newNumber+match.group(5)
                        a[int(match.group(6))-1]=int(newNumber)
                        linec=2
                    if(match.group(7)):
                        newNumber="+"
                        if(match.group(8)=="-"):
                            newNumber="-"
                        if(match.group(9)==""):
                            newNumber= newNumber+"1"
                        else:
                            newNumber= newNumber+match.group(9)
                        a[int(match.group(10))-1]=int(newNumber)
                if(match.group(11)):
                    nNumber="+"
                    if(match.group(12)==">="):
                        pros=1
                    elif(match.group(12)=="="):
                        pros=0
                    else:
                        pros=-1
                    if(match.group(13)):
                        if(match.group(13)=="-"):
                            nNumber="-"
                    if(match.group(14)==""):
                        nNumber= nNumber+"1"
                    else:
                        nNumber= nNumber+match.group(14)
        if(match.group(1)):
            u=0
        else:
            B[j]=int(nNumber)
            Eqin[j]=int(pros)               
            A[j]=a   
            j=j+1

file.close()

print "MinMax=" + str(MinMax)                       
print "C=" + str(c)
print "A=" + str(A)
print "B=" + str(B)
print "Eqin=" + str(Eqin)


file = open("result.txt","w")
file.write("MinMax=" + str(MinMax)+"\n")
file.write("C=" + str(c)+"\n")
file.write("A=" + str(A)+"\n")
file.write("B=" + str(B)+"\n")
file.write("Eqin=" + str(Eqin))

file.close()

                

