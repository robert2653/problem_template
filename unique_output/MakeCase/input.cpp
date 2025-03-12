#include "../testlib.h"
using namespace std;
using ll = long long;

map<int, Spec> specs = {};

void rand_output(int casenum, Spec spec) {}

vector<string> samples {};

void manual_secret(int casenum) {}

int main(int argc, char **argv) { // sample total 要跳過的測資...
    registerGen(argc, argv, 1);
    vector<int> steps;
    int sample_test_num = stoi(argv[1]), total_test_num = stoi(argv[2]);
    for (int i = 3; i < argc; i++) {
        steps.push_back(stoi(argv[i]));
    }
    auto order = [](int n) { // 測資照字典序，個位數前導補 0
        string res = (n < 10 ? "0" : "");
        res += to_string(n);
        return res;
    };
    for (int i = 1; i <= 200; i++) {
        bool b = true;
        for (auto &j : steps) if (i == j) b = false;
        if (!b) continue;
        string sample_in = "../data/sample/" + order(i) + ".in";
        remove(sample_in.c_str());
        string sample_ans = "../data/sample/" + order(i) + ".ans";
        remove(sample_ans.c_str());
        string secret_in = "../data/secret/" + order(i) + ".in";
        remove(secret_in.c_str());
        string secret_ans = "../data/secret/" + order(i) + ".ans";
        remove(secret_ans.c_str());
    }
    for (int i = 1; i <= sample_test_num; i++) {
        string filename = "../data/sample/" + order(i) + ".in";
        freopen((filename).c_str(), "w", stdout);
        cout << samples[i - 1];
        fclose(stdout);
    }
    for (int i = sample_test_num + 1; i <= total_test_num; i++) {
        bool b = true;
        for (auto &j : steps) if (i == j) continue;
        string filename = "../data/secret/" + order(i) + ".in";
        freopen((filename).c_str(), "w", stdout);
        if (specs.count(i)) {
            rand_output(i, specs[i]);
            fclose(stdout);
        } else {
            manual_secret(i);
            fclose(stdout);
            if (ifstream(filename).peek() == EOF) {
                cerr << "Error: " << filename << " is empty." << "\n";
                remove(filename.c_str());
                exit(1);
            }
        }
    }
    freopen("/dev/tty", "w", stdout); 
    freopen("/dev/tty", "r", stdin);
    return 0;
}