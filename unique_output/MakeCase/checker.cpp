#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    // test code
    
}
 
#include "../testlib.h"
void check(vector<string> files) { // in, ans, user
    setName("compare sequences of tokens");
    char *argv[4];
    for (int i = 1; i <= 3; i++) {
        argv[i] = new char(files[i - 1].length());
        strcpy(argv[i], files[i - 1].c_str());
    }

    registerTestlibCmd(4, argv);

    int n = 0;
    string j, p;

    while (!ans.seekEof() && !ouf.seekEof()) {
        n++;

        ans.readWordTo(j);
        ouf.readWordTo(p);

        if (j != p)
            quitf(_wa, "%d%s words differ - expected: '%s', found: '%s'", n, englishEnding(n).c_str(),
                  compress(j).c_str(), compress(p).c_str());
    }
    if (ans.seekEof() && ouf.seekEof()) {
        if (n == 1)
            quitf(_ok, "\"%s\"", compress(j).c_str());
        else
            quitf(_ok, "%d tokens", n);
    } else {
        if (ans.seekEof())
            quitf(_wa, "Participant output contains extra tokens");
        else
            quitf(_wa, "Unexpected EOF in the participants output");
    }
}
void Output(string inputFileName, string outputFileName) {
    freopen((inputFileName).c_str(), "r", stdin);
    freopen((outputFileName).c_str(), "w", stdout);
    solve();
    fclose(stdin);
    fclose(stdout);
}
int main(int argc, char **argv) { // sample total
    string inputFile = toString(argv[1]);
    string answerFile = toString(argv[2]);
    string userFile = toString(argv[3]);
    Output(inputFile, userFile);
    freopen("/dev/tty", "w", stdout); 
    freopen("/dev/tty", "r", stdin);
    check(vector<string> ({inputFile, answerFile, userFile}));
    return 0;
}