-- rabking the countries based on the number of fans
-- we need to use sum 

SELECT origin, SUM(fans) as fans_number FROM metal_bands GROUP BY origin
HAVING fans_number != 1
ORDER BY fans_number DESC;
