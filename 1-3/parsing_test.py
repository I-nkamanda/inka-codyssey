expres = input("enter expression (example: 13 * 21.45):")

print(type(expres))

parts= expres.split()

print (parts)

print(type(parts))
count =0
for i in parts:
    count += 1

print("number is:", count)

if count !=3:
      print ("ERROR: The expression must take the form of 'number' 'operator' 'number' divided by space!")
      exit()

a = parts[0]
operator = parts [1]
b = parts [2]

print (type (a), a)

print (type (operator), operator)

print (type (b), b)

try:
    a = float (a)
except ValueError:
    print ("Expression error!")
    exit()

print("1st expression is:",a)


try:
     b=float(b)
except ValueError:
      print ("Expression error!")
      exit()

print ("2nd expression is: ", b)

print ("operator is:", operator)


print (type (a), a)

print (type (operator), operator)

print (type (b), b)


print( "Breakpoint 1")



exit()

if operator == "+":
        print(f"Result: <{add (a, b)} >")

elif operator == "-":
        print(f"Result: <{subtract (a, b)}>")
elif operator == "*":
        print(f"Result: <{multiply (a, b)}>")
elif operator == "/":
        print(f"Result: <{divide (a, b)}>")
else:
        print ("Invalid operator.")
        exit()

