import os

f=open("title.txt","r")
#read whole file
print(f.read())


#read charcter from the file
print(f.read(1))


#read line method
print(f.readline())

print(f.readlines())

#one line after other
for x in f:
 print(x)

f1=open("title.txt","a")
f1.write("a line is new")
f1=open("title.txt","r")
print(f1.read())
f1.close()


#create new file
#f2=open("new.txt","x")
f3=open("trial.txt","r")
os.remove("trial.txt")
f4=open("demo.txt","r")


if os.path.exists("title.txt"):
    os.remove("title.txt")
else:
    print("file is not present")
