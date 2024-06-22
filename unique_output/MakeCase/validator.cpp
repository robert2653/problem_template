/**
 * Validates that the first line contains the integer between 1 and 10^5, inclusive.
 * The second line should contains space-separated sequence of integers between -10^15 and 10^15, inclusive.
 * Also validates that file ends with EOLN and EOF.
 */

// 範例: 檢查四個在範圍內的數字
#include "../testlib.h"
using namespace std;

int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    vector<long long> v = inf.readLongs(4, 0LL, 10000000000000000LL);

    inf.readEoln();

    inf.readEof();
}