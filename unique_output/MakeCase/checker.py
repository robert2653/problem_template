import subprocess
import os
import re
import glob

CHECKER_CPP_FILE = 'checker.cpp'
CHECKER_EXECUTION_FILE = 'checker.exe'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'
USER_FOLDER = '../data/user/'

USER_SUBMISSIONS_FOLDER = '../submissions/'
MAMUAL_CPP_FILE = [
    '../submissions/accepted/ac.cpp',
    # '../submissions/wrong_answer/wa.cpp',
    '../submissions/time_limit/tle.cpp',
]

TIME_LIMIT = 1  # seconds
class TimeoutException(Exception):
    pass

# 編譯 checker
subprocess.run(['g++', CHECKER_CPP_FILE, '-o', CHECKER_EXECUTION_FILE], check=True)

def clear_data():
    pattern = re.compile(r'\.ans$')  # 匹配 .ans 結尾的檔案名稱
    for folder in [USER_FOLDER]:
        for filename in os.listdir(folder):
            if pattern.search(filename):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)

def run_with_timeout(cmd, input_data, timeout):
    """
    執行程式並設置時間限制
    返回 (執行狀態碼, 輸出結果)
    狀態碼：
    - 0: 正常執行
    - 1: 超時
    - 2: 執行錯誤
    """
    def target(proc, input_data):
        try:
            stdout, stderr = proc.communicate(input=input_data, timeout=timeout)
            return proc.returncode, stdout
        except subprocess.TimeoutExpired:
            proc.kill()
            raise TimeoutException()

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        returncode, stdout = target(proc, input_data)
        return 0, stdout  # 正常執行
    except TimeoutException:
        return 1, None    # 超時
    except Exception as e:
        return 2, None    # 執行錯誤

def user_output(inputFile, userFile, user_executable):
    """
    執行使用者程式並產生輸出
    返回執行狀態：
    - "OK": 正常執行
    - "TLE": 超時
    - "RE": 執行錯誤
    """
    with open(inputFile, 'r') as f_in:
        stdin_content = f_in.read().encode()
        
        status, result = run_with_timeout([user_executable], stdin_content, TIME_LIMIT)
        
        with open(userFile, 'w') as f_out:
            if status == 1:  # TLE
                f_out.write("")  # 超時時不寫入任何內容
                return "TLE"
            elif status == 2:  # RE
                f_out.write("")  # 執行錯誤時不寫入任何內容
                return "RE"
            else:  # 正常執行
                f_out.write(result.decode())
                return "OK"

def checker_output(inputFile, ansFile, userFile, caseName):
    """
    執行檢查器並輸出結果
    """
    argv = [inputFile, ansFile, userFile]
    checker_process = subprocess.run(['./' + CHECKER_EXECUTION_FILE] + argv, capture_output=True, text=True)
    print('case', caseName, ':', checker_process.stderr, end='')

def testing(userCPP):
    # 確定 user_executable 的路徑
    user_executable = os.path.splitext(userCPP)[0] + '.exe'
    
    # 編譯 userCPP
    try:
        subprocess.run(['g++', userCPP, '-o', user_executable], check=True)
    except subprocess.CalledProcessError:
        print(f'Compilation Error: {userCPP}')
        return
    
    print(f'Testing {userCPP}.')

    # 處理 sample 測試案例
    sample_cases = glob.glob(os.path.join(SAMPLE_FOLDER, '*.in'))
    for input_file in sample_cases:
        case_name = os.path.splitext(os.path.basename(input_file))[0]
        result = user_output(input_file, USER_FOLDER + case_name + '.ans', user_executable)
        if result == "TLE":
            print(f'Case {case_name}: Time Limit Exceeded')
            continue
        elif result == "RE":
            print(f'Case {case_name}: Runtime Error')
            continue
        checker_output(input_file, SAMPLE_FOLDER + case_name + '.ans',
                       USER_FOLDER + case_name + '.ans', case_name)

    # 處理 secret 測試案例
    secret_cases = glob.glob(os.path.join(SECRET_FOLDER, '*.in'))
    for input_file in secret_cases:
        case_name = os.path.splitext(os.path.basename(input_file))[0]
        result = user_output(input_file, USER_FOLDER + case_name + '.ans', user_executable)
        if result == "TLE":
            print(f'Case {case_name}: Time Limit Exceeded')
            continue
        elif result == "RE":
            print(f'Case {case_name}: Runtime Error')
            continue
        checker_output(input_file, SECRET_FOLDER + case_name + '.ans',
                       USER_FOLDER + case_name + '.ans', case_name)

    os.remove(user_executable)
    print(f'Testing {userCPP} completed.\n')

if __name__ == '__main__':
    clear_data()

    # 指定路徑中的執行檔案列表
    try:
        for userCPP in MAMUAL_CPP_FILE:
            testing(userCPP)
    except Exception as e:
        print('Error:', e)

    # 遍歷 USER_SUBMISSIONS_FOLDER, 找到 cpp
    try:
        userCPPFiles = glob.glob(os.path.join(USER_SUBMISSIONS_FOLDER, '*.cpp'))
        for userCPP in userCPPFiles:
            testing(userCPP)
    except Exception as e:
        print('Error:', e)

    # 刪除 checker 執行檔
    if os.path.exists(CHECKER_EXECUTION_FILE):
        os.remove(CHECKER_EXECUTION_FILE)