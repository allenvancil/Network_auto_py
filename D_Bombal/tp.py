
## file for comparing differences in two txt docs
file1 = 'iosv_l2_cisco_design'
file2 = 'ios_I2_cisco_design_2'
import difflib

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()
# compares txt docs for difference
        for line1 in file1_lines:
            if line1 in file2_lines:
                pass
            else:
                print(file1_lines.index(line1))
                print(f"\nThis line = \n{line1} \nfrom file1 is not in file2\n")

compare_files(file1, file2)