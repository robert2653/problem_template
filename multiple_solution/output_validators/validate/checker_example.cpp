#include <bits/stdc++.h>
using namespace std;

// domjudge form checker
void wa(string log = "wrong answer") {
    cerr << log << ".";
    exit(43); // 答案錯誤時呼叫這個
}
void accept() {
    cerr << "accepted.";
    exit(42);
}
void check_accepted() {
    string remain;
    if (cin >> remain) wa("redundant output");
    accept();
}

// user_output: stdin
// .in: argv[1]
// .ans: argv[2]
int main(int argc, char *argv[]) {
    ifstream input;
    ifstream output;
    input.open(argv[1]);
    if (!input) wa("cannot open input");
    output.open(argv[2]);
    if (!output) wa("cannot open output");

    

    check_accepted();
    return 0;
}