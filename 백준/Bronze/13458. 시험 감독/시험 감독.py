import math

N = int(input()) #시험장 갯수
Class_array = list(map(int, input().split())) # 시험장 당 응시자 수 리스트업
B, C = map(int, input().split()) #감독관이 감시하는 응시자 수(총, 부)

#총 필요 감독관 수 변수
person = 0

#총감독이 감시하고 남은 학생 수 
for students in Class_array:
    students -= B #총 감독관 배치 후 남은 학생 수 
    person += 1 
    
    if students > 0:
        person = person + math.ceil(students / C)


#총 필요 감독관 수 출력
print(person)

