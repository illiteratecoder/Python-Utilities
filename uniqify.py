def uniqify(seq):
    """Returns list of unqiue elements, preserving order"""

    uniques = []
    [uniques.append(i) for i in seq if not uniques.count(i)]

    return uniques
