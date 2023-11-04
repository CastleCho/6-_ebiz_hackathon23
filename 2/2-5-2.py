def output():
    for i in range(8, 0, -2):
        print(('*' * i).center(8))
    # 8부터 2씩 2까지 줄어들며 각 값 만큼 별을 출력하게 하고, 너비 8을 기준으로 가운데 정렬
    
    for i in range(4, 10, 2):
        print(('*' * i).center(8))
    # 4부터 8까지 2씩 늘어나며 각 값 만큼 별을 출력하게 하고, 너비 8을 기준으로 가운데 정렬
    
output()
# 함수 실행
