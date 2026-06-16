diet(diabetes,'Avoid sugar and sweets').
diet(bp,'Reduce salt intake').
diet(obesity,'Low fat diet and exercise').
diet(anemia,'Iron rich foods').

suggest_diet(Disease) :-
    diet(Disease,Diet),
    write(Diet).
