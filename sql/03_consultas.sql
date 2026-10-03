--- Realizando consultas basicas 

--- SELECT basico
SELECT * 
FROM bronze b;

---------------

--- SELECT com filtro
SELECT * 
FROM bronze b
WHERE b."Customer type" = 'Member';

---------------

--- SELECT utilizando GROUP BY e COUNT
SELECT 
	b."Product line", 
	count (*) AS total_vendas 
FROM bronze b 
GROUP BY b."Product line"; 

---------------

--- SELECT utilizando GROUP BY e SUM
SELECT
	b."Branch", 
	SUM(b."Sales") AS total_vendas
FROM bronze b 
GROUP BY b."Branch";

---------------

--- SELECT utilizando GROUP BY e AVG    
SELECT
	AVG(b."Tax 5%" ) AS imposto_medio
FROM bronze b; 

---------------

--- SELECT utilizando MIN e MAX
SELECT
	MIN(b."Rating") AS avaliacao_minima,
	MAX(b."Rating") AS avaliacao_maxima
FROM bronze b;

---------------

--- SELECT utilizando ORDER BY
SELECT
	b."Customer type",
	b."Product line", 
	b."Payment",
	b."Quantity",
	b."Sales"
FROM bronze b
ORDER BY b."Sales" DESC
LIMIT 5;

---------------

--- SELECT utilizando WHERER
SELECT
	b."Customer type",
	b."Payment",
	b."Sales"
FROM bronze b
WHERE b."Customer type" = 'Member'
  AND b."Payment" IN ('Cash')
  AND b."Sales" > 800;