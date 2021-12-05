mylist = [num**2 for num in range(0,11) if num % 2 ==0]
print(mylist)

celcius = [0,10,20,34.5]
fahrenheit = [ ( (9/5)*temp + 32 ) for temp in celcius]

for temp in celcius:
    fahrenheit.append(( (9/5)*temp + 32 ))

print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range (0,11)]

asd= []
for x in [2,4,6]:
    for y in [100,200,300]:
        asd.append(x*y)
        
alternative = [x*y for x in [2,4,6] for y in [1,10,100]]
