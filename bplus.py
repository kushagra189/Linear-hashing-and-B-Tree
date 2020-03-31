from classes import Node, BPlusTree
import bisect
import sys
import os

output_buffer = []

def perform(cmnd):
	global output_buffer
	dem = ["INSERT", "FIND", "COUNT", "RANGE"]
	if cmnd[0] == dem[0]:
		tree.insert_routine(int(cmnd[1]))

	elif cmnd[0] == dem[1]:
		res = tree.count_query(int(cmnd[1]))
		temp = "NO" if res == 0 else "YES"
		output_buffer.append(temp)

	elif cmnd[0] == dem[2]:
		output_buffer.append(str(tree.count_query(int(cmnd[1]))))

	elif cmnd[0] == dem[3]:
		output_buffer.append(str(tree.range_query(int(cmnd[1]), int(cmnd[2]))))

	if len(output_buffer) >= ((B * 1.0) / 10.0):
		for res in output_buffer:
			print(res)
		output_buffer = []


if __name__ == "__main__":
	M = int(sys.argv[2])
	B = int(sys.argv[3])

	if not os.path.isfile(sys.argv[1]):
		print("Invalid File")
		sys.exit()

	input_buffer = []

	pointer_count = max(2, (((B - 8) / 12) + 1))
	M, B = max(2,M), max(B,20)

	tree = BPlusTree(pointer_count)

	with open(sys.argv[1]) as fh:
		for line in fh:
			cmnd = line.strip().split()
			input_buffer.append(cmnd)
			val = (((M-1) * B * 1.0) / 10.0)
			if len(input_buffer) >= val :
				for cmnd in input_buffer:
					perform(cmnd)
				input_buffer = []

	for cmnd in input_buffer:
		perform(cmnd)
	input_buffer = []
	fh.close()

	for res in output_buffer:
		print(res)
	output_buffer = []