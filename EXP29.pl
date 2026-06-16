fact(a).
fact(b).

fact(c) :-
    fact(a),
    fact(b).

fact(d) :-
    fact(c).
