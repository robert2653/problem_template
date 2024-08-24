#include "../testlib.h"
using namespace std;
using ll = long long;

// 範例: 生成 n 個 [1, inf] 的數字

const int N = 2E5;
const int X = 1E9;

struct input_controller {
    int n;
    int x;
    input_controller() {
        n = rnd.next(N) + 1;
        x = rnd.next(X) + 1;
    }
};

map<int, input_controller> input_controllers = {
    
};

void rand_output(input_controller spec = input_controller()) {
    int n = spec.n;
    int x = spec.x;
}

void secret(int start, int test_num, vector<int> &step) {
    for (int cn = start; cn <= test_num; cn++) {
        bool b = true;
        for (auto &j : step) if (cn == j) b = false;
        if (!b) continue;
        string filename = "../data/secret/" + to_string(cn) + ".in";
        freopen((filename).c_str(), "w", stdout);
        if (input_controllers.count(cn)) {
            rand_output(input_controllers[cn]);
        }
        // manual output: else if (cn == ?)...




        else rand_output();
        fclose(stdout);
    }
}

void sample(int test_num, int writeIn){
    if (!writeIn) return;
    for (int i = 1; i <= test_num; i++) {
        string filename = "../data/sample/" + to_string(i) + ".in";
        freopen((filename).c_str(), "w", stdout);
        string tmp = "\n";
        cerr << "input task:" << i << ":\n";
        while (true){
            getline(cin, tmp);
            if (tmp.empty()) break;
            cout << tmp << "\n";
        }
        fclose(stdout);
    }
}
void clear(vector<int> &steps){
    for(int i = 1; i <= 100; i++){
        bool b = true;
        for (auto &j : steps) if(i == j) b = false;
        if (!b) continue;
        string sample_in = "../data/sample/" + to_string(i) + ".in";
        string sample_ans = "../data/sample/" + to_string(i) + ".ans";
        remove(sample_in.c_str());
        remove(sample_ans.c_str());
        string secret_in = "../data/secret/" + to_string(i) + ".in";
        string secret_ans = "../data/secret/" + to_string(i) + ".ans";
        remove(secret_in.c_str());
        remove(secret_ans.c_str());
    }
}
int main(int argc, char **argv) { // sample total sampleWriteInMode 要跳過生成的筆數...
    registerGen(argc, argv, 1);

    vector<int> steps;
    int sample_test_num = stoll(argv[1]), total_test_num = stoll(argv[2]), writeIn = stoll(argv[3]);
    for (int i = 4; i < argc; i++) steps.push_back(stoll(argv[i]));
    if (!writeIn) for (int i = 1; i <= sample_test_num; i++) steps.push_back(i);
    clear(steps);

    sample(sample_test_num, writeIn);
    secret(sample_test_num + 1, total_test_num, steps);

    freopen("/dev/tty", "w", stdout); 
    freopen("/dev/tty", "r", stdin);

    return 0;
}