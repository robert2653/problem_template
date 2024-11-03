把後綴有 _example 的去掉後綴就可以用了

# Input
1. 要會用 ```testlib.h```
2. 使用 cout 寫檔

## Random Output
在 input_controller 設當前 case 的規格，記得 constructor 也要改，
上下限可以在 global 設 const，如 line 7, 8, 14, 15 那樣。

```map<int, input_controller> input_controllers = {}``` 可以手動設置，某筆測資的 case，
例如測資出滿可以放 ```{10, input_controller(N, X)}```，
沒有設置那麼該筆就是看你 ```input_controller``` 的 defalut constructor 怎麼寫的。

再來到 ```void rand_output(input_controller spec = input_controller())```，
先讀當前測資的規格，然後看你怎麼生測資。

## Manaul Output
到 ```void secret(int start, int test_num, vector<int> &step)```，
寫 ```else if (cn == ?) {...}``` 當筆測資就不會跑 ```random_output()```，
就在裡面直接 cout。

## 運行
```shell
g++ input.cpp
```
```shell
a.out [範測數] [全部測資數] [0/1:要不要手動輸入範測] [option:要保留的secret測資編號，會直接pass]
```

例如
```shell
a.out 2 20 1 4 5 6
```
程式會叫你輸入兩個範測 01.in, 02.in，兩次換行結束輸入，
然後跳過 04.in, 05.in, 06.in，不會蓋掉原本的測資。

# Output
直接在 submissions/accepted 寫個 ac.cpp，
然後運行即可
```shell
python output.py
```

# Checker
## Unique Output
1. 到 chcker.py
    - USER_EXECUTION_FOLDER 代表待運行的資料夾，他會跑裡面的 *.cpp
    - MAMUAL_CPP_FILE 可以放手動的檔案，預設有跑 submissions 的三個 state，沒寫就註解掉
2. 然後運行即可
    ```shell
    python checker.py
    ```

## Multiple Solution
1. 寫好 output_validators/validate/checker.cpp，就 domjudge 那樣寫
2. 到 chcker.py
    - USER_EXECUTION_FOLDER 代表待運行的資料夾，他會跑裡面的 *.cpp
    - MAMUAL_CPP_FILE 可以放手動的檔案，預設有跑 submissions 的三個 state，沒寫就註解掉
3. 然後運行即可 
    ```shell
    python checker.py
    ```