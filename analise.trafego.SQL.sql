-- consulta de todas as colunas da tabela
SELECT *
FROM local_authority_traffic
LIMIT 10;

-- Intervalo anos analisados
SELECT MIN(year), MAX(year)
FROM local_authority_traffic;

-- Média de veículos por ano
SELECT
    year,
    AVG(all_motor_vehicles) AS media_veiculos
FROM local_authority_traffic
GROUP BY year
ORDER BY year;

-- 10 regiões com maior número de carros e táxis
SELECT
    local_authority_name,
    SUM(cars_and_taxis) AS total_carros
FROM local_authority_traffic
GROUP BY local_authority_name
ORDER BY total_carros DESC
LIMIT 10;

-- Regiões que possuem maior volume de tráfego
SELECT
    local_authority_name,
    year,
    all_motor_vehicles
FROM local_authority_traffic
ORDER BY all_motor_vehicles DESC
LIMIT 10;