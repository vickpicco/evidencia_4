CREATE SCHEMA IF NOT EXISTS `maquina_de_bolsos` DEFAULT CHARACTER SET utf8mb4;
USE `maquina_de_bolsos`;

CREATE TABLE IF NOT EXISTS `maquina_de_bolsos`.`Materiales` (
  `idMaterial` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idMaterial`)
);

CREATE TABLE IF NOT EXISTS `maquina_de_bolsos`.`Colores` (
  `idColor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idColor`)
);

CREATE TABLE IF NOT EXISTS `maquina_de_bolsos`.`Tamaños` (
  `idTamaño` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NULL,
  PRIMARY KEY (`idTamaño`)
);

CREATE TABLE IF NOT EXISTS `maquina_de_bolsos`.`Bolsos` (
    `idBolsos` INT NOT NULL AUTO_INCREMENT,
    `material_id` INT,
    `color_id` INT,
    `tamaño_id` INT,
    `piezas_cortadas` BOOLEAN,
    `piezas_cocidas` BOOLEAN,
    PRIMARY KEY (`idBolsos`),
    FOREIGN KEY (`material_id`) REFERENCES `Materiales`(`idMaterial`),
    FOREIGN KEY (`color_id`) REFERENCES `Colores`(`idColor`),
    FOREIGN KEY (`tamaño_id`) REFERENCES `Tamaños`(`idTamaño`)
);