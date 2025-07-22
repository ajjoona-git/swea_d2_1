T = int(input())

for test_case in range(1, T+1):
    # 각 테스트 케이스 받아오기
    N = int(input())
    price_list = list(map(int, input().split()))
    max_price = 0
    profit = 0
	
    # 뒤에서부터 순회하면서 최대값 저장
    # 최대값과 현재값의 차이만큼 이익으로 계산
    for i in range(N-1,-1,-1):
        if price_list[i] > max_price:
            max_price = price_list[i]
        else:
            profit += max_price - price_list[i]
            
    print(f'#{test_case} {profit}')