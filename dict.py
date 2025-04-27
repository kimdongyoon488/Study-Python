# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고 2월을 29일로 수정
month_end_days = {'1월':31, '2월':28,'3월':31,'4월':30,'5월':31,'6월':30}

month_end_days["2월"] = 29

print(month_end_days)

# 딕셔너리에 각 달의 마지막 날들을 한번에 담고,
# update를 사용하여, 2월 29일로 수정하고 4월,5월의 정보도 추가

month_end_days1 = {"1월":31, "2월":28,"3월":31}
month_end_days2 = {"2월":29, "4월":30,"5월":31}

month_end_days1.update(month_end_days2)
print(month_end_days1)