import pytest
from my_code import analyze_numbers


def test_analyze_normal():
    result = analyze_numbers([1,2,3,4,5,6,7])

    assert result['sum']==28
    assert result['even'] == 3
    assert result['odd'] == 4
    assert result['average'] ==4
    assert result['max'] == 7
    assert result['min'] == 1

def test_analyze_sigle():
    result= analyze_numbers([7])
    assert result['sum']== 7
    assert result['even'] == 0
    assert result['odd'] == 1
    assert result['average'] == 7
    assert result['max'] == 7
    assert result['min'] == 7

def test_analyze_emptyList():
    with pytest.raises(ValueError):
        analyze_numbers([])