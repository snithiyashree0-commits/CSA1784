symptom(fever).
symptom(cough).
symptom(headache).

disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(migraine) :-
    symptom(headache).
