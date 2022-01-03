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


### Removing Global Variables

In general, global variables are a *bad* idea in programming because it can be
very difficult to know when they change, and which part of a program changes
them. In small programs global variables may not be too much of a problem, but
as your programs get bigger and more complex, global variables are more and
more of a problem.

