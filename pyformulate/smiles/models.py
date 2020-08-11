#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from typing import Optional, Union, Sequence


class Element(Enum):
    """
    Enumeration of the elements of the periodic table
    """

    UNKNOWN = 0
    H = 1
    He = 2
    Li = 3
    Be = 4
    B = 5
    C = 6
    N = 7
    O = 8  # noqa: E741
    F = 9
    Ne = 10
    Na = 11
    Mg = 12
    Al = 13
    Si = 14
    P = 15
    S = 16
    Cl = 17
    Ar = 18
    K = 19
    Ca = 20
    Sc = 21
    Ti = 22
    V = 23
    Cr = 24
    Mn = 25
    Fe = 26
    Co = 27
    Ni = 28
    Cu = 29
    Zn = 30
    Ga = 31
    Ge = 32
    As = 33
    Se = 34
    Br = 35
    Kr = 36
    Rb = 37
    Sr = 38
    Y = 39
    Zr = 40
    Nb = 41
    Mo = 42
    Tc = 43
    Ru = 44
    Rh = 45
    Pd = 46
    Ag = 47
    Cd = 48
    In = 49
    Sn = 50
    Sb = 51
    Te = 52
    I = 53  # noqa: E741
    Xe = 54
    Cs = 55
    Ba = 56
    La = 57
    Ce = 58
    Pr = 59
    Nd = 60
    Pm = 61
    Sm = 62
    Eu = 63
    Gd = 64
    Tb = 65
    Dy = 66
    Ho = 67
    Er = 68
    Tm = 69
    Yb = 70
    Lu = 71
    Hf = 72
    Ta = 73
    W = 74
    Re = 75
    Os = 76
    Ir = 77
    Pt = 78
    Au = 79
    Hg = 80
    Tl = 81
    Pb = 82
    Bi = 83
    Po = 84
    At = 85
    Rn = 86
    Fr = 87
    Ra = 88
    Ac = 89
    Th = 90
    Pa = 91
    U = 92
    Np = 93
    Pu = 94
    Am = 95
    Cm = 96
    Bk = 97
    Cf = 98
    Es = 99
    Fm = 100
    Md = 101
    No = 102
    Lr = 103
    Rf = 104
    Db = 105
    Sg = 106
    Bh = 107
    Hs = 108
    Mt = 109
    Ds = 110
    Rg = 111
    Cn = 112
    Nh = 113
    Fl = 114
    Mc = 115
    Lv = 116
    Ts = 117
    Og = 118


class BondType(Enum):
    """
    Bond type enumeration
    """

    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3
    QUADRUPLE = 4
    AROMATIC = 5
    BOTTOM_TOP = 6  # For cis-trans
    TOP_BOTTOM = 7


class ChiralClass(Enum):
    """
    Enumeration for the tags used in SMILES for representing chiral stereochemistry
    """

    _ANTICLOCKWISE = -1  # Indicates an atom requires further analysis
    _CLOCKWISE = -2      # to determine chiral class
    TH1 = 1
    TH2 = 2
    AL1 = 3
    AL2 = 4
    SP1 = 5
    SP2 = 6
    SP3 = 7
    TB1 = 8
    TB2 = 9
    TB3 = 10
    TB4 = 11
    TB5 = 12
    TB6 = 13
    TB7 = 14
    TB8 = 15
    TB9 = 16
    TB10 = 17
    TB11 = 18
    TB12 = 19
    TB13 = 20
    TB14 = 21
    TB15 = 22
    TB16 = 23
    TB17 = 24
    TB18 = 25
    TB19 = 26
    TB20 = 27
    OH1 = 28
    OH2 = 29
    OH3 = 30
    OH4 = 31
    OH5 = 32
    OH6 = 33
    OH7 = 34
    OH8 = 35
    OH9 = 36
    OH10 = 37
    OH11 = 38
    OH12 = 39
    OH13 = 40
    OH14 = 41
    OH15 = 42
    OH16 = 43
    OH17 = 44
    OH18 = 45
    OH19 = 46
    OH20 = 47
    OH21 = 48
    OH22 = 49
    OH23 = 50
    OH24 = 51
    OH25 = 52
    OH26 = 53
    OH27 = 54
    OH28 = 55
    OH29 = 56
    OH30 = 57


class Atom:
    """
    Represents an atom, ion, etc.
    """

    def __init__(
        self,
        element: Union[str, Element],
        *,
        isotope: Optional[int] = None,
        charge: int = 0,
        chiral_class: Optional[ChiralClass] = None,
        aromatic: bool = False,
        bonds: Sequence["Bond"] = None,
        atom_class: int = 0,
    ):
        if isinstance(element, str):
            try:
                element = Element[element.title()]
            except KeyError:
                raise ValueError(f"{element!r} is not a valid symbol") from None
        if isotope is None:
            isotope = element.value
        self.isotope = isotope
        self.element = element
        self.charge = charge
        self.chiral_class = chiral_class
        self.aromatic = aromatic
        self.bonds = list(bonds) if bonds else []
        self.atom_class = atom_class

    def bond(self, atom: "Atom", bond_type: BondType = BondType.SINGLE):
        if atom == self:
            raise ValueError("Cannot bond atom to itself")
        bond = Bond(bond_type, self, atom)
        for atm in (self, atom):
            atm.bonds.append(bond)

    def __str__(self):
        return "{0.isotope}{0.element.name}".format(self)

    def __repr__(self):
        return (
            "{0.__name__}(element={1.element}, isotope={1.isotope}, "
            "charge={1.charge}, chiral_class={1.chiral_class}, "
            "aromatic={1.aromatic}, atom_class={1.atom_class})"
        ).format(type(self), self)


class Bond:
    """
    Represents a bond between two Atoms
    """

    def __init__(self, type_: BondType, *atoms: Atom):
        self.type = type_
        self.atoms = atoms

    def __contains__(self, atom: Atom):
        return atom in self.atoms

    def __str__(self):
        return "<Bond between {0} and {1} of type {2.name}>".format(
            *self.atoms, self.type
        )

    def __repr__(self):
        return str(self)


class Molecule:
    """
    Represents a molecule
    """

    def __init__(self, atoms):
        self.atoms = atoms

    @property
    def bonds(self):
        bonds = set()
        for atom in self.atoms:
            bonds.add(atom.bonds)
        return bonds

    def elem_count(self, element: Element) -> int:
        """
        Returns the number of atoms of the specified element

        :param element: The element to count
        :type element: Element
        :return: The number of atoms of that element
        :rtype: int
        """
        return sum(1 for atom in self.atoms if atom.element == element)
