l = []

n = int(input("Enter the numbers of persons standing in a row infront of devil:"))

for i in range(1,n+1):
    l.append(i)

print(l)
print()
print()

while(len(l)!=1):
    l = l[1:len(l):2]

print("The person position saved finally is:",l)
