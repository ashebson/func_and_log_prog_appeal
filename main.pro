handle_num(X,Y):-sqrt(X,XSQ),X5 is X**5, Y = [XSQ,X5].
handle_list([],[]).
handle_list([HX|X],[HY|Y]):-number(HX),handle_num(HX,HY),handle_list(X,Y),!.
handle_list([HX|X],[HY|Y]):-is_list(HX),handle_list(HX,HYR),reverse(HYR, HY),handle_list(X,Y).
job(X,Z):-handle_list(X,Y),reverse(Y,Z).


%job([[4.0,16.0],9.0],Z).
