INSERT INTO `Materiales` (`nombre`) VALUES 
('Cuero'), 
('Tela'), 
('Sintético'), 
('Lona'), 
('Malla');

INSERT INTO `Colores` (`nombre`) VALUES 
('Rojo'), 
('Azul'), 
('Verde'), 
('Negro'), 
('Blanco');

INSERT INTO `Tamaños` (`nombre`) VALUES 
('Pequeño'), 
('Mediano'), 
('Grande'), 
('Extra Grande'), 
('Mini');

INSERT INTO `Bolsos` (`material_id`, `color_id`, `tamaño_id`, `piezas_cortadas`, `piezas_cocidas`) VALUES 
(1, 1, 1, TRUE, FALSE), 
(2, 2, 2, TRUE, TRUE), 
(3, 3, 3, FALSE, TRUE), 
(4, 4, 4, TRUE, TRUE), 
(5, 5, 5, FALSE, FALSE), 
(1, 2, 3, TRUE, TRUE), 
(2, 3, 1, FALSE, TRUE), 
(3, 4, 2, TRUE, FALSE), 
(4, 5, 4, TRUE, TRUE), 
(5, 1, 5, FALSE, FALSE);