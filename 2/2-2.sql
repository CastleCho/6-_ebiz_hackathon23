SELECT c.first_name, c.last_name, o.item, o.amount  # 데이터의 first_name, last_name, item, amount 데이터를 이용
FROM Customers c #Customers 테이블을 c라 선언한 후 이용
JOIN Orders o ON c.customer_id = o.customer_id; # Customers 테이블과 Orders 테이블을 customer_id를 기준으로 Join함으로써 주문 내역에 id가 존재하는 customer 데이터만을 이용할 수 있게 함. #Orders 테이블을 o라고 선언한 후 이용
