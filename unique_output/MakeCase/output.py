import subprocess
import os
import re
import glob

CPP_FILE = '../submissions/accepted/ac.c'
EXECUTION_FILE = '../submissions/accepted/ac.out'
SAMPLE_FOLDER = '../data/sample/'
SECRET_FOLDER = '../data/secret/'

# 編譯
compile_process = subprocess.run(['gcc', CPP_FILE, '-o', EXECUTION_FILE], check=True)

def output(case_name):
    input_file = f'{case_name}.in'
    output_file = f'{case_name}.ans'

    # 重新導向標準輸入到 .in 文件
    with open(input_file, 'r') as f_in:
        stdin_content = f_in.read()
        process = subprocess.run([EXECUTION_FILE], input=stdin_content.encode(), capture_output=True)

    # 將輸出寫入 .ans 文件
    with open(output_file, 'w') as f_out:
        f_out.write(process.stdout.decode())

def clear_data():
    pattern = re.compile(r'\.ans$')  # 匹配 .ans 結尾的檔案名稱
    for folder in [SAMPLE_FOLDER, SECRET_FOLDER]:
        for filename in os.listdir(folder):
            if pattern.match(filename):
                file_path = os.path.join(folder, filename)
                os.remove(file_path)

if __name__ == '__main__':
    clear_data()

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
