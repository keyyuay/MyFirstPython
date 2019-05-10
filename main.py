#number = input("enter number :")
#print ("your lucky number is " + number )

key1 = "real"
key2 = 555568

print (type(key1))
print (type(key2))

var = "00011"
print(int(var))

float1 = 1.22
float2 = 2.44

print(int(float1 + float2))

num = 10**4 / 100+100
print (num)

print (2 == 3)

print(int(False))
print(int(True))

text1 = "cherry"
text2 = "bomp"
text3 = text1, text2
print(text3)

text = "Pythongod\n"
print(text * 10)

text1 = "yuay"
text2 = "za"
print(text1 + text2 + str(678))

age = 18
print("you are %i years old" % age )

name = "Khunyuay"
age = 18
print("My name is %s, I'm %d." % (name, age))


name = "Khunyuay"
age = 18
print("My name is %-10s, I'm %5d." % (name, age))

name = "Nirantree"
print("My name is %.4s." %name)

def main():
    result = adder(11,12)
def adder(val1, val2):
    answer = val1 * val2
    return answer
main()

print("ABC")

call = "1150"
if (call == "1150"):
    print("Pizza hut")
else :
    print("Pizza company")

num = 0
while num < 5:
    print(num)
    num += 1

print("\n")

for i in "Goddest":
    print(i)

print("\n")

for i in range(10,20):
    print(i)

print("\n")

for i in range(100):
    print(i, end=" key ")
    if i == 5:
        break

print("\n")

for i in range(10):
    if i == 5:
        continue
    print(i)

print("\n")
