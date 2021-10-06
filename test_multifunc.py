import multifunc

def test_add_two_to_two_numbers():
    assert multifunc.add_two_to_two_numbers(1,1) == [3,3]

def test_calcuscore():
    assert multifunc.calcuscore(10,10,10) == 17