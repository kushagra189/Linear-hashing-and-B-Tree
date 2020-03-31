import sys
i, p, S, b, b_new, bucket_count, total_block_count = 0, 0, 0, 2, 4, 2, 2
linHash, block_count, output_buffer = {}, {}, []

block_count[0] = 1
block_count[1] = 1

filename = sys.argv[1]
M = max(4,int(sys.argv[2]))
B = max(2,int(sys.argv[3]))

def insertion (num):
	global S, total_block_count, output_buffer

	hash_val = num%b
	if hash_val < p:
		hash_val = num%b_new
	if hash_val not in linHash:
		linHash[hash_val] = [[]]

	flag = 0
	for i in range(block_count[hash_val]):
		if num in linHash[hash_val][i]:
			flag = 1

	if flag == 0:
		S = S + 1
		temp = block_count[hash_val] - 1
		if len(linHash[hash_val][temp]) >= (B * 0.25):
			total_block_count, temp, block_count[hash_val], l = total_block_count+1, temp+1, block_count[hash_val]+1, []
			linHash[hash_val].append(l)

		linHash[hash_val][temp].append(num)
		output_buffer.append(num)

		if len(output_buffer) >= ((B * 1.0) / 4.0):
			for val in output_buffer:
				print(str(val))
			output_buffer = []

	if hash_table_too_full():
		create_new_bucket()

def hash_table_too_full():
	return 1 if (( S * 400.0 ) / (B * total_block_count)) > 75.0 else 0

def create_new_bucket():
	global bucket_count, p, b, b_new, total_block_count

	bucket_count += 1
	replace_array = [value for i in range(block_count[p]) for value in linHash[p][i]]

	total_block_count = total_block_count - block_count[p]

	linHash[p] = [[]]
	block_count[p], total_block_count = 1, total_block_count+1

	linHash[bucket_count - 1] = [[]]
	block_count[bucket_count - 1], total_block_count = 1, total_block_count+1

	for value in replace_array:
		hash_val = value % b_new

		if hash_val not in linHash:
			linHash[hash_val] = [[]]
			block_count[hash_val], total_block_count = 1, total_block_count+1

		flag = 0
		for j in range(block_count[hash_val]):
			flag = 1 if value in linHash[hash_val][j] else 0

		if flag == 0:
			temp = block_count[hash_val] - 1
			if len(linHash[hash_val][temp]) >= (B * 0.25):
				temp, block_count[hash_val], total_block_count, l = temp+1, block_count[hash_val]+1, total_block_count+1, []
				linHash[hash_val].append(l)
			linHash[hash_val][temp].append(value)
	p = p + 1

	if bucket_count == b_new:
		b, p = b*2, 0
		b_new = 2*b
	return 1

input_buffer, measure = [], (((M-1) * B * 1.0) / 4.0)
fh = open(filename)
for line in fh:
	input_buffer.append(int(line.strip()))
	if len(input_buffer) >= measure:
		for val in input_buffer:
			insertion(val)
		input_buffer = []

for val in input_buffer:
	insertion(val)
input_buffer = []
fh.close()

for val in output_buffer:
	print(str(val))
output_buffer = []