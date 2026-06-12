% Facts: person(Name, DOB)

person('Nithya', '15-08-2003').
person('Rahul', '20-01-2002').
person('Priya', '10-05-2004').
person('Arun', '25-12-2001').

% Rule to find DOB of a person
dob(Name, DOB) :-
    person(Name, DOB).
