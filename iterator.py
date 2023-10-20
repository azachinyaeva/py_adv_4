class FlatIterator:

    def __init__(self, list_of_lists):
        self.main_list = iter(list_of_lists)

    def __iter__(self):
        self.result_list = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.result_list)
        except StopIteration:
            self.result_list = iter(next(self.main_list))
            item = next(self.result_list)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
