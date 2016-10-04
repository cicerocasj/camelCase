# -*- coding: utf-8

class Conversor(object):
    
    @staticmethod
    def temProximo(i=int()):
        return True if i < len(Conversor.original)-1 else False

    @staticmethod
    def temAnterior(i=int()):
        return True if i > 0 and len(Conversor.original) else False

    @staticmethod
    def caso1(i=int()):
        # aa
        if Conversor.temProximo(i):
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(atual == atual.lower() and proximo == proximo.lower() and not Conversor.isInt(proximo)):
                return False
        return True

    @staticmethod
    def caso2(i=int()):
        # Aa
        if Conversor.temProximo(i) and not i:
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(atual == atual.upper() and proximo == proximo.lower() and not Conversor.isInt(proximo)):
                return False
        else:
            return False
        Conversor.letra = Conversor.letra.lower()
        return True

    @staticmethod
    def caso3(i=int()):
        # AA
        if Conversor.temProximo(i):
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(atual == atual.upper() and proximo == proximo.upper() and not Conversor.isInt(proximo)):
                return False
        return True

    @staticmethod
    def caso4(i=int()):
        # [a-A]9
        if Conversor.temProximo(i):
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(not Conversor.isInt(atual) and Conversor.isInt(proximo)):
                return False
        return True
    @staticmethod
    def caso5(i=int()):
        # 99
        if Conversor.temProximo(i):
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(Conversor.isInt(atual) and Conversor.isInt(proximo)):
                return False
        return True

    @staticmethod
    def isInt(letra=str()):
        try:
            int(letra)
            return True
        except:
            return False

    @staticmethod
    def casoExtra1(i=int()):
        # A[A]a
        if Conversor.temProximo(i) and i and Conversor.temAnterior(i):
            anterior = Conversor.original[i]
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(anterior == anterior.upper() and atual == atual.upper() and proximo == proximo.lower()):
                return False
        else:
            return False
        Conversor.letra = Conversor.letra.lower()
        return True

    @staticmethod
    def casoExtra2(i=int()):
        # 9[9]a
        if Conversor.temProximo(i) and i and Conversor.temAnterior(i):
            anterior = Conversor.original[i]
            atual = Conversor.original[i]
            proximo = Conversor.original[i+1]
            if not(Conversor.isInt(anterior) and Conversor.isInt(atual) and not Conversor.isInt(proximo)):
                return False
        else:
            return False
        return True

    @staticmethod
    def continuaPalavra(i=int()):
        atual = Conversor.original[i]
        caso1 = Conversor.caso1(i) 
        caso2 = Conversor.caso2(i)
        caso3 = Conversor.caso3(i)
        caso4 = Conversor.caso4(i)
        caso5 = Conversor.caso5(i)
        return caso1 or caso2 or caso3 or caso5
    
    @staticmethod
    def inicializaVariaveis(original=str()):
        Conversor.original = original
        Conversor.palavra = ""
        Conversor.letra = ""
        Conversor.palavras = []
    @staticmethod
    def converterCamelCase(original=str()):
        Conversor.inicializaVariaveis(original)
        i = 0
        for Conversor.letra in original:
            if Conversor.continuaPalavra(i):
                Conversor.palavra = Conversor.palavra + Conversor.letra
                i = i + 1
                continue
            else:
                casoExtra1 = Conversor.casoExtra1(i)
                casoExtra2 = Conversor.casoExtra2(i)
                print "casoExtra", casoExtra1, casoExtra2
                if casoExtra1:
                    if Conversor.palavra:
                        Conversor.palavras.append(Conversor.palavra)
                    Conversor.palavra = Conversor.letra
                else:
                    Conversor.palavra = Conversor.palavra + Conversor.letra
                    Conversor.palavras.append(Conversor.palavra)
                    Conversor.palavra = ""
                i = i + 1

        if Conversor.palavra:
            Conversor.palavras.append(Conversor.palavra)
        return Conversor.palavras


print Conversor.converterCamelCase("nome") # nome
print Conversor.converterCamelCase("Nome") # nome
print Conversor.converterCamelCase("nomeComposto") # nome, composto
print Conversor.converterCamelCase("NomeComposto") # nome, composto
print Conversor.converterCamelCase("CPF") # CPF
print Conversor.converterCamelCase("CPFContribuintePessoa")
print Conversor.converterCamelCase("CPFContribuinteTALPessoaOI")
print Conversor.converterCamelCase("numeroCPF")
print Conversor.converterCamelCase("NumeroCPFContribuinte")
print Conversor.converterCamelCase("recupera10Primeiros")
print Conversor.converterCamelCase("10Primeiros")# - Inválido → não deve começar com números
print Conversor.converterCamelCase("nome#Composto")# - Inválido → caracteres especiais não são permitidos, somente letras e números
