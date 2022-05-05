n = int(input())
countries = {}

for _ in range(n):
    country, city = input().split()
    countries[country] = city

checked_country = input()
print(countries.get(checked_country, "Unknown Country"))

# 딕셔너리

# 나라 이름과 수도를 공백을 기준으로 입력 받아야 함.
# 그 후에 나라 이름을 치면 수도 이름이 나오게 해야함.
