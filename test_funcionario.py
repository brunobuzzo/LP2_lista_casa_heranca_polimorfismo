from Classfuncionarios import Funcionario


def test_valor():
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(10) == 1870
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(33) == 2261
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(3) == 1751
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(72) == 2924
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(14) == 1938
    func = Funcionario('bruno', 1700)
    assert func.aumentar_salario(26) == 2142

