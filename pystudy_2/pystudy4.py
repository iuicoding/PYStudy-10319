while True:
 string_input = input("정수 입력>")
 if string_input.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름":, number_input_a)
        print("원의 둘레:", 2 * 3.14 * number_input_a)
        print("원의 넓이:", 3.14 *number_input_a * number_input_a)
    break
else:
    print("점수를 입력해주세요!")
    #변수를 선언합니다
    list_input_a = ["52", "273", "32","스파이", "103"]

 #반복을 적용합니다.
 list_number = []
 for item in list_input_a:
     # 숫자로 변환해서 리스트에 추가합니다.
    try:
        float(item) # 예외가 발생하면 알아서 다음으로 진행은 안 되겠지?
        list_naumber.append(item) #예외없이통과했으면리스트에 넣어줘!
    expect:
    pass

     # 출력합니다.
     print("{} 내부에 있는 숫자는".format(list_input_a))
     print("{}입니다.".format(list_number))

    #반복을 적용합니다
    # test() 함수를 선언합니다
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        ㅇㅂㅇ.ㅇㅂㅇ()
        print("try 구문이 return 키워드 뒤입니다")
    excspt:
        print("except 구문이 실행되었습니다.")
     return
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의마지막 줄입니다.")
# test() 함수를 호출합니다.
test()

#학생 리스트를 선언합니다.
 students = []