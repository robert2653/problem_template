import subprocess
import os, re

CHECKER_CPP_FILE = 'checker.cpp'
CHECKER_EXECUTION_FILE = 'checker.out'
USER_CPP_FILE = '../submissions/userCode.cpp'
USER_EXECUTION_FILE = '../submissions/userCode.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'
USER_FOLDER = '../data/user/'

# 編譯
subprocess.run(['g++', CHECKER_CPP_FILE, '-o', CHECKER_EXECUTION_FILE], check = True)
subprocess.run(['g++', USER_CPP_FILE, '-o', USER_EXECUTION_FILE], check = True)

def clear_data():
    pattern = re.compile(r'^\d+\.ans$')  # 匹配數字開頭，以 .ans 結尾的檔案名稱
    for folder in [USER_FOLDER]:
        for filename in os.listdir(folder):
            if pattern.match(filename):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)

def user_output(inputFile, userFile):
    with open(inputFile, 'r') as f_in:
        stdin_content = f_in.read()
        process = subprocess.run([USER_EXECUTION_FILE], input = stdin_content.encode(), capture_output = True)
    with open(userFile, 'w') as f_out:
        f_out.write(process.stdout.decode())

def checker_output(inputFile, ansFile, userFile, caseName):
    argv = [inputFile, ansFile, userFile]
    checker_process = subprocess.run(['./' + CHECKER_EXECUTION_FILE] + argv, capture_output = True, text = True)
    print('case', caseName, ':', checker_process.stderr, end = '')

if __name__ == '__main__':
    import sys
    sample_test_num = int(sys.argv[1])
    total_test_num = int(sys.argv[2])

    clear_data()

    for i in range(1, sample_test_num + 1):
        user_output(SAMPLE_FOLDER + f'{i}' + '.in', USER_FOLDER + f'{i}' + '.ans')
    for i in range(sample_test_num + 1, total_test_num + 1):
        user_output(SECRET_FOLDER + f'{i}' + '.in', USER_FOLDER + f'{i}' + '.ans')

    for i in range(1, sample_test_num + 1):
        checker_output(SAMPLE_FOLDER + f'{i}' + '.in', SAMPLE_FOLDER + f'{i}' + '.ans', USER_FOLDER + f'{i}' + '.ans', i)
    for i in range(sample_test_num + 1, total_test_num + 1):
        checker_output(SECRET_FOLDER + f'{i}' + '.in', SECRET_FOLDER + f'{i}' + '.ans', USER_FOLDER + f'{i}' + '.ans', i)

    if (os.path.exists(CHECKER_EXECUTION_FILE)):
        os.remove(CHECKER_EXECUTION_FILE)
    if (os.path.exists(USER_EXECUTION_FILE)):
        os.remove(USER_EXECUTION_FILE)
