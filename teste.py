""" 
        * item:
        - Nome do produto:
        - dict{preco, descricao**, estoque, Id_cod.}

        *categoria**:
        - categoria:
        - [itens (nomes dos itens, apenas)]

        ** Estrutura no BD:
        Formato: "categoria,descricao" 


        CREATE TABLE produtos(
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(150),
            quant INTEGER,
            preco DOUBLE
            descricao VARCHAR(150), #500!
       )

Comando correto para inserir produto:
        c.execute( "INSERT INTO produtos (nome, quant, preco, descricao) VALUES ('%s', %d, %f,'%s')" % ("agua", 10, 2.30, "bebidas,ok"))
"""
class Produtos:
    def __init__(self):
        self.produto = {}
        self.categoria = {}
        UpdateProdutoList();

    def UpdateProdutoList(self):
        import MySQLdb #mudar de posicao
        try:
            con = MySQLdb.connect(host="10.5.18.40", user="root", passwd="admin", db="loja_pet")
        except:
            print 'Erro na conexcao com o banco de dados!'
            return 'BD_Con_Erro'
        
        c = con.cursor()
        c.execute("SELECT * FROM produtos")
        
        #preencher os dicionarios com os dados do banco para acesso rapido:
        for item in c: 
            id_Prod, item, preco, descricao, estoque = item
            self.produto[item] = {'preco' : preco, 'descricao' : descricao, 'estoque' : estoque, 'id_' : id_Prod}  #preenche dict. produto

            #preenche dict Categoria
            for i in range(len(descricao)): #extrai a categoria do produto do campo produto_descricao
                if descricao[i] == ',': #encontra o caractere separador
                    cat = descricao[:i] #encontrou a categoria
                    break #sai do loop
            
            if not cat in self.categoria: #se a categoria ainda nao existe...
                self.categoria[cat] = [] #cria primeiro.
            self.categoria[cat].append #preenche a categoria.
        

        
