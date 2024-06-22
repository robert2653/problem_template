import subprocess
import os

CPP_FILE = 'validator.cpp'
EXECUTION_FILE = 'validator.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'

# 編譯
compile_process = subprocess.run(['g++', CPP_FILE, '-o', EXECUTION_FILE], check = True)

def output(case_name):
    input_file = f'{case_name}.in'

    # 重新導向標準輸入到 .in 文件
    with open(input_file, 'r') as f_in:
        stdin_content = f_in.read()
        run_process = subprocess.run(['./' + EXECUTION_FILE], input = stdin_content.encode(), capture_output = True)
        print('case', i, ':', run_process.stderr)


if __name__ == '__main__':
    import sys
    sample_test_num = int(sys.argv[1])
    total_test_num = int(sys.argv[2])

    for i in range(1, sample_test_num):
        casename = SAMPLE_FOLDER + f'{i}'
        output(casename)

    for i in range(sample_test_num + 1, total_test_num + 1):
        casename = SECRET_FOLDER + f'{i}'
        output(casename)

    if (os.path.exists(EXECUTION_FILE)):
        os.remove(EXECUTION_FILE)
