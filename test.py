from pwneurons import pwneurons


def insert_(item, val):
    item.append(val)
    return item

"""Basic Test"""
def test_():
    from datasets import load_seeds
    x, y = load_seeds()
    data = map(lambda n:insert_(n[0],n[1]), zip(x,y))
    pw = pwneurons(data)

test_()
    
