
def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        print ("Error: Division by zero.")
        exit ()
    else:
        return a / b

def main(): #main 정의
    print ("Running calculator itself!") #import되지 않고 직접 실행 시 나오는 메시지

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
    print ("ERROR: 1st number Expression error!")
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



if operator == "+":
        print(f"Result: <{add (a, b)}>")

elif operator == "-":
        print(f"Result: <{subtract (a, b)}>")
elif operator == "*":
        print(f"Result: <{multiply (a, b)}>")
elif operator == "/":
        print(f"Result: <{divide (a, b)}>")
else:
        print ("ERROR: Invalid operator.")
        exit()



print( "Breakpoint 2")

    
if __name__ == "__main__": #파일을 직접 실행할 때 __name__값이 "__main__"으로 설정되기 때문에 직접 실행인지 import된 것인지 알 수 있다. (import되었을 때에는 __name__ = "파일 이름")
    main() #그래서 직접 실행과 다른 파일에서 호출되는 상황을 구분할 수가 있다