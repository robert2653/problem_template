#include <bits/stdc++.h>
using namespace std;

void wa(string log = "") {
    cerr << log << "\n";
    exit(43); // 答案錯誤時呼叫這個
}
void accept(){
    cerr << "accepted\n";
    exit(42);
}
void check_accepted() {
    string remain;
    if (cin >> remain) wa("redundant output");
    accept();
}

// user_output: stdin
// .ans: argv[2]
// .in: argv[1]
int main(int argc, char *argv[]) {
    // freopen("../../data/sample/1.txt", "r", stdin);
    ifstream input;
    ifstream output;
    input.open(argv[1]);
    if (!input) wa("cannot open input");
    output.open(argv[2]);
    if (!output) wa("cannot open output");

    

    check_accepted();
    return 0;
}