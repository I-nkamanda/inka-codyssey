# 우선 사칙연산 함수를 정의하기

def add (a, b): #덧셈 함수
    return a + b

def subtract (a, b): #뺄셈 함수
    return a - b

def multiply (a, b): #곱셈 함수
    return a * b

def divide (a, b): #나눗셈 함수
    if b == 0: #Division by zero를 예외상황으로 빼주기
        print ("Error: Division by zero.") #에러메시지 출력
        exit () #탈출!
    else:
        return a / b

def main(): #main 정의
    print ("Running calculator itself!") #import되지 않고 직접 실행 시 나오는 메시지

expres = input("Enter expression (example: 13 * 21.45):") # space로 나뉜 (숫자) (연산자) (숫자) 형식의 입력을 받음 (형태 string)

print ("You have entered:", expres) #입력한 expression의 확인
print(type(expres)) # 방금 입력한 expres는 string임을 확인할 수 있습니다.

parts= expres.split() #위에서 받은 string expression을 space를 기준으로 list로 잘라준다. 예시: "i am good".split()-> ['i', 'am', 'good'] 이라는 list로 나누어짐

print (parts) #expres 가 잘 나눠졌는지 출력을 해 보고...
print(type(parts)) # parts의 class는 list 임을 알 수 있습니다.

#(arg 1) (arg 2) (arg 3)의 형태가 아닌 입력 (예를 들어서 "12-+23", "135 112"나, "e + 34 - 16" 등등)을 걸러내는 부분
count =0 #카운터를 0으로 세팅합니다.
for i in parts: #list의 항목 갯수만큼
    count += 1 #1씩 더해 나가줍니다. (항목이 3개면 3, 4개면 4 이런 식으로)

if count !=3: # (arg1) (arg2) (arg3) 형식으로 항목이 3개인 리스트가 아니라면
      print ("ERROR: The expression must take the form of 'number' 'operator' 'number' divided by space!") #예외 처리를 해 주고, 
      exit() #탈출!

# 3항목 테스트를 통과한 list 내용물들을 변수로 지정하는 부분
a = parts[0] #a =  리스트 1번째
operator = parts [1] # 연산자 = 리스트 2번째
b = parts [2] # b = 리스트 3번째

#자료형을 확인해보면 a, operator, b 모두 string임을 알 수 있답니다.
print (type (a), a)
print (type (operator), operator)
print (type (b), b)

#계산을 위해 string이었던 a, b를 float로 변환해 주는 부분!
try: 
    a = float (a) #우선 a의 자료형을 float로 바꿔 보고
except ValueError: #float로 변환할 수 없는 자료형일 경우에는
    print ("ERROR: 1st number Expression error!") #예외상황이니 에러 메시지 출력
    exit() #탈출!

print("1st number is:",type(a), a) # a 자료형 변화 체크!

try:
     b=float(b)  #우선 b의 자료형을 float로 바꿔 보고
except ValueError: #float로 변환할 수 없는 자료형일 경우에는 (2)
      print ("ERROR: 2nd number Expression error!") #예외상황이니 에러 메시지 출력 (2)
      exit() #탈출! (2)

print ("2nd number is: ", type(b), b) #b 자료형 변화 체크! (2)


#이제 opeator가 무엇인지에 구분하고, 거기에 따라 a, b값을 각각의 함수에 넘겨주거나 예외처리 하는 부분

if operator == "+": #덧셈이면
        print(f"Result: <{add (a, b)}>") #덧셈 함수에 넣고 리턴 값을 출력!
elif operator == "-": #뺄셈이면
        print(f"Result: <{subtract (a, b)}>") #뺄셈 함수에 넣고 리턴 값을 출력!
elif operator == "*": #곱셈이면
        print(f"Result: <{multiply (a, b)}>") #곱셈 함수에 넣고 리턴 값을 출력!
elif operator == "/": #나눗셈이면
        print(f"Result: <{divide (a, b)}>") #나눗셈 함수에 넣고 리턴 값을 출력!
else: #연산자가 그 중에 아무 것도 아니라면:
        print ("ERROR: Invalid operator.") #에러 메시지 출력 후
        exit() #탈출!


    
if __name__ == "__main__": #파일을 직접 실행할 때 __name__값이 "__main__"으로 설정되기 때문에 직접 실행인지 import된 것인지 알 수 있다. (import되었을 때에는 __name__ = "파일 이름")
    main() #그래서 직접 실행과 다른 파일에서 호출되는 상황을 구분할 수가 있다