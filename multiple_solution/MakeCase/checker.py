import subprocess
import os
import re
import glob

CHECKER_CPP_FILE = 'checker.cpp'
CHECKER_EXECUTION_FILE = 'checker.out'
USER_CPP_FILE = '../submissions/userCode.cpp'
USER_EXECUTION_FILE = '../submissions/userCode.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'
USER_FOLDER = '../data/user/'

# 編譯
subprocess.run(['g++', CHECKER_CPP_FILE, '-o', CHECKER_EXECUTION_FILE], check=True)
subprocess.run(['g++', USER_CPP_FILE, '-o', USER_EXECUTION_FILE], check=True)

def clear_data():
    pattern = re.compile(r'\.ans$')  # 匹配 .ans 結尾的檔案名稱
    for folder in [USER_FOLDER]:
        for filename in os.listdir(folder):
            if pattern.search(filename):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)

def user_output(inputFile, userFile):
    with open(inputFile, 'r') as f_in:
        stdin_content = f_in.read()
        process = subprocess.run([USER_EXECUTION_FILE], input=stdin_content.encode(), capture_output=True)
    with open(userFile, 'w') as f_out:
        f_out.write(process.stdout.decode())

def checker_output(inputFile, ansFile, userFile, caseName):
    argv = [inputFile, ansFile, userFile]
    checker_process = subprocess.run(['./' + CHECKER_EXECUTION_FILE] + argv, capture_output=True, text=True)
    print('case', caseName, ':', checker_process.stderr, end='')

if __name__ == '__main__':
    clear_data()

    # 處理 sample 測試案例
    sample_cases = glob.glob(os.path.join(SAMPLE_FOLDER, '*.in'))
    for input_file in sample_cases:
        case_name = os.path.splitext(os.path.basename(input_file))[0]
        user_output(input_file, USER_FOLDER + case_name + '.ans')
        checker_output(input_file, SAMPLE_FOLDER + case_name + '.ans', USER_FOLDER + case_name + '.ans', case_name)

    # 處理 secret 測試案例
    secret_cases = glob.glob(os.path.join(SECRET_FOLDER, '*.in'))
    for input_file in secret_cases:
        case_name = os.path.splitext(os.path.basename(input_file))[0]
        user_output(input_file, USER_FOLDER + case_name + '.ans')
        checker_output(input_file, SECRET_FOLDER + case_name + '.ans', USER_FOLDER + case_name + '.ans', case_name)

    # 刪除執行檔
    if os.path.exists(CHECKER_EXECUTION_FILE):
        os.remove(CHECKER_EXECUTION_FILE)
    if os.path.exists(USER_EXECUTION_FILE):
        os.remove(USER_EXECUTION_FILE)
