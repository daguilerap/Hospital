-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingresos`
--

DROP TABLE IF EXISTS `ingresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingresos` (
  `coding` int NOT NULL,
  `procedencia` varchar(45) DEFAULT NULL,
  `fecha_ingreso` varchar(45) DEFAULT NULL,
  `num_planta` int DEFAULT NULL,
  `num_cama` int DEFAULT NULL,
  `observaciones` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`coding`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingresos`
--

LOCK TABLES `ingresos` WRITE;
/*!40000 ALTER TABLE `ingresos` DISABLE KEYS */;
INSERT INTO `ingresos` VALUES (1,'Aljarafe','11/02/2021',1,345,'Mas malito'),(2,'Sevilla','11/02/2021',2,23,'Malito'),(3,'San Juan','02/01/2021',1,12,'Pocho'),(4,'Alcala','02/01/2021',3,45,'Malito'),(5,'Mairena','01/03/2021',2,1,'Malito'),(6,'Sevilla','15/02/2000',2,36,'Malito'),(7,'Sevilla','20/02/2000',2,34,'Pocho');
/*!40000 ALTER TABLE `ingresos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicos`
--

DROP TABLE IF EXISTS `medicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicos` (
  `codmed` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `especialidad` varchar(45) DEFAULT NULL,
  `num_colegiado` varchar(45) DEFAULT NULL,
  `cargo` varchar(45) DEFAULT NULL,
  `observaciones` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codmed`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicos`
--

LOCK TABLES `medicos` WRITE;
/*!40000 ALTER TABLE `medicos` DISABLE KEYS */;
INSERT INTO `medicos` VALUES (1,'Miguel','Romero','Medicina General','125','ayudante','Ninguna'),(2,'Antonio','Carmona','Medicina General','25','jefe','Ninguna'),(3,'Manuel','Buenao','Especialista','98','ayudante','Ninguna');
/*!40000 ALTER TABLE `medicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `codpac` int NOT NULL,
  `numseg` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `domicilio` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `poblacion` varchar(45) DEFAULT NULL,
  `cp` int DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `numhist` int DEFAULT NULL,
  `observa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`codpac`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (1,4564654,'David','Martin','Sevilla','Sevilla','Dos Hermanas',41100,'652345067',12,'Malito'),(2,4564649,'José','Casetellano','Sevilla','Sevilla','Dos Hermanas',41100,'695921067',12,'lalala'),(3,4564649,'Rafael','Morata','C/Abelardo','Sevilla','Dos Hermanas',41704,'695996898',236,'Malito'),(4,4564649,'Juan José','Gonzalez','C/Ruidera','Sevilla','San Juan',41100,'695996898',698,'Malito');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-06 19:03:29
