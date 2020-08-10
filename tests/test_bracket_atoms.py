#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from pyformulate.smiles import loads
from pyformulate.smiles.decoder import DecodeError
from pyformulate.smiles.models import Element


def test_known_elements():
    for elem in Element:
        if elem == Element.UNKNOWN:
            continue
        assert loads(f"[{elem.name}]").molecules[0].atoms[0].element == elem


def test_unknown_element():
    assert loads("[*]").molecules[0].atoms[0].element == Element.UNKNOWN


def test_invalid_elements():
    with pytest.raises(DecodeError):
        assert loads("[]")  # Empty bracket atom


def test_explicit_hydrogen_count():
    assert loads("[CH4]").molecules[0].elem_count(Element.H) == 4
    assert loads("[ClH1]").molecules[0].elem_count(Element.H) == 1


def test_implicit_hydrogen_count():
    assert loads("[ClH]").molecules[0].elem_count(Element.H) == 1


def test_illegal_hydrogen_count():
    with pytest.raises(DecodeError):
        loads("[HH1]")