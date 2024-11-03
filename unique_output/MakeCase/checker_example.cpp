#include <bits/stdc++.h>
#include "../testlib.h"
using namespace std;
using ll = long long;

// 本地 checker，非嚴格比對，可以自己改，參考 testlib.h
void check(vector<string> files) { // inf(input), ouf(judge), ans(user)
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

        ouf.readWordTo(j);
        ans.readWordTo(p);

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
int main(int argc, char **argv) { // sample total
    string inputFile = toString(argv[1]);
    string answerFile = toString(argv[2]);
    string userFile = toString(argv[3]);
    check({inputFile, answerFile, userFile});
    return 0;
}