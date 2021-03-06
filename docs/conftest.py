"""This file is automatically executed by pytest when testing anything in the
docs folder"""
import pytest

import pypkg_bintray_02


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    """Inject package itself into doctest namespace.

    This is so we don't need
        
    .. doctest::

        >>> import pypkg_bintray_02

    in any doctests
    """
    doctest_namespace['pypkg_bintray_02'] = pypkg_bintray_02
