import argparse

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
#type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('--integers', type=int, nargs='+', default=0, help='传入的数字')
parser.add_argument('--name', type=str, help='传入的名字')

args = parser.parse_args()

#获得传入的参数
print(args.integers)
print(args.name)