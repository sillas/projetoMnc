class Produtos:
    """ * item:
        - Nome do produto:
        - dict{preço, descrição**, estoque, cod.}

        *categoria**:
        - categoria:
        - [itens (nomes apenas)]

        ** Estrutura no BD:
        "categoria,descricao" - primeira ',' Caractere separador'



CREATE TABLE produtos (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(150),
quantidade INTEGER,
descricao VARCHAR(500),
preco DOUBLE
)

"""
    def __init__(self):
        self.produto = {}
        self.categoria = {}
        UpdateProdutoList();

    def UpdateProdutoList(self):
        import MySQLdb #mudar de posicao
        try:
            con = MySQLdb.connect(host= `host`, user=`root`, passwd=password, db=`banco`)
        except:
            print 'Erro na conexcao com o banco de dados!'
            return 'BD_Con_Erro'
        
        c = con.cursor()
        c.execute("SELECT * FROM `produtos`")#ver
        #preencher:
        '''
        for item in c: -- Ver isso
            item, preco, descricao, estoque = item -- Ver a estrutura antes!
            self.produto[item] = {'preco':preco, 'descricao':descricao, 'estoque':estoque}

            for i in range(len(descricao)):
                if descricao[i] == ',':
                    cat = descricao[:i]
                    break
            
            if not cat in self.categoria:
                self.categoria[cat] = []
            self.categoria[cat].append
        '''
        
