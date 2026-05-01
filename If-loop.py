#example of if-else statement
i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")

#lab examples

var1 = True

if var1:
    print("var1")
else:
    print("var1 is not true")


for i in range(0, 10, 1):
    print(i)
for i in range(0, 10):
    print(i)
for i in range(10):
    print(i)

s = "Hello World"

for i in s:
    print('current Letter:', i)

print(range(10))

a = ['Kirtan' , 'Rydham', 'Ahmedabad']
print(len(a))

for i in range(len(a)):
    print(i,a[i])

for i in range(20,30):
    print("index",i)
else:
    print("in else part")
    print("Hello") 

ls = ["hello" for x in range (5)]
print(ls)

for i in range(10):
    for j in range(20,30):
        print("j>>",j)

    print("i",i)

count = 0

while count < 10:
    print(count)
    count += 1
else:
    print("count value reached to 10")
    print("count value is", count)