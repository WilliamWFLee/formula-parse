#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from typing import Dict, Iterator, List, Optional, Sequence, Union


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


class CisTransType(Enum):
    """
    Cis-trans classification of bond
    """

    BOTTOM_TOP = 1
    TOP_BOTTOM = 2


class ChiralClass(Enum):
    """
    Enumeration for the tags used in SMILES for representing chiral stereochemistry
    """

    _ANTICLOCKWISE = -1  # Indicates an atom requires further analysis
    _CLOCKWISE = -2  # to determine chiral class
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


class BondType:
    """
    Class for holding bond type information

    .. attribute:: order

        The order of the bond

        :type: int

    .. attribute:: aromatic

        Whether the bond is aromatic

        :type: bool

    .. attribute:: cis_trans

        The cis-trans classification of the bond, as per SMILES, if applicable

        :type: Optional[CisTransType]
    """

    def __init__(
        self,
        order: int = 1,
        aromatic: bool = False,
        cis_trans: Optional[CisTransType] = None,
    ):
        self.order = order
        self.aromatic = aromatic
        self.cis_trans = cis_trans

    def __iter__(self):
        return iter((self.order, self.aromatic, self.cis_trans))

    def __repr__(self):
        return "{0.__name__}({1.order}, {1.aromatic}, {1.cis_trans})".format(
            type(self), self
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.order == other.order
            and self.aromatic == other.aromatic
            and self.cis_trans == other.cis_trans
        )


class BondingError(Exception):
    """
    Class of exceptions raised for illegal bonds

    Inherits directly from :class:`Exception`
    """

    pass


class Atom:
    """
    Represents an atom, ion, etc.

    .. attribute:: element

        The element of the atom

        :type: Element

    .. attribute:: isotope

        The isotope of the element, as its nucleon number

        :type: int

    .. attribute:: charge

        The charge of the atom

        :type: int

    .. attribute:: chiral_class

        The chiral class of the atom, according to the SMILES specification

        :type: ChiralClass

    .. attribute:: bonds

        The bonds of the atom

        :type: List[Atom]

    .. attribute:: atom_class

        The atom class of the atom, as defined by the SMILES specification

        :type: int
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
                raise ValueError("{!r} is not a valid symbol".format(element)) from None
        self.isotope = isotope
        self.element = element
        self.charge = charge
        self.chiral_class = chiral_class
        self.aromatic = aromatic
        self.bonds = list(bonds) if bonds else []
        self.atom_class = atom_class
        self.molecule = None

    @property
    def total_bond_order(self) -> int:
        """
        The sum of the orders of the bonds this atom is participating in.
        For example, if a carbon atom has two double bonds,
        then its total bond order is 4.

        :return: The sum of the bond orders
        :rtype: int
        """
        return sum(bond.order for bond in self.bonds)

    @property
    def valency(self) -> int:
        """
        The valency of this atom. This is the number of bonds added to the charge

        :return: The valency
        :rtype: int
        """
        return self.total_bond_order + self.charge

    def bond(self, atom: "Atom", bond_type: Optional[BondType] = None):
        bond = Bond(self, atom, bond_type)
        for atm in (self, atom):
            atm.bonds.append(bond)

    def bonded_to(self, atom: "Atom"):
        for bond in self.bonds:
            if atom in bond.atoms:
                return True
        return False

    def neighbours(self) -> List["Atom"]:
        atoms = []
        for bond in self.bonds:
            other_atom = bond.atoms[0] if bond.atoms[1] == self else bond.atoms[1]
            atoms.append(other_atom)

        return atoms

    def __str__(self):
        return "{0}{1}".format(
            self.isotope if self.isotope is not None else "", self.element.name
        )

    def __repr__(self):
        return (
            "{0.__name__}(element={1.element}, isotope={1.isotope}, "
            "charge={1.charge}, chiral_class={1.chiral_class}, "
            "aromatic={1.aromatic}, atom_class={1.atom_class})"
        ).format(type(self), self)


class Bond:
    """
    Represents a bond between two Atoms

    The attributes of the :attr:`Bond.type` attribute can be accessed directly
    from the :class:`Bond` object. For example,

    >>> bond.type.order == bond.order
    True

    .. attribute:: atoms

        A tuple of the atoms in the bond

        :type: Tuple[Atom]

    .. attribute:: type

        The bond's type information

        :type: BondType
    """

    def __init__(self, atom: Atom, other_atom: Atom, type_: Optional[BondType] = None):
        """
        Creates a new :class:`Bond` between two atoms

        :param atom: One of the atoms to bond
        :type atom: Atom
        :param other_atom: The other atom to bond
        :type other_atom: Atom
        :param type_: The bond type, defaults to None
        :type type_: Optional[BondType]
        :raises BondingError: If the bond is illegal
        """
        if atom == other_atom:
            raise BondingError("Cannot bond atom to itself")
        if atom.bonded_to(other_atom):
            raise BondingError("Atoms are already bonded")
        if type_ is None:
            type_ = (
                BondType(1, True, None)
                if atom.aromatic and other_atom.aromatic
                else BondType(1, False, None)
            )
        if type_.aromatic and not (atom.aromatic and other_atom.aromatic):
            raise BondingError(
                "Aromatic bond cannot be used between atoms "
                "that are not both aromatic"
            )
        self.atoms = (atom, other_atom)
        self.type = type_

    def __getattr__(self, key):
        return getattr(self.type, key)

    def __contains__(self, atom: Atom):
        return atom in self.atoms

    def __str__(self):
        return "<Bond between {0} and {1} of order {2}>".format(
            *self.atoms, self.type, self.order
        )

    def __repr__(self):
        return str(self)


class Molecule:
    """
    Represents a molecule
    """

    def __init__(self, atoms: Optional[List[Atom]] = None):
        self._atoms = set(atoms) if atoms is not None else set()

    @property
    def bonds(self) -> List[Bond]:
        bonds = set()
        for atom in self._atoms:
            bonds.update(set(atom.bonds))
        return list(bonds)

    def add(self, atom: Atom, added_ok=False):
        """
        Adds an atom to this molecule, without any bonding.

        Raises :class:`ValueError`, unless `added_ok` is set to :data:`True`,
        if the atom to be added has already been added to this molecule.

        :param atom: The atom to add
        :type atom: Atom
        :param added_ok: Whether to ignore the atom already being in this molecule
        :type added_ok: bool
        """
        if atom in self._atoms and not added_ok:
            raise ValueError("Atom already exists in this molecule")
        atom.molecule = self
        self._atoms.add(atom)

    def new_atom(self, *args, **kwargs) -> Atom:
        """
        Creates a new atom in this molecule

        The arguments are passed directly to the constructor for :class:`Atom`,
        and the new atom is added to this molecule.

        :return: The new atom
        :rtype: Atom
        """
        atom = Atom(*args, **kwargs)
        self.add(atom)
        return atom

    def bond(self, atom: Atom, other_atom: Atom, *args, **kwargs):
        """
        Bonds two atoms together, one of which must exist in this molecule.

        Takes two positional arguments for the two atoms to bond,
        and the rest of the arguments are passed to :meth:`Atom.bond`.

        :param atom: The atom to bond
        :type atom: Atom
        :param other_atom: The other atom to bond
        :type other_atom: Atom
        :raises ValueError: If neither atom exists in this moleculee
        """
        if atom not in self._atoms and other_atom not in self._atoms:
            raise ValueError("Neither atom exists in this molecule")
        atom.bond(other_atom, *args, **kwargs)

    def elem_count(self, element: Element) -> int:
        """
        Returns the number of atoms of the specified element

        :param element: The element to count
        :type element: Element
        :return: The number of atoms of that element
        :rtype: int
        """
        return sum(1 for atom in self._atoms if atom.element == element)

    def all_elem_counts(self) -> Dict[Element, int]:
        """
        Returns a dictionary of the count of each element in this molecule,
        if there are atoms of that element.

        :return: A dictionary mapping element to element count
        :rtype: Dict[Element, int]
        """
        counts = {}
        for atom in self._atoms:
            counts.setdefault(atom.element, 0)
            counts[atom.element] += 1

        return counts

    def atoms(
        self, elements: Optional[Union[Element, Sequence[Element]]] = None, **kwargs
    ) -> List[Atom]:
        """
        Returns atoms in this molecule with specified properties.

        The sole positional argument is an :class:`Element`
        or sequence of :class:`Element` to search for.

        The remaining arguments must be keyword arguments,
        that specify the desired value of attributes on an instance of :class:`Atom`.

        Examples:
        >>> molecule.atoms()  # All atoms
        >>> molecule.atoms(Element.H)  # All hydrogen atoms
        >>> molecule.atoms(aromatic=True)  # All aromatic atoms
        >>> molecule.atoms(aromati=True)  # Mispelling of 'aromatic', returns empty list

        :param element: The element to search for
        :type element: Element
        :return: The list of atoms
        :rtype: List[Atom]
        """
        if elements is None:
            elements = Element
        elif isinstance(elements, Element):
            elements = (elements,)
        atoms = []
        for atom in self._atoms:
            for attr, value in kwargs.items():
                try:
                    if getattr(atom, attr) != value:
                        break
                except AttributeError:
                    break
            else:
                if atom.element in elements:
                    atoms.append(atom)

        return atoms

    def merge(self, *others: "Molecule"):
        """
        Merges other molecules with these molecule.

        This has the effect of adding the other molecules' atoms to this molecule.

        The other molecules are unchanged by this method
        """
        for other in others:
            self._atoms = self._atoms.union(other._atoms)
        for atom in self._atoms:
            atom.molecule = self

    def __iter__(self) -> Iterator[Atom]:
        """
        Iterates over the atoms of the molecule
        """
        return iter(self._atoms.copy())

    def __str__(self):
        sort_order = [
            Element.C,
            Element.H,
        ]
        counts = {
            k: v
            for k, v in sorted(
                self.all_elem_counts().items(),
                key=lambda x: (
                    str(sort_order.index(x[0])) if x[0] in sort_order else x[0].name
                ),
            )
        }
        s = "".join(
            "{}{}".format(element.name, count if count > 1 else "")
            for element, count in counts.items()
        )
        charge = sum(atom.charge for atom in self._atoms)
        if charge:
            s = "[{}]{}{}".format(
                s, abs(charge) if abs(charge > 1) else "", "+" if charge > 0 else "-"
            )

        return s
