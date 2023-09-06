female(pam).
male(tom).
male(bob).
female(liz).
female(ann).
female(pat).
male(jim).
parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
