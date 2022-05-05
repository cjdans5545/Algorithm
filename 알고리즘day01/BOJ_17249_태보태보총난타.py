left, right = input().split("(^0^)")#오른쪽과 왼쪽을 지정하는 변수를 받고
                                # input함수로 입력을 받고 split함수로 (^0^)를
                                #기점으로 @의 수를 센다
print(left.count("@"), right.count("@"))#왼쪽 오른쪽의 @ 수를 센다
