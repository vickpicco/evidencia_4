SELECT * FROM maquina_de_bolsos.bolsos WHERE piezas_cocidas = TRUE AND piezas_cortadas = TRUE;

SELECT * FROM maquina_de_bolsos.bolsos WHERE piezas_cocidas = FALSE AND piezas_cortadas = FALSE;

SELECT * FROM maquina_de_bolsos.bolsos WHERE piezas_cocidas = TRUE AND piezas_cortadas = FALSE;

SELECT * FROM maquina_de_bolsos.colores ORDER BY nombre;

SELECT * FROM maquina_de_bolsos.materiales WHERE nombre LIKE '%a%';

SELECT * FROM maquina_de_bolsos.tamaños;



