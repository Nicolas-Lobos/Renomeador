'''
DESENVOLVIDO POR NICOLAS RAFAEL LOBOS SILVA

ESTE SCRIPT TEM A INTENÇÃO DE AUTOMATIZAR O PROCESSO DE
RENOMEAÇÃO DE ARQUIVOS COM BASE NO CONTEUDO DELES

ESTE ARQUIVO FOI DESENVOLVIDO PARA UTILIZAÇÃO  COM
O CLIENTE CETENCO ENGENHARIA S.A. DA EMPRESA ARQUIVAR
DE SÃO JOSÉ DOS CAMPOS
'''

# IMPORTAÇÃO DE BIBLIOTECAS UTILIZADAS

# BIBLIOTECA DE INTERAÇÃO COM O SISTEMA OPERACIONAL
import os
# BIBLIOTECA DE CONVERSÃO DE PDF OCRIZADO PARA TXT
import PyPDF2

# LOCALIZANDO O DIRETORIO A SER UTILIZADO
os.chdir(r"C:\Users\Nicolas\Desktop\TESTE ARQUIVAR\OP")

'''
A LINHA ABAIXO EXIBE O DIRETORIO ATUAL PARA CONFIRMAÇÃO
UTILIZADO APENAS NO DESENVOLVIMENTO

print(os.getcwd())
'''

# LAÇO DE REPETIÇÃO QUE PERCORRE TODOS OS ARQUIVOS DO DIRETORIO
for f in os.listdir():
    # DENOMINAÇÃO DAS CONSTANTES
    f_ext = ".pdf"
    string_busca = "PAGAMENTO"

    file_name = f
    '''
    # A LINHA ABAIXO CONFERE O NOME DO ARQUIVO
    UTILIZADO APENAS NO DESENVOLVIMENTO
    
    # print(file_name)
    '''
    # CRIANDO UM ARQUIVO DE TEXTO PARA ARMAZENAR OS DADOS DO PDF
    pdf_file_obj = open(f, 'rb')
    # LENDO O PDF
    pdfreader = PyPDF2.PdfFileReader(pdf_file_obj)
    # REALIZA A CONTAGEM DAS PAGINAS DO PDF
    count_pages = pdfreader.numPages
    # SELECIONA APENAS A PRIMEIRA PAGINA
    select_page = pdfreader.getPage(count_pages == 0)
    # EXTRAINDO O TEXTO PARA UMA VARIAVEL LOCAL
    text = select_page.extractText()
    # DIVIDE O TEXTO EXTRAIDO UTILIZANDO O ESPAÇO COMO SEPARADOR
    text_lines = text.split(" ")
    '''
    CRIANDO UM SISTEMA DE LIMPEZA PARA AS INFORMAÇÕES EXTRAIDAS
    DO TEXTO OCRIZADO, REMOVE TABULAÇÕES Q INVALIDAM A BUSCA DE STRING
    '''

    # LISTA PARA ARMAZENAR O TEXTO FATIADO E LIMPO
    text_l_clean = []
    # REPETIÇÃO PARA LIMPEZA
    for i in text_lines:
        # REMOÇÃO DE CARACTERES E SUBSTITUIÇÃO DE CARACTERES NO MEIO DA STRING
        i = i.strip('\n')
        i = i.strip('\t')
        i = i.replace('\n', '')
        # INCLUSÃO DO TEXTO LIMPO NA LISTA
        text_l_clean.append(i)
    '''
    A LINHA ABAIXO EXIBE O CONTEUDO LIMPO DO TEXTO EXTRAIDO
    UTILIZADO APENAS NO DESENVOLVIMENTO
    
    # print(text_l_clean)
    '''

    # REALIZA A BUSCA DA STRING QUE PRECEDE O NUMERO DA OP
    if string_busca in text_l_clean:
        index = text_l_clean.index(string_busca)
        '''
        OS COMENTARIOS ABAIXO SERVEM APENAS PARA CONFERIR INFORMAÇÕES
        UTILIZADO APENAS NO DESENVOLVIMENTO, SOMENTE A VARIAVEL OP DEVE
        PERMANECER PARA GARANTIR O FUNCIONAMENTO DO SCRIPT, O ELSE SERVE
        PARA TRATAMENTO DE ERROS
        '''
        # print("encontrado")
        # print(index)
        # print(text_l_clean[index + 1])
        op = text_l_clean[index + 1]
        # print(f'op é = {op}')
        # print(op+f_ext)
    else:
        print("erro")
    # FECHAMENTO DO ARQUIVO DE TEXTO
    pdf_file_obj.close()
    '''
    A SEQUENCIA ABAIXO CRIA O NOVO NOME DO ARQUIVO COM BASE NA INFORMAÇÃO
    OBTIDA DA LEITURA DO TXT, QUE FOI ARMAZENADA NA VARIAVEL OP
    '''
    file_old_name = file_name
    file_new_name = op + f_ext
    '''
    A LINHA ABAIXO REALIZA A ALTERAÇÃO DO NOME DO ARQUIVO
    '''
    os.rename(file_old_name, file_new_name)
print("RENOMEAÇÃO CONCLUIDA!")