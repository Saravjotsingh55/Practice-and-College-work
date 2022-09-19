#a program to show working with touples
print("code written by: Saravjot Singh,2003249","\n")
tuple1=("hello",1234,True,23.42)
tuple2=("this is a string",321.44,2)


print("tuple1 created: ",tuple1,"\n")

print("tuple2 is unsuccessfully appended in tuple1 because tuples are imuutable: ",tuple1,"\n")
tuple1.append(tuple2)             #appending



tuple1.clear()
print("elements of tuple1 are cleared: ",tuple1,"\n")        

