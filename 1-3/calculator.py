# 함수를 정의하는 부분
def add (a, b): #add 함수 정의. a와 b의 값을 받아서 a+b를 리턴한다.
    return a + b

def subtract (a, b): #subtract 함수 정의. a와 b의 값을 받아서 a-b를 리턴한다.
    return a - b

def multiply (a, b): #multiply 함수 정의. a와 b의 값을 받아서 a*b를 리턴한다.
    return a * b

def divide (a, b): #divide 함수 정의. a와 b의 값을 받아서 a/b를 리턴한다.
    if b == 0:
        print ("Error: Division by zero.") #0으로 나눌 때의 예외 처리
        exit () #탈출!
    else:
        return a / b

def main(): #main 정의
    print ("Running calculator itself!") #import되지 않고 직접 실행 시 나오는 메시지



    a = input ("Enter the first number: ") #첫 번째 입력값을 받는다

    try:
        a= float(a) #a 를 float 자료형으로 변환해 본다.
    except ValueError: #string 등 float으로 변환이 안 되는 경우에는
        print ("Error: Invalid Input!") #예외처리
        exit () #탈출!

    b = input ("Enter the second number: ") #두 번째 입력값을 받는다.
    try:
        b= float(b) #a 를 float 자료형으로 변환해 본다.
    except ValueError: #string 등 float으로 변환이 안 되는 경우에는 (2)
        print ("Error: Invalid Input!") #예외처리 (2)
        exit () #탈출! (2)


    operator = input ("Enter the operator (+, -, *, /): ") #이제 연산자 입력값을 받는다.
    if operator == "+": #더하기라면
        print(f"Result: <{add (a, b)} >") #덧셈 함수에 넣어주고

    elif operator == "-": #빼기라면
        print(f"Result: <{subtract (a, b)}>") #뺄셈 함수에 넣어주고

    elif operator == "*": #곱하기라면
        print(f"Result: <{multiply (a, b)}>") #곱셈 함수에 넣어주고

    elif operator == "/": #나누기라면
        print(f"Result: <{divide (a, b)}>") #나눗셈 함수에 넣어준다!

    else: #4개 전부 아니라면
        print ("Invalid operator.") #위 네 개의 연산자에 포함되지 않는 다른 input은 예외처리.
        exit() #탈출!

    
if __name__ == "__main__": #파일을 직접 실행할 때 __name__값이 "__main__"으로 설정되기 때문에 직접 실행인지 import된 것인지 알 수 있다. (import되었을 때에는 __name__ = "파일 이름")
    main() #그래서 직접 실행과 다른 파일에서 호출되는 상황을 구분할 수가 있다