## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
## Any code taken from other sources is referenced within my code solution.
## Student ID: 18179956
## Date: 3/11/21

#Part 1(Main Version) 
#Outcomes

Pass = int(input("Please enter your credits at pass: "))
Defer = int(input("Please enter your credits at defer: "))
Fail  = int(input("Please enter your credits at fail: "))
if Pass == 120:
          print("Progress")
elif Pass == 100:
          print("Progress (module trailer)")
elif Pass == 80 or Pass == 60 or Pass == 40  or Defer == 40:
    print("Module retriever")
elif Pass == 20 or Pass == 0 or Fail == 80 or Defer == 0 or Defer == 60 or Fail == 20:
      print("Exclude")

#Validation

#Integer Required
try:    
   Pass = int(input("Please enter your credits at pass: "))
   Defer = int(input("Please enter your credits at defer: "))
   Fail  = int(input("Please enter your credits at fail: "))
except ValueError:
    print("Integer required")

#Out of range
Pass = int(input("Please enter your credits at pass: "))
for i in range(0,121,20):  #prints in range 0,20,40,60,80,100,120 in 20 steps
               if i != Pass:
                         print("Out of range")
                         break

#Total Incorrect        
Pass = int(input("Please enter your credits at pass: "))
Defer = int(input("Please enter your credits at defer: "))
Fail  = int(input("Please enter your credits at fail: "))
sum = Pass + Defer + Fail
if sum != 120:     #prints total incorrect if pass,defer,fail altogether is not equal to 120
    print("Total incorrect")

#Multiple outcomes and histogram

print("Staff version with Histogram")
progress = 0
progress_list = []
module_trailer = 0
module_trailer_list = []
module_retriever = 0
module_retriever_list = []
exclude = 0
exclude_list = []
finish = True
while finish:
   Pass = int(input("Enter your total PASS credits: "))
   Defer = int(input("Enter your total DEFER credits: "))
   Fail  = int(input("Enter your total FAIL credits: "))
   if Pass == 120:        #goes through the loop and adds 1 to progress
              print("Progress")
              progress += 1
              progress_list.append(Pass)
              progress_list.append(Defer)
              progress_list.append(Fail)
   elif Pass == 100:      #goes through the loop and adds 1 to module_trailer
              print("Progress (module trailer)")
              module_trailer += 1
              module_trailer_list.append(Pass)
              module_trailer_list.append(Defer)
              module_trailer_list.append(Fail)
   elif Pass == 80 or Pass == 60 or Pass == 40 or Defer == 40:   #goes through the loop and adds 1 to module_retriever
        print("Module retriever")
        module_retriever += 1
        module_retriever_list.append(Pass)
        module_retriever_list.append(Defer)
        module_retriever_list.append(Fail)
   elif Pass == 20 or Pass == 0 or Defer == 60 or Defer == 0 or Fail == 80 or Fail == 20:     #goes through the loop and adds 1 to exclude
        print("Exclude")
        exclude += 1
        exclude_list.append(Pass)
        exclude_list.append(Defer)
        exclude_list.append(Fail)
   print("Would you like to enter another set of data?")
   User = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
   if User == 'y':  #if user enters yes it will continue from the top 
      continue
   else:            #if user enters quit it will break out of the loop
      break

#Horizontal Histogram

print("-----------------------------------------------------")
print("Horizontal Histogram")
hor_his = ["Progress","Trailer","Retriever","Excluded"]
hor_values = [progress,module_trailer,module_retriever,exclude]
for i,j in zip(hor_his,hor_values):
    print(i,j * '*',end='  ')    #prints stars horizontally
    print()
count = progress + module_trailer + module_retriever + exclude
print(count,"outcomes in total.")
print("------------------------------------------------------")

#Part 2 - Vertical histogram(extension)

def histogram(data):  #taken from stackoverflow.com/questions/43563672/python-plotting-a-histogram-downward at 21/11/21
    return '\n'.join('           '.join('*' if depth>row else ' ' for depth in data)               
        for row in range(max(data)))
   
print("Progress  Trailer  Retriever  Excluded") 
print(histogram((progress,module_trailer,module_retriever,exclude))) #print stars vertically
print(count,"outcomes in total.")

#Part 3 - Lists/tuples/directory(extension)

n = 3
Q = (progress_list[i:i+n] for i in range(0,len(progress_list),n))
for p in Q:
   print("Progress -",end='')
   print(*p,sep=',')

m = 3
A = (module_trailer_list[j:j+m] for j in range(0,len(module_trailer_list),m))
for q in A:
   print("Progress (module trailer) -",end='')
   print(*q,sep=',')

u = 3
S = (module_retriever_list[k:k+u] for k in range(0,len(module_retriever_list),u))
for r in S:
   print("Module retriever -",end='')
   print(*r,sep=',')

o = 3
T = (exclude_list[l:l+o] for l in range(0,len(exclude_list),o))
for s in T:
   print("Exclude -",end='')
   print(*s,sep=',')

#Part 4 - Text file

f = open('w1817995.py','w')
f.write("Progress - 120,0,0\n")
f.write("Progress (module trailer) - 100,0,20\n")
f.write("Module retriever - 80,20,20\n")
f.write("Module retriever - 60,0,60\n")
f.write("Exclude - 40,0,80\n")
f.close()

fer = open('w1817995.py')
line = fer.read()
fer.close()
print(line)


   
