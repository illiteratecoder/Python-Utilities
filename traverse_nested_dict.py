"""Retrieve or set value of item in arbitrarily nested dict."""

def get_from_dict(dictionary, maplist):
    from functools import reduce
    import operator

    return reduce(operator.getitem, maplist, dictionary)

def set_in_dict(dictionary, maplist, value):
    get_from_dict(dictionary, maplist[:-1])[maplist[-1]] = value

if __name__ == "__main__":
    DICTIONARY = {
        "a1": {
            "b1": 100,
            "b2": 200,
            "b3": {
                "c1": {
                    "d1": 100
                },
                "c2": 200
            }
        },
        "a2": {
            "b1": "I'm a string!",
            "b2": ["I'm", "a", "list"]
        }
    }

    MAPLIST = ["a2", "b1"]
    print(get_from_dict(DICTIONARY, MAPLIST))
    # >> I'm a string!

    MAPLIST = ["a1", "b3", "c1", "d1"]
    set_in_dict(DICTIONARY, MAPLIST, 9000)
    print(get_from_dict(DICTIONARY, MAPLIST))
    # >> 9000