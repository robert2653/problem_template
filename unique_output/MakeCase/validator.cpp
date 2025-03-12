/**
 * Validates that the first line contains the integer between 1 and 10^5, inclusive.
 * The second line should contains space-separated sequence of integers between -10^15 and 10^15, inclusive.
 * Also validates that file ends with EOLN and EOF.
 */

// 範例: 檢查多筆測資
#include "../testlib.h"
using namespace std;

int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    int t = inf.readInt(1, 10000, "t");
    inf.readEoln();
    long long sum = 0;
    for (int i = 0; i < t; i++) {
        int n = inf.readInt(1, 200000, "n");
        inf.readSpace();
        int k = inf.readInt(1, 5, "k");
        inf.readEoln();
        vector<long long> v = inf.readLongs(n, 0LL, 1000000000LL, "a[i]");
        inf.readEoln();
        sum += n;
    }
    ensure(sum <= 1000000000);

    inf.readEof();
    return 0;
}