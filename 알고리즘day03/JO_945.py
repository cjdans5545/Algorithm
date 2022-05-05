animation = input()
#애니메이션 변수에 입력받음
animations = {
    "Pokemon": "Pikachu",
    "Digimon": "Agumon",
    "Yugioh": "Black Magician"
}
#딕셔너리
print(animations.get(animation, "I don't know"))
#애니메이션스 딕셔너리에서 애니메이션 값을 추출한다. 해당 값이 없으면 I don't know를 01.출력.