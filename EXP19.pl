% Facts:
% record(Student, Teacher, Subject, Code)

record(nithya, kumar, ai, cs301).
record(rahul, priya, dbms, cs302).
record(arun, kumar, ai, cs301).
record(meena, ramesh, java, cs303).

% Rule to find details
details(Student, Teacher, Subject, Code) :-
    record(Student, Teacher, Subject, Code).
