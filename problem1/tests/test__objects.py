from problem1.objects import Tool

def test__is_multiple_of_3():
    tool = Tool()
    assert tool.is_multiple_of_3(9)
    assert tool.is_multiple_of_3(12)


def test__is_multiple_of_5():
    tool = Tool()
    assert tool.is_multiple_of_5(9)
    assert tool.is_multiple_of_5(12)