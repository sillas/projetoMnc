'''
produtos		clientes		Compras
---------------------------------------------------------------
-codigo	(auto)		-id			-carrinho
-nome			-nome			-valor_total
-quant			-telefone		-status	
-preco			-cpf
-descricao		-Dnascimento
			-endereco
			-e-mail
---------------------------------------------------------------

Produtos:
-produto_indvidual - {preco':valor, 'descricao': str, 'quantidade': valor}


estoque = {'agua':{preco':valor, 'descricao': str, 'quant': valor},
	   'pera':{preco':valor, 'descricao': str, 'quant': valor},
	   'bisc':{preco':valor, 'descricao': str, 'quant': valor}
            }

categoria = {
	  'bebidas':[],
	  'salgados':[],
	  'doces':[]
	}
'''


class Produtos:
    def __init__(self, bib = {}):
        self.produtos = bib

    #esta funcao cadastra os produtos
    def cadastro(self, produto, valor, quant, desc):
        #-------------------------
        if produto in self.produtos:
            print produto,':',produtos[produto]
            ok = raw_input('Produto ja existe, deseja alterar? Sim ou não')
            #-------------------------
            if ok == 'Sim' or ok == 'SIM' or ok == 'sim' or ok == 's' or ok == 'S':
				
                self.produtos[produto]['preco'] = valor
                self.produtos[produto]['quant'] = quant
                self.produtos[produto]['descricao'] = desc	

                print 'Valores alterados!'
                return len(self.produtos)
                #-------------------------
            else:
                print 'valor nao alterado.'
                return len(self.produtos)
            #-------------------------
        #-------------------------
        else:
            self.produtos[produto] = {}
            self.produtos[produto]['preco'] = valor
            self.produtos[produto]['quant'] = quant
            self.produtos[produto]['descricao'] = desc

            print 'produto cadastrado!'
            return len(self.produtos)
        #-------------------------



    #esta funcao faz uma pesquisa por produtos
    def busca(self, consulta = '', end = 'no'):
        ok = False
        #consulta por preco
        #-------------------------
        if type(consulta) == int or type(consulta) == float:
            #consulta entre valores
            #-------------------------
            if type(end) == int or type(end) == float:
                if consulta > end:
                    consulta, end = end, consulta
                #-------------------------
                for item in self.produtos:
                    if self.produtos[item]['preco'] >= consulta and self.produtos[item]['preco'] <= end:
                        ok = True
                        print item,'- R$', self.produtos[item]['preco']
                    #-------------------------
                #-------------------------
                else:
                    #-------------------------
                    for item in self.produtos:
                        if self.produtos[item]['preco'] == consulta:
                            ok = True
                            print item,'- R$',self.produtos[item]['preco']
                    #-------------------------
        #-------------------------
        #consulta por nome
        elif type(consulta) == str:
            if consulta in self.produtos:
                print consulta,'-R$', self.produtos[consulta]['preco'],'-',self.produtos[consulta]['descricao'],'St:',self.produtos[consulta]['quant']
                ok = True
        else:
            print 'Parametro invalido'
        #-------------------------
        return ok
				
		

    #esta funcao altera o valor de um produto
    def altera(self, produto = '', valor = '', quant = '', desc = 0):
    #-------------------------
        if produto in self.produtos:
            print produto,'-R$', self.produtos[produto]['preco'],'-',self.produtos[produto]['descricao'],'St:',self.produtos[produto]['quant']

            if type(valor) == int or type(valor) == float:
            	self.produtos[produto]['preco'] = valor

            if type(quant) == int or type(quant) == float:
            	self.produtos[produto]['quant'] = quant

            if type(quant) == str:
                self.produtos[produto]['descricao'] = desc

            return True
        #-------------------------			
        else:
            print 'Produto nao existe!'
            return False	
        #-------------------------





    #esta funcao remove um produto
    def remove(self, produto):
        #-------------------------
        if produto in self.produtos:
            print produto,'-R$', self.produtos[produto]['preco'],'-',self.produtos[produto]['descricao'],'St:',self.produtos[produto]['quant']
            ok = raw_input('Deseja remover este produto? Sim ou não')
            #-------------------------
            if ok == 'Sim' or ok == 'SIM' or ok == 'sim' or ok == 's' or ok == 'S':
                del self.produtos[produto]
                return len(self.produtos)
            #-------------------------
            else:
                return 'no'
            #-------------------------
        #-------------------------
        else:	
            print 'Produto nao existe!'
            return 'no'
        #-------------------------
		



	#esta funcao remove todos os produtos
	def removeAll(self):
		#-------------------------
		ok = raw_input('Deseja remover TODOS os produtos? Sim ou não')
		if ok == 'Sim' or ok == 'SIM' or ok == 'sim' or ok == 's' or ok == 'S':
			lista = self.produtos.keys()
			for i in lista:
				del self.produtos[i]
			return True
		#-------------------------
		else:
			return False
		#-------------------------


    #esta funcao mostra todos os produtos
    def mostra(self):
        for produto in self.produtos:
            print produto,'-R$', self.produtos[produto]['preco'],'-',self.produtos[produto]['descricao'],'St:',self.produtos[produto]['quant']
        return len(self.produtos)


#===================================================================================


class Cliente:
	
	def __init__(self, bib = {}):
		self.nome = bib

	#esta funcao realiza um cadastro de um cliente
	def cadastro(self, _nome, _cpf, _rg, _dNascimento, end, logIn, senha, e_mail):

		if _nome in self.nome:

			print _nome, ':', nome[_nome]
			ok = raw_input('Cliente existente, deseja alterar? Sim ou não')
           		#-------------------------
            		if ok == 'Sim' or ok == 'SIM' or ok == 'sim' or ok == 's' or ok == 'S':

				self.nome[_nome]['cpf'] = _cpf
				self.nome[_nome]['rg'] = _rg
				self.nome[_nome]['dNascimento'] = _dNascimeto
				self.nome[_nome]['endereco'] = end
				self.nome[_nome]['logIn'] = logIn
				self.nome[_nome]['senha'] = senha
				self.nome[_nome]['e_mail'] = e_mail

				print "\nDados alterados"
				return len(self.nome)

			else:

				print "\nDados nao alterados"
				return len(self.nome)

		else:

			self.nome[_nome] = {}
			self.nome[_nome]['cpf'] = _cpf
			self.nome[_nome]['rg'] = _rg
			self.nome[_nome]['dNascimento'] = _dNascimeto
			self.nome[_nome]['endereco'] = end
			self.nome[_nome]['logIn'] = logIn
			self.nome[_nome]['senha'] = senha
			self.nome[_nome]['e_mail'] = e_mail
			
			print "\nCliente cadastrado"
			return len(self.nome)
			
	#esta funcao exclui o cadastro de um cliente
	def exclui_cadastro():
		pass

	def carrinho():
		pass

	def compras():
		pass

	def cMostra():
		pass
"""	

				

"""
if __name__ == "__main__":
	app = app()
	app.execute()
	
