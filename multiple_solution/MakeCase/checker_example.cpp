#include <bits/stdc++.h>
#include "../testlib.h"
using namespace std;
 
void check(vector<string> files) { // inf(input), ouf(judge), ans(user)
    setName("mutiple solution judge");
    char *argv[4];
    for (int i = 1; i <= 3; i++) {
        argv[i] = new char(files[i - 1].length());
        strcpy(argv[i], files[i - 1].c_str());
    }

    registerTestlibCmd(4, argv);
    // do something
    // 讀完 input

    // 讀完 judge ans

    // 讀 user output

    // do something
    while (!ouf.seekEof()) { ouf.readLine(); }
    if (ans.seekEof() && ouf.seekEof()) {
        quitf(_ok, "AC");
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