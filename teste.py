""" 
        * item:
        - Nome do produto:
        - dict{preco, descricao**, estoque, categoria, Id_cod.}

        *categoria**:
        - categoria:
        - [itens (nomes dos itens, apenas)]

        ** Estrutura no BD:
        Formato: "categoria,descricao" 


        CREATE TABLE produtos(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150),
            quant INTEGER,
            descricao VARCHAR(150), #500!
	    preco DOUBLE
       )

Comando correto para inserir produto:
        c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("agua", 10, "bebidas,ok", 2.30))
	c.execute( "INSERT INTO produtos (nome, quant, preco, descricao) VALUES ('%s', %d, %f,'%s')" % ("agua", 10, 2.30, "bebidas,ok"))
"""
class Produtos:
    def __init__(self):
        self.produto = {}
        self.categoria = {}

    def updateProdutoList(self):
        import MySQLdb #mudar de posicao
        try:
            con = MySQLdb.connect(host="10.5.18.40", user="root", passwd="admin", db="loja_pet")
        except:
            print 'Erro na conexcao com o banco de dados!'
            return 'BD_Con_Erro'
        
        c = con.cursor()
	c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("agua", 100, "bebidas, garrafa iL", 2.30))
	c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("manga", 105, "frutas,manga verde", 0.10))
	c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("abacate", 230, "frutas,abacate de fulano", 0.30))
        c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("frango", 30, "frios,peito de frango", 5.00))
        c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("leite", 10, "frios,leite integral", 1.70))
        c.execute( "INSERT INTO produtos (nome, quantidade, descricao, preco) VALUES ('%s', %d, '%s', %f)" % ("Refri", 35, "bebidas,1L", 3.30))
        c.execute("SELECT * FROM produtos")


        #preencher os dicionarios com os dados do banco para acesso rapido:
        for item in c: 
	    id_Prod, item, estoque, descricao, preco = item
            
            #preenche dict Categoria
            for i in range(len(descricao)): #extrai a categoria do produto do campo produto_descricao
                if descricao[i] == ',': #encontra o caractere separador
                    cat = descricao[:i] #encontrou a categoria
                    descricao = descricao[i+1:]
                    break #sai do loop
            
            if not cat in self.categoria: #se a categoria ainda nao existe...
                self.categoria[cat] = [] #cria primeiro.
            self.categoria[cat].append(item) #preenche a categoria.
            
            self.produto[item] = {'preco' : preco, 'descricao' : descricao, 'estoque' : estoque, "categoria": cat,'id_' : id_Prod}  #preenche dict. produto

	c.close()
	return 'ok'


merc = Produtos()
merc.updateProdutoList()

#print merc.produto
#print merc.categoria
print "Testando"
print "----------------------------------"
print "mostrando produtos:"
for prod in merc.produto:
	print prod, "- R$", merc.produto[prod]["preco"], ",categoria:", merc.produto[prod]["categoria"]
print "----------------------------------"
print "mostrando categoria:"
for cat in merc.categoria:
	print cat, ":", merc.categoria[cat]
print "----------------------------------"
print "fim"
