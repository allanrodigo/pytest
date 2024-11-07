import pytest
from methods_for_test import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto:
    @pytest.fixture
    def util_texto_normal(self):
        texto = "Olá mundo! Este é um teste. Olá novamente?"
        return UtilitariosAnaliseTexto(texto)
    
    @pytest.fixture
    def util_texto_vazio(self):
        return UtilitariosAnaliseTexto("")
    
    def test_contar_palavras_unicas(self, util_texto_normal, util_texto_vazio):
        # Teste com texto normal
        assert util_texto_normal.contar_palavras_unicas() == 7
        # Teste com texto vazio
        assert util_texto_vazio.contar_palavras_unicas() == 0
        # Teste com palavras repetidas
        util = UtilitariosAnaliseTexto("test teste Test TESTE")
        assert util.contar_palavras_unicas() == 2
    
    def test_eh_anagrama(self):
        util = UtilitariosAnaliseTexto()
        # Teste de anagramas
        assert util.eh_anagrama("amor", "roma") == True
        # Teste de não anagramas
        assert util.eh_anagrama("casa", "saco") == False
        # Teste com maiúsculas e minúsculas
        assert util.eh_anagrama("Ana", "naa") == True
        # Teste com palavras vazias
        assert util.eh_anagrama("", "") == True
        assert util.eh_anagrama("a", "") == False
    
    def test_frequencia_caracteres(self, util_texto_normal, util_texto_vazio):
        # Teste com texto normal
        freq = util_texto_normal.frequencia_caracteres()
        expected = {
            'o': 4,
            'l': 2,
            'á': 2,
            'm': 3,
            'u': 2,
            'n': 3,
            'd': 1,
            'e': 6,
            'é': 1,
            's': 2,
            't': 4,
            'v': 1,
            'a': 1
        }
        assert freq == expected
        # Teste com texto vazio
        assert util_texto_vazio.frequencia_caracteres() == {}
        # Teste com caracteres especiais
        util = UtilitariosAnaliseTexto("C@d@#123")
        expected = {'c': 1, 'd': 1, '1': 1, '2': 1, '3': 1}
        assert util.frequencia_caracteres() == expected
    
    def test_palavras_unicas_ordenadas(self, util_texto_normal, util_texto_vazio):
        # Teste com texto normal
        palavras_ordenadas = util_texto_normal.palavras_unicas_ordenadas()
        expected = ['este', 'mundo!', 'novamente?', 'olá', 'teste.', 'um', 'é']
        assert palavras_ordenadas == expected
        # Teste com texto vazio
        assert util_texto_vazio.palavras_unicas_ordenadas() == []
        # Teste com repetição e diferentes casos
        util = UtilitariosAnaliseTexto("Casa casa CASA")
        expected = ['casa']
        assert util.palavras_unicas_ordenadas() == expected
    
    def test_palavra_mais_longa(self):
        # Teste com texto normal
        util = UtilitariosAnaliseTexto("Olá mundo! Este é um teste. Olá novamente?")
        assert util.palavra_mais_longa() == "novamente?"
        # Teste com múltiplas palavras com mesmo tamanho
        util = UtilitariosAnaliseTexto("carro moto barco")
        assert util.palavra_mais_longa() == "carro"
        # Teste com texto vazio
        util = UtilitariosAnaliseTexto("")
        assert util.palavra_mais_longa() == ""
        # Teste com pontuação
        util = UtilitariosAnaliseTexto("Olá, mundo!!!")
        assert util.palavra_mais_longa() == "mundo!!!"
    
    def test_prefixo_comum(self):
        util = UtilitariosAnaliseTexto()
        # Teste com prefixo comum
        lista = ["prefixo", "preto", "preparar"]
        assert util.prefixo_comum(lista) == "pre"
        # Teste sem prefixo comum
        lista = ["casa", "carro", "gato"]
        assert util.prefixo_comum(lista) == ""
        # Teste com lista vazia
        assert util.prefixo_comum([]) == ""
        # Teste com todas as palavras iguais
        lista = ["teste", "Teste", "TESTE"]
        assert util.prefixo_comum(lista) == "teste"
        # Teste com uma única palavra
        lista = ["única"]
        assert util.prefixo_comum(lista) == "única"
    
    def test_contar_frases(self):
        # Teste com texto normal
        util = UtilitariosAnaliseTexto("Olá mundo! Este é um teste. Olá novamente?")
        assert util.contar_frases() == 3
        # Teste com texto sem pontuação
        util = UtilitariosAnaliseTexto("Sem pontuação aqui")
        assert util.contar_frases() == 1
        # Teste com texto vazio
        util = UtilitariosAnaliseTexto("")
        assert util.contar_frases() == 0
        # Teste com múltiplas pontuações consecutivas
        util = UtilitariosAnaliseTexto("Olá!!! Como vai??? Tudo bem.")
        assert util.contar_frases() == 3
    
    def test_fatores_primos(self):
        util = UtilitariosAnaliseTexto()
        # Teste com número positivo
        assert util.fatores_primos(28) == [2, 2, 7]
        # Teste com número primo
        assert util.fatores_primos(13) == [13]
        # Teste com número 1
        assert util.fatores_primos(1) == []
        # Teste com número 0
        assert util.fatores_primos(0) == []
        # Teste com número negativo
        assert util.fatores_primos(-15) == []
        # Teste com número grande
        assert util.fatores_primos(1001) == [7, 11, 13]
        # Teste com número 2
        assert util.fatores_primos(2) == [2]
        # Teste com número 16
        assert util.fatores_primos(16) == [2, 2, 2, 2]
