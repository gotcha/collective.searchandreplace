from plone.testing import layered
from collective.searchandreplace.testing import SEARCH_REPLACE_FUNCTIONAL_LAYER
from unittest import TestSuite
import doctest


oflags = (doctest.ELLIPSIS |
          doctest.NORMALIZE_WHITESPACE)


def test_suite():
    suite = TestSuite()

    basicsearchtest = layered(doctest.DocFileSuite(
        'tests/basicsearch.txt',
        package='collective.searchandreplace',
        optionflags=oflags),
        layer=SEARCH_REPLACE_FUNCTIONAL_LAYER)

    searchavailabletest = layered(doctest.DocFileSuite(
        'tests/searchavailable.txt',
        package='collective.searchandreplace',
        optionflags=oflags),
        layer=SEARCH_REPLACE_FUNCTIONAL_LAYER)

    suite.addTests([
        basicsearchtest,
        searchavailabletest,
    ])

    return suite
