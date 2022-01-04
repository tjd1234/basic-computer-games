// evenwins6.cpp

//
// Based on evenwins5.cpp. next_player re-written using a switch statement.
//

#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

enum class Player {
    human,
    computer
};

struct Gamestate {
    int marbles_in_middle = -1;
    int human_marbles     = -1;
    int computer_marbles  = -1;
    int human_wins        = 0;
    int computer_wins     = 0;
    Player whose_turn;
};

const vector<string> taunts = {
    "tremble before it's mighty brain!",
    "it's unbeatable!",
    "respect the silicon!",
    "it is the best!",
    "the computer beats all!"
};

string get_rand_taunt() {
    int n = taunts.size();
    int r = rand() % n;
    return taunts[r];
}

void welcome_screen() {
    cout << "+-----------------------+\n"
         << "| Welcome to Even Wins! |\n"
         << "+-----------------------+\n\n";

    cout << "Even Wins is a two-person game. You start with\n";
    cout << "27 marbles in the middle of the table.\n";
    cout << "\n";
    cout << "Players alternate taking marbles from the middle.\n";
    cout << "A player can take 1 to 4 marbles on their turn, and\n";
    cout << "turns cannot be skipped. The game ends when there are\n";
    cout << "no marbles left, and the winner is the one with an even\n";
    cout << "number of marbles.";
    cout << "\n";
}

string marbles_str(int n) {
    if (n == 1) return "1 marble";
    return to_string(n) + " marbles";
}

void choose_first_player(Gamestate& state) {
   for (;;) {
        cout << "\nDo you want to play first? (y/n) --> ";
        string ans;
        cin >> ans;
        if (ans == "y") {
            state.whose_turn = Player::human;
            return;
        } else if (ans == "n") {
            state.whose_turn = Player::computer;
            return;
        } else {
            cout << "\nPlease enter 'y' if you want to play first,\n";
            cout << "or 'n' if you want to play second.\n";
        }
    }
} // choose_first_player

void next_player(Gamestate& state) {
    state.whose_turn = (state.whose_turn == Player::human) 
                      ? Player::computer
                      : Player::human;
    // switch (state.whose_turn) {
    //     case Player::human    : state.whose_turn = Player::computer;
    //     case Player::computer : state.whose_turn = Player::human;
    // }
}

void print_board(const Gamestate& state) {
    cout << "\n";
    cout << " marbles in the middle: " << state.marbles_in_middle 
         << " " << string(state.marbles_in_middle, '*') << "\n";
    cout << "    # marbles you have: " << state.human_marbles << "\n";
    cout << "# marbles computer has: " << state.computer_marbles << "\n";
    cout <<  "\n";
}

// returns true if s is an int, and false otherwise
// https://www.cplusplus.com/reference/string/stoi/
bool is_int(const string& s) {
    try {
        stoi(s); // throws an invalid_argument exception if conversion fails
        return true;
    } catch (...) {
        return false;
    }
}

void human_turn(Gamestate& state) {
    // get number in range 1 to min(4, marbles_in_middle)
    int max_choice = min(4, state.marbles_in_middle);
    cout << "It's your turn!\n";
    for(;;) {
        cout << "Marbles to take? (1 - " << max_choice << ") --> ";
        string s;
        cin >> s;
        if (!is_int(s)) {
            cout << "\n  Please enter a whole number from 1 to " << max_choice
                 << "\n";
            continue;
        }

        // convert s to an int so it can be compared
        int n = stoi(s);
        if (n < 1) {
            cout << "\n  You must take at least 1 marble\n";
            continue;
        }
        if (n > max_choice) {
            cout << "\n  You can take at most " << marbles_str(max_choice)
                 << "\n";
            continue;
        }

        cout << "\nOkay, taking " << marbles_str(n) << " ...\n";
        state.marbles_in_middle -= n;
        state.human_marbles += n;

        return;
    } // for
} // human_turn

void computer_turn(Gamestate& state) {
    cout << "It's the computer's turn ...\n";
    int max_choice = min(4, state.marbles_in_middle);

    // choose at random
    int n = 1 + rand() % max_choice;
    cout << "Computer takes " << marbles_str(n) << " ...\n";
    state.marbles_in_middle -= n;
    state.computer_marbles += n;
}

void game_over(Gamestate& state) {
    cout << "\n";
    cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
         << "!! All the marbles are taken: Game Over !!\n"
         << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n";
    print_board(state);
    if (state.human_marbles % 2 == 0) {
        cout << "You are the winner! Congratulations!\n";
        state.human_wins++;        
    } else {
        // cout << "The computer wins: tremble before it's mighty brain!\n";
        cout << "The computer wins: "
             << get_rand_taunt()
             << "\n";
        state.computer_wins++;
    }
    int total_games = state.human_wins + state.computer_wins;
    cout << "\n  Statistics\n" 
         <<   "  ----------\n"
         << "   total games: " << total_games         << "\n"
         << "    human wins: " << state.human_wins    << "\n"
         << " computer wins: " << state.computer_wins << "\n";
} // game_over

void play_game(Gamestate& state) {
    // initialize the game state
    state.marbles_in_middle = 27;
    state.human_marbles = 0;
    state.computer_marbles = 0;
    print_board(state);

    for (;;) {
        if (state.marbles_in_middle == 0) {
            game_over(state);
            return;
        } else if (state.whose_turn == Player::human) {
            human_turn(state);
            print_board(state);
            next_player(state);
        } else if (state.whose_turn == Player::computer) {
            computer_turn(state);
            print_board(state);
            next_player(state);
        }
    } // for
} // play_game

int main() {
    srand(time(NULL));

    welcome_screen();
    Gamestate state;

    for(;;) {
        choose_first_player(state);
        play_game(state);

        // ask if the user if they want to play again
        cout << "\nWould you like to play again? (y/n) --> ";
        string again;
        cin >> again;
        if (again == "y") {
            cout << "\nOk, let's play again ...\n";
        } else {
            cout << "\nOk, thanks for playing ... goodbye!\n";
            return 0;
        }
    } // for
} // main
