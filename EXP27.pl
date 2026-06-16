edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(d,g).
edge(e,g).

best_first(Start,Goal) :-
    path(Start,Goal).

path(Goal,Goal).

path(Start,Goal) :-
    edge(Start,Next),
    path(Next,Goal).
