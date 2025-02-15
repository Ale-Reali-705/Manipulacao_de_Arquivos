def abrir_arquivo(arquivo:str):
    '''
    Recebe o nome de um arquivo e retorna uma lista de dicionários.
    Cada dicionário representa um registro do arquivo.
    '''
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            chaves = f.readline().replace('\n', '').split(", ")
            valores = [linha.replace('\n', '').split(', ') for linha in f.readlines()]
            return [{chave: valor for chave, valor in zip(chaves, linha)} for linha in valores]
   
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        return None
    

def quantidade_nome(nome:str=''):
    '''
    Recebe um nome (string) e retorna um inteiro e uma lista de dicionários.
    O inteiro retornado é a quantidade de registros cujo nome começa com o nome recebido.
    A lista retornada contem todos os registros/dicionários cujo nome começa com o nome recebido.
    Caso o nome não seja informado, retorna todos os registros.
    Caso o arquivo não exista, retorna a mensagem 'Arquivo não encontrado.'.
    '''
    try:
        if type(nome) != str:
            raise Exception("O nome deve ser uma string.")
        elif not nome.isalpha():
            raise Exception("O nome deve conter apenas letras.")
        
    except Exception as e:
        print(e)
        return None
    
    else:
        registros = abrir_arquivo("dados_usuarios.txt")
        filtro = [item for item in registros if item["name"][:len(nome)] == nome.title()]
        return len(filtro), filtro


def quantidade_genero_ano(genero:str, ano:int=0):
    '''
    Recebe um genero (string) e um ano (inteiro) e retorna um inteiro.
    O inteiro retornado é a quantidade de registros que possuem o mesmo genero e com valores maiores ou igual ao ano.
    Caso o ano não seja informado, retornará a quantidade de registros do genero selecionado.
    Caso os argumentos não atendam as condições, retorna a mensagem de erro personalizada.
    '''
    try:
        if genero[0].upper() not in ['M', 'F']:
            raise Exception("O genero deve começar com 'M' ou 'F'.")
        
        if type(ano) != int:
            raise Exception("O ano deve ser um número inteiro.")
        
    except Exception as e:
        print(e)
        return None
    
    else:
        registros = abrir_arquivo("dados_usuarios.txt")
        return len([item for item in registros if item['gender'] == genero[0].upper() and int(item['year']) >= ano])
            

def detectando_substring(arg:str):
    '''
    Recebe um arg (string) e retorna uma lista de dicionários.
    Cada dicionário contém o argumento 'arg' como substring.
    '''
    try:
        if type(arg) != str:
            raise Exception("O argumento deve ser uma string.")
        
    except Exception as e:
        print(e)
        return None
    
    else:
        registros = abrir_arquivo("dados_usuarios.txt")
        return [item for item in registros if any(arg.lower() in valores.lower() for valores in item.values())]

def detectando_ID(numero:int):
    '''
    Recebe um número (inteiro) e retorna um dicionário.
    O dicionário retornado contém o registro cujo ID é igual ao número recebido.
    '''
    try:
        if type(numero) != int:
            raise Exception("O número deve ser um número inteiro.")
        
    except Exception as e:
        print(e)
        return None
    
    else:
        registros = abrir_arquivo("dados_usuarios.txt")
        filtro = [registro for registro in registros if int(registro['ID']) == numero]
        return filtro[0] if filtro else "ID não encontrado."
    

def adicionar_novo_registro(nome:str, ano:str, genero:str, numero:str):
    '''
    Recebe um nome (string), um ano (string), um genero (string) e um número (string).
    Adiciona um novo registro ao arquivo 'dados_usuarios.txt'.
    '''
    try:
        if type(nome) != str \
        or type(ano) != str \
        or type(genero) != str \
        or type(numero) != str:
            raise Exception("Os argumentos devem ser strings.")
        
        elif not ano.isdigit() \
        or not numero.isdigit():
            raise Exception("O ano e o numero devem ser digitos.")
        
        elif genero[0].upper() not in ['M', 'F']: 
            raise Exception("O genero deve começar com 'M' ou 'F'.")
        
    except Exception as e:
        print(e)
    
    else:
        with open("dados_usuarios.txt", "a", encoding="utf-8") as f:
            f.write(f"{len(abrir_arquivo('dados_usuarios.txt')) + 1}, {ano:04}, {genero[0].upper()}, {nome.title()}, {numero:02}\n")
            print("Registro adicionado com sucesso.")
