def test_passing():
    assert (1,2,3)==(1,2,3)


def test_fail():
    assert 'test'=='testing'


def test_not():
    a='test'
    b='testing'
    assert not a==b


def test_list():
    x=[1,2,3]
    y=['a','b','c']
    assert not x==y
    assert x != y


