
def minval(listo):       #최솟값 함수!
    mingaf = listo[0]    #받은 리스트의 첫 값을 min값으로 지정해줍니다
    for i in listo:      #listo의 모든 항목에 대해서
         if mingaf>i:    #해당 항목이 설정해놓은 min값보다 작을 경우
              mingaf =i  #min값을 해당 항목으로 갈아치웁니다!
    ## print ("minval") - 실행이 확인되는지 체크하는 메시지
    return mingaf        # 이제 min 값을 return합니다.

def sortie(num_list):            #Minimal value를 응용한 소팅 함수를 정리해 주겠습니다!
    temp = num_list[:]           #input list를 복사한 리스트, temp를 만듭니다 (원래 리스트 보호)
    sortend = []                 #그리고 sorting이 끝난 것을 담을 빈 리스트 sortend를 만들어줍니다.
    for i in range(len(temp)):   #임시 리스트의 항목 갯수만큼 반복을 합니다. 무엇을?
        min_value = minval(temp) #temp에서 최소값을 구해준 뒤에
        sortend.append(min_value)#구한 최소값을 sortend에 담아주고
        temp.remove(min_value)   #temp에서 방금 담아준 최소값을 뺍니다. 
                                 #다음 loop에는 그 다음으로 작은 게 sortend로 옮겨가겠죠?
    return sortend               #그렇게 sorting이 끝난 list, sortend를 반환해줍니다.


def main(): #.py 직접 실행해서 함수 호출 시:
    print("running directly!") #직접 출력 메시치 호출!

    listee = input ("Enter a list of numbers, divided by space: ") # 공백으로 나눠진 string 입력을 받는다
    
    if not listee: #우선 input이 없을 경우
            print("THERE IS NO INPUT!! DO IT AGAIN!!") # 에러 메시지를 출력하고
            exit() #탈출!
        
    haechae = listee.split() #string으로 있는 입력값을 공백 따라 잘라서 리스트로 만들어 줍니다.
    num_list = [] #이제 잘라진 listee를 변환해서 넣을 빈 리스트를 만들어줍니다.


    for n in haechae: #해체된 입력값으로 이루어진 리스트의 각 항목마다
        try:
            num_list.append(float(n)) #각 항목을 float로 바꿔서 num_list에 넣어줍니다.
        except ValueError as exception: # 만약 항목이 float로 변환이 안 되는 경우에는
                print("Invalid Input.", exception) #에러 메시지와 이유를 출력하기
                exit() # 탈출!

    if len(haechae) == 1:
        print("보여줄 건", haechae[0], "밖에 없구만. 값을 하나만 주고는 소팅을 하라고?") #input이 하나만 있을 때 예외상황
        exit()

    sorthetda = sortie(num_list) # num_list를 최솟값을 구해주는 함수에 넣어줍니다

    print("Sorted: ", " ".join(f"<{x}>" for x in sorthetda)) #
                     # ^ " ". : 따옴표 속: 각 항목 사이에 들어갈 구분자 (여기서는 공백)
                         #  ^ join: List, iterable의 꾸며진 요소들을 한 줄로 주욱 붙여준다 ^
                               # ^ f"<{x}>" : f-string, x 값을 문자열로 변화해서 <> 사이에 넣어줌 ^
                                        # ^ for x in ~: sorthetda의 처음~끝까지 순회하면서 하나씩... ^
 


if __name__ == "__main__": # 호출이 아니고 직접 실행되었을 시에
    main()                 #main() 을 실행해주기!


