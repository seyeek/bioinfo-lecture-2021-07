
file_name = "read_sample.txt"

#with open(file_name,"r") as handle:
#    for line in handle:
#        print(line)    
 #line안에 엔터가 있고 프린트에도 엔터가 있기 때문에 두개의 엔터가 나온다
 #이를 수정하고 싶다면 print(line.strip())

#for line in handle:
#    print(line.strip())
#handle.close()


handle = open(file_name,"r")
lines = handle.readlines()
for line in lines:
    print(line.strip())
handle.close()



