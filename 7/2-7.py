def min_moves(n):
    
    factors = [(i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    # 문제에서 주어진 곱셈표는, i행 j열이라고 표현했을 때 그 값이 i*j 이므로, 어떤 수에 대하여 그 수의 어떤 약수와 그 수를 약수로 나눈 수와의 곱에 그 수가 위치한다고 볼 수 있다.
    # 한 수를 그 약수끼리의 곱의 순서쌍으로 표현할 때, 1부터 그 수의 제곱근까지 약수를 구하면 모든 약수끼리의 순서쌍을 구할 수 있다.
    min_distance = float('inf')
    # 순서쌍들로 구하는 거리들 중 첫 번째로 구한 거리가 바로 min_distance로 지정되게 하기 위해 min_distance의 default 값을 무한대로 설정해놓음.
    for factor in factors:
       
        distance = (factor[0] - 1) + (factor[1] - 1)
        min_distance = min(min_distance, distance)
        #거리를 구해 이전에 구한 거리와 새로 구한 거리 중 더 짧은 거리를 min_distance로 할당함.
    return min_distance

print(min_moves(12))  
print(min_moves(16))  
print(min_moves(29))  
