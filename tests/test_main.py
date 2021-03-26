import os
import sys

# 获取项目的绝对路径，并加入到当前的系统路径中
parent = os.path.dirname(os.path.realpath(__file__))               
father_path = os.path.abspath(os.path.dirname(parent))

sys.path.append(father_path)

from tidevice.__main__ import main, _udid2device
from tidevice._usbmux import Usbmux

if __name__ == "__main__":
    main()