#include "../testlib.h"
using namespace std;
using ll = long long;

const int X = 1E9;

map<int, Spec> specs = {
    {4, {{"inf", 20}, {"ans", "touch"}}},
    {5, {{"inf", X}}},
    {6, {{"inf", X}}},
    {7, {{"inf", X}}},
    {8, {{"inf", X}}},
    {9, {{"inf", X}}},
    {10, {{"inf", X}}},
    {11, {{"inf", X}}},
};

void rand_output(int casenum, Spec spec) {
    int x = spec.get<int>("inf");
    if (spec.hasKey("ans")) {
        string ans = spec.get<string>("ans");
        if (ans == "touch") {
            cout << "0 0 ";
            cout << 0 << " " << rnd.next(x) << " ";
            cout << 0 << " " << rnd.next(x) << "\n";
            return;
        }
    }
    pair<int, int> res;
    auto gen = [&]() -> pair<int, int> {
        int a = rnd.next(-x, x + 1), b = rnd.next(-x, x + 1);
        return {a, b};
    };
    auto a = gen(), b = gen(), c = gen();
    while (a == b) {
        b = gen();
    }
    cout << a.first << " " << a.second << " " << b.first << " " << b.second << " " << c.first << " " << c.second << "\n";
}

vector<string> samples {
"\
1 1 5 3 2 3\n\
",

"\
1 1 5 3 4 1\n\
",

"\
1 1 5 3 3 2\n\
"
};

void manual_secret(int casenum) {
    if (casenum == 12) {
        cout << "0 0 0 10 0 -10\n";
    }
}

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