from nirvana.coalesce_stragety import AverageCoalesce, MinCoalesce


def test_avg_coalesce_should_return_averages() -> None:
    data1 = {
        'a': 1,
        'b': 1,
        'c': 1.,
    }

    data2 = {
        'a': 3.,
        'b': 4,
        'c': 5,
    }

    avg_coalesce = AverageCoalesce()

    avg_coalesce.add_data(data1)
    avg_coalesce.add_data(data2)

    assert avg_coalesce.get_coalesced() == {
        'a': 2.,
        'b': 2.5,
        'c': 3.,
    }


def test_min_coalesce_should_return_minimum_values() -> None:
    data1 = {
        'a': 1.,
        'b': 1,
        'c': 1,
    }

    data2 = {
        'a': 3.,
        'b': 4,
        'c': -1,
    }

    data3 = {
        'a': 3,
        'b': 0,
        'c': 0.,
    }

    avg_coalesce = MinCoalesce()

    avg_coalesce.add_data(data1)
    avg_coalesce.add_data(data2)
    avg_coalesce.add_data(data3)

    assert avg_coalesce.get_coalesced() == {
        'a': 1,
        'b': 0,
        'c': -1,
    }