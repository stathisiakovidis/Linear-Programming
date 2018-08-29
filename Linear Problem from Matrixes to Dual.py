import re
import ast

file = open('test.txt','r')
file1 = open ('result.txt', 'w')
linec=0
c=[]
A=[]
B=[]
w=[]
wres=[]
Equin=[]
MinorMax=0

for line in file:
    if(linec==0):
        matches = re.finditer('(\-?\d+)',line)
        for m in matches:
            if (m.group(1)== '-1'):
                file1.write("max ")
                MinorMax=-1
            else:
                file1.write("min ")
        linec=1
    elif(linec==1):
         matches = re.finditer('\[[\,?\ ?(\-?\d+)]*\]',line)
         for m in matches:
             c = ast.literal_eval(m.group(0))
             
             for i in range(1,len(c)+1):
                 w.append("w"+str(i))    
             
             linec=2
    elif(linec==2):
        matches = re.finditer('\[[\,?\ ?(\-?\d+)]*\]',line)
        for m in matches:
            A.append(ast.literal_eval(m.group(0)))
        A = zip(*A)
        
        linec=3
        
    elif(linec==3):
        matches = re.finditer('\: (\-?\d+)',line)
        for m in matches:
            B.append(ast.literal_eval(m.group(1)))
        linec=4
        
    elif(linec==4):
         matches = re.finditer('\: (\-?\d+)',line)
         i=1
         for m in matches:
            if(MinorMax==-1):
                if(m.group(1)=='1'):
                    wres.append('w'+ str(i) + ">=0")
                elif(m.group(1)=='-1'):
                    wres.append('w'+ str(i) + "<=0")
                else:
                    wres.append('w'+ str(i) + "=free")
                Equin.append("<=")
            else:
                if(m.group(1)=='1'):
                    wres.append('w'+ str(i) + "<=0")
                elif(m.group(1)=='-1'):
                    wres.append('w'+ str(i) + ">=0")
                else:
                    wres.append('w'+ str(i) + "=free")
                Equin.append(">=")   
            i+=1
         
for i in range(0,len(B)):
      file1.write(["","+"][B[i] > 0] +str(B[i]) + w[i] )
file1.write("\ns.t ")
for i in range(len(A)):
    for j in range(len(A[i])):
        file1.write(["","+"][A[i][j] > 0] +str(A[i][j]) + w[j] +" " )
    file1.write(Equin[i] +" "+ str(c[i])+"\n")
file1.write("\n")
for i in wres:
    file1.write(i+" ")


file.close()
file1.close()        
            
               



