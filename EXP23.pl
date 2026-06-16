male(john).
male(peter).

female(mary).
female(anna).

parent(john,peter).
parent(mary,peter).
parent(john,anna).
parent(mary,anna).

father(X,Y) :-
    parent(X,Y),
    male(X).

mother(X,Y) :-
    parent(X,Y),
    female(X).

sibling(X,Y) :-
    parent(Z,X),
    parent(Z,Y),
    X \= Y.
