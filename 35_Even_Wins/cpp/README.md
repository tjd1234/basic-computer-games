# Additional Features

### Better Title

When the program starts, the program title is written like this:

```
Welcome to Even Wins!
```

Modify [evenwins.cpp](evenwins.cpp) so the title is printed in a text box like
this:

```
+-----------------------+
| Welcome to Even Wins! |
+-----------------------+
```

Put your updated code in [evenwins1.cpp](evenwins1.cpp).


### An Enumerated Type for Turns

In [evenwins.cpp](evenwins.cpp), the variable `whose_turn` has type `string`.
However, we only care about two strings: `"human"` and `"computer"`. If we
mis-type these strings then errors will occur.

We can get the compiler to help catch these errors by using an **enumerated
type**. To do this, replace the declaration `string whose_turn` with this:

```
enum class Player {
    human,
    computer
};

Player whose_turn;
```

Now `whose_turn` is a variable of type `Player`, and it can only be assigned
values `Player::human` or `Player::computer`, e.g.:

```
whose_turn = Player::human;
```

If you try to assign it any other value, the compiler will stop with an error:

```
whose_turn = human; // compiler error!
```

You can also test if `whose_turn` has a particular value:

```
if (whose_turn == Player::computer) {
	// ...
}
```

Modify [evenwins1.cpp](evenwins1.cpp) to use `Player` for `whose_turn` instead
of `string`. Put your updated code in [evenwins2.cpp](evenwins2.cpp).


### Wins and Losses

Modify [evenwins2.cpp](evenwins2.cpp) so that at the end of every game it
tells the user how many games they and the computer have won, e.g.:

```
  Statistics
  ----------
   total games: 7
    human wins: 5
 computer wins: 2
```

Put your updated code in [evenwins3.cpp](evenwins3.cpp).


### Random Taunts

When the computer wins a game, it prints a *taunt* "tremble before it's mighty
brain!":

```
cout << "The computer wins: tremble before it's mighty brain!\n";
```

Modify [evenwins3.cpp](evenwins3.cpp) so that it prints a randomly chosen
taunt each time the computer wins a game. Choose at least 5 different taunts
(one of them can be the one already in the program), and make your taunts
kid-friendly.

Put your updated code in [evenwins4.cpp](evenwins4.cpp).


### Removing Global Variables

In general, global variables are a *bad* idea in programming because it can be
very difficult to know when they change, and which part of a program changes
them. Global variables might not cause problems in *small* programs, but as
your programs get bigger and more complex, global variables are more and more
likely to be the reason for subtle and hard to fix problems.

Modify [evenwins4.cpp](evenwins4.cpp) so it has *no global variables*. To do
this, implement a struct called `Gamestate` that looks like this:

```
struct Gamestate {
    //
    // ... all variables needed for a game go here ...
    //
};
```

Then create one `Gamestate` struct inside `main`, and pass it to, and return
it from, functions as needed. To return values, you can use pass-by-reference.

Global *constants* are permitted, i.e. variables declared using `const` are
permitted since they can't be changed.

Put your updated code in [evenwins5.cpp](evenwins5.cpp).


### The ? : Operator

Modify [evenwins5.cpp](evenwins5.cpp) so that the `next_player` functions uses
the `?` `:` operator. The entire body of `next_player` should use a single
`;`!

Put your updated code in [evenwins6.cpp](evenwins6.cpp).
