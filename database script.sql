-- -----------------------------------------------------
-- Table `mydb`.`produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `produtos` (
  `idproduto` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `quant` INT NOT NULL,
  `preco` FLOAT NOT NULL,
  `descricao` VARCHAR(180) NULL,
  PRIMARY KEY (`idproduto`))
;


-- -----------------------------------------------------
-- Table `mydb`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clientes` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NULL,
  `cpf` VARCHAR(15) NOT NULL,
  `dNascimento` DATE NULL,
  `endereco` VARCHAR(180) NULL,
  `e-mail` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcliente`))
;


-- -----------------------------------------------------
-- Table `mydb`.`carrinhos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carrinhos` (
  `idcarrinho` INT NOT NULL AUTO_INCREMENT,
  `valor_total` FLOAT NULL,
  `status` VARCHAR(45) NULL,
  `cliente` INT NOT NULL,
  PRIMARY KEY (`idcarrinho`),
  INDEX `idcliente_idx` (`cliente` ASC),
  CONSTRAINT `idcliente`
    FOREIGN KEY (`cliente`)
    REFERENCES `clientes` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;