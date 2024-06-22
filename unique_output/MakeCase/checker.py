import subprocess
import os, re

CPP_FILE = 'checker.cpp'
EXECUTION_FILE = 'checker.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'
USER_FOLDER = '../data/user/'

# 編譯
compile_process = subprocess.run(['g++', CPP_FILE, '-o', EXECUTION_FILE], check = True)

def clear_data():
    pattern = re.compile(r'^\d+\.ans$')  # 匹配數字開頭，以 .ans 結尾的檔案名稱

    for folder in [USER_FOLDER]:
        for filename in os.listdir(folder):
            if pattern.match(filename):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)

def output(case_number, folder):
    input_file = folder + f'{case_number}.in'
    answer_file = folder + f'{case_number}.ans'
    user_file = USER_FOLDER + f'{case_number}.ans'

    # 重新導向標準輸入到 .in 文件
    with open(input_file, 'r') as f_in:
        stdin_content = f_in.read()
        process = subprocess.run(['./' + EXECUTION_FILE], input = stdin_content.encode(), capture_output = True)

    # 將輸出寫入 .ans 文件
    with open(user_file, 'w') as f_out:
        f_out.write(process.stdout.decode())
        
    argv = [input_file, answer_file, user_file]
    checker_process = subprocess.run(['./' + EXECUTION_FILE] + argv, capture_output = True, text = True)
    print('case', i, ':', checker_process.stderr, end = '')

if __name__ == '__main__':
    import sys
    sample_test_num = int(sys.argv[1])
    total_test_num = int(sys.argv[2])

    clear_data()

    # 創建 sample 測試案例的輸入和輸出文件
    for i in range(1, sample_test_num + 1):
        output(i, SAMPLE_FOLDER)

    # 創建 secret 測試案例的輸入和輸出文件
    for i in range(sample_test_num + 1, total_test_num + 1):
        casename = SECRET_FOLDER + f'{i}'
        output(i, SECRET_FOLDER)

    if (os.path.exists(EXECUTION_FILE)):
        os.remove(EXECUTION_FILE)
