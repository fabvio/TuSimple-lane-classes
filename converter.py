import os
import json

from argparse import ArgumentParser as ArgParse

# Method to obtain json files with class information
def main(label):

	output_path = label + '_withclasses.json'
	out = open(output_path, 'w')
	with open(label + '.json') as json_file, open(label + '_classes.txt') as txt:
		for line_json, line_classes in zip(json_file, txt):
			line_json = line_json.strip()
			line_classes = line_classes.strip()
			j_content = json.loads(line_json)
			j_content['classes'] = line_classes

			string = json.dumps(j_content)
			string += '\n'
			out.write(string)


if __name__ == '__main__':
	ap = ArgParse()
	ap.add_argument('--root', type=str, default='.')
	args = ap.parse_args()

	main(os.path.join(args.root, "label_data_0313"))
	main(os.path.join(args.root, "label_data_0531"))
	main(os.path.join(args.root, "label_data_0601"))
