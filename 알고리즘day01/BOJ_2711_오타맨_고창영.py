t = int(input())  # 오타, 단어를 입력받는 변수

for i in range(t):  # 입력받은 수만큼 반복
    index, word = input().split()  # 숫자와 단어 모두 문자열로 받음
    index = int(index)  # 입력받은 숫자를 "정수형으로 바꾸는 코드"
    # index-1을 제외한 이전 문자들을 출력하고 index부터 끝까지 출력하라
    print(word[:index - 1] + word[index:])
