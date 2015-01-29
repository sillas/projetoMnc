SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`produtos` (
  `idproduto` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `quant` INT NOT NULL,
  `preco` FLOAT NOT NULL,
  `descricao` VARCHAR(180) NULL,
  PRIMARY KEY (`idproduto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clientes` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(15) NOT NULL,
  `dNascimento` DATE NULL,
  `endereco` VARCHAR(180) NULL,
  `e-mail` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`carrinhos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`carrinhos` (
  `idcarrinho` INT NOT NULL AUTO_INCREMENT,
  `valor_total` FLOAT NULL,
  `status` VARCHAR(45) NULL,
  `cliente` INT NOT NULL,
  PRIMARY KEY (`idcarrinho`),
  INDEX `idcliente_idx` (`cliente` ASC),
  CONSTRAINT `idcliente`
    FOREIGN KEY (`cliente`)
    REFERENCES `mydb`.`clientes` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
