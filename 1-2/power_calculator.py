
def main(): #main 정의
    print ("Running calculator itself!") #import되지 않고 직접 실행 시 나오는 메시지

if __name__ == "__main__": #파일을 직접 실행할 때 __name__값이 "__main__"으로 설정되기 때문에 직접 실행인지 import된 것인지 알 수 있다. (import되었을 때에는 __name__ = "파일 이름")
    main() #그래서 직접 실행과 다른 파일에서 호출되는 상황을 구분할 수가 있다


num = input ("Enter Number: ") # 숫자를 받는다
try:
    num = float(num) #입력을 float로 변환을 시도해 본다
except ValueError: #입력이 float로 변환 불가할 경우 분기
    print ("Invalid number input.") #예외처리
    exit() # 종료

exp = input ("Enter exponent: ") #지수를 받는다

try:
    exp = int(exp) #exp 입력을 int로 변환을 시도해 본다
except ValueError: #int 변환이 불가할 경우 분기
    print ("Invalid exponent input.") # 예외처리
    exit() # 종료
    

if (num == 0 and exp <= 0): #0을 0으로 나누는 케이스를 예외처리
    print ("Division of zero by zero? Cannot do that, man") #예외처리
    exit() #종료

result =1 #결과값을 initialize해준다

if exp < 0: #지수가 음수일 경우 (exp 번 나눠주는 케이스)
    for i in range (abs(exp)): #음수 지수의 절대값 횟수만큼
        result = result/num # result(1)에다 숫자를 나눠준다
else: #지수가 양수거나 0일 경우
    for i in range(exp): #지수의 횟수만큼
        result *= num # result (1)에다가 숫자를 곱해준다.

print ("Result: ", result ) #결과값을 출력한다.

