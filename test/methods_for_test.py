from collections import Counter
import re


class UtilitariosAnaliseTexto:
    def __init__(self, texto=""):
        self.texto = texto
        
    def contar_palavras_unicas(self):
        """Conta o número de palavras únicas na string."""
        return len(set(self.texto.lower().split()))

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        return sorted(palavra1.lower()) == sorted(palavra2.lower())

    def frequencia_caracteres(self):
        """Retorna a frequência de cada caractere em um dicionário, ignorando espaços."""
        caracteres = [char.lower() for char in self.texto if char.isalnum()]
        return dict(Counter(caracteres))

    def palavras_unicas_ordenadas(self):
        """Retorna uma lista de palavras únicas ordenadas alfabeticamente."""
        return sorted(set(self.texto.lower().split()))

    def palavra_mais_longa(self):
        """Retorna a palavra mais longa na string. Em caso de empate, retorna a primeira."""
        palavras = self.texto.split()
        return max(palavras, key=len) if palavras else ""

    def prefixo_comum(self, lista_palavras):
        """Retorna o prefixo comum mais longo entre as palavras da lista."""
        if not lista_palavras:
            return ""
        prefixo = lista_palavras[0].lower()
        for palavra in lista_palavras[1:]:
            palavra = palavra.lower()
            while not palavra.startswith(prefixo):
                prefixo = prefixo[:-1]
                if not prefixo:
                    return ""
        return prefixo

    def contar_frases(self):
        """Conta o número de frases no texto, considerando pontos, exclamações e interrogações."""
        frases = re.split(r'[.!?]+', self.texto)
        return len([frase for frase in frases if frase.strip()])

    def fatores_primos(self, numero):
        """Retorna uma lista de fatores primos do número fornecido."""
        if numero < 2:
            return []
        fatores = []
        divisor = 2
        while divisor * divisor <= numero:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 1
        if numero > 1:
            fatores.append(numero)
        return fatores
