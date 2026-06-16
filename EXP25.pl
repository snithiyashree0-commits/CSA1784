at(monkey,door).
at(box,window).
at(banana,center).

move(monkey,box).
push(box,center).
climb(box).
grasp(banana).

get_banana :-
    move(monkey,box),
    push(box,center),
    climb(box),
    grasp(banana),
    write('Monkey got the banana').
