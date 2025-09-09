-- 02_sample_queries.sql
-- Exemplos para validar o esquema e fazer análises rápidas.

-- Leituras por sensor (contagem)
SELECT sensor_id, COUNT(*) AS total_readings
FROM reading
GROUP BY sensor_id
ORDER BY total_readings DESC;

-- Média de leitura por máquina (supondo junção por sensor -> machine)
SELECT m.machine_id, AVG(r.value) AS avg_value
FROM reading r
JOIN sensor s ON s.sensor_id = r.sensor_id
JOIN machine m ON m.machine_id = s.machine_id
GROUP BY m.machine_id
ORDER BY m.machine_id;

-- Leituras anômalas (se mantidas na tabela label)
SELECT l.sensor_id, l.reading_time, l.status
FROM label l
WHERE l.status = 'ANOMALO'
ORDER BY l.reading_time DESC;
