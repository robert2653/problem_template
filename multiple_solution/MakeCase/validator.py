import subprocess
import os
import glob

CPP_FILE = 'validator.cpp'
EXECUTION_FILE = 'validator.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'

# 編譯
compile_process = subprocess.run(['g++', CPP_FILE, '-o', EXECUTION_FILE], check=True)

def output(case_name):
    input_file = f'{case_name}.in'

    # 重新導向標準輸入到 .in 文件
    with open(input_file, 'r') as f_in:
        stdin_content = f_in.read()
        run_process = subprocess.run(['./' + EXECUTION_FILE], input=stdin_content.encode(), capture_output=True)
        print(f'case {case_name}:', run_process.stderr.decode())

if __name__ == '__main__':
    # 找出 sample 資料夾中的所有 .in 檔案
    sample_cases = glob.glob(os.path.join(SAMPLE_FOLDER, '*.in'))
    for case in sample_cases:
        casename = os.path.splitext(case)[0]  # 取得不含副檔名的檔案名稱
        output(casename)

    # 找出 secret 資料夾中的所有 .in 檔案
    secret_cases = glob.glob(os.path.join(SECRET_FOLDER, '*.in'))
    for case in secret_cases:
        casename = os.path.splitext(case)[0]  # 取得不含副檔名的檔案名稱
        output(casename)

    if os.path.exists(EXECUTION_FILE):
        os.remove(EXECUTION_FILE)
