import yaml
import pandas
from setting import DIR_NAME


def read_yaml(filename):


	with open(filename,'r',encoding='utf-8') as f:
		# 读取yml文件
		content =yaml.load(f,Loader=yaml.FullLoader)
		return content


if __name__ == '__main__':
	print(read_yaml('/data/Case.yaml'))

