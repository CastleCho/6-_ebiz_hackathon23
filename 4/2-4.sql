SELECT country as "나라",count(customer_id) as "고객수", avg(age) as "평균나이"
FROM Customers
GROUP BY country
ORDER BY 평균나이 desc