import os


# 语法检测
def is_correct(code: str):
    # 将代码存为.py文件
    with open('code.py', 'w') as fc:
        fc.write(code)
    # 调用cmd,获取检查结果
    os.system('(pyflakes code.py) 1>1.txt 2>&1')
    with open('1.txt', 'r') as f1:
        text = f1.read()
    # debug
    print(f'----------text----------\n{text}', end='')
    # 判断结果
    if text:
        return False
    else:
        return True


def test_code(filename: str):
    with open(filename, 'r') as fc:
        code = fc.read()
        return is_correct(code)


if __name__ == '__main__':
    print(f"测试未定义            --> 理论结果、实际结果分别为: False-->{test_code('test_code_001.py')}")
    # print(f"测试缺括号            --> 理论结果、实际结果分别为: False-->{test_code('test_code_002.py')}")
    # print(f"测试try内部异常        --> 理论结果、实际结果分别为: False-->{test_code('test_code_003.py')}")
    # print(f"测试运行异常,语法无异常 --> 理论结果、实际结果分别为: True-->{test_code('test_code_004.py')}")
