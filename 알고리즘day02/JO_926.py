#두 리스트를 설정
first_array=[[int(input()), int(input()), int(input()), int(input())],[int(input()), int(input()), int(input()), int(input())]]
second_array=[[int(input()), int(input()), int(input()), int(input())],[int(input()), int(input()), int(input()), int(input())]]

#두 리스트의 곱
total = 0
for i in range(2):
    for j in range(4):
        total += first_array