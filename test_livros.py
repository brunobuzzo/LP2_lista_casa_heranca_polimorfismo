from Classlivros import Livro

livro = Livro()

def test_preco():
    assert livro.setPreco(50.00) == 50.00
    assert livro.setPreco(53.30) == 53.30
    assert livro.setPreco(121.11) == 121.11
    assert livro.setPreco(44.73) == 44.73
    assert livro.setPreco(30) == 30.00