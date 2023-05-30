from re import search



# Store input data
input_file = open('cycle.c')
input_data = input_file.readlines()
input_file.close()

# dict of comments
second_check = {}

# Read data, find comments and write the code
output_file = open('pen_di.c', 'a+')
for count, line in enumerate(input_data):
    if search(r'^\s*(\/|\/\/|\/\*|\*|.*\/\/.*)', line):
        if search(r'\s*\*.*;$', line):
            code = line
        elif r'//' in line:
            code, comment = line.split('//')[0], line.split("//")[-1]
            # print("line number:"+str(count)+", comment found: "+str(comment))
        else:
            code = '\n'
            # print("line number:"+str(count)+", comment found: "+line)
            if '/*' in line and '*/' in line:
                # Bypassing because found a valid comment
                pass
            else:
                if search(r'(.*\/ )', line):
                    print(f"INVALID_COMMENT AT {count+1}", line)
                else:
                    second_check[count+1] = line.lstrip('    ').replace('\n','')
    else:
        code = line
    output_file.write(code)

comment_holder = ''
com_dict = {}
for line_number, line in second_check.items():
    if line_number < 100:
        comment_holder += line+' '
        if '/*' in comment_holder and '*/' in comment_holder or '*/' == line:
            com_dict[line_number] = comment_holder
            comment_holder =''
    else:
        com_dict[line_number] = line
    
for ln_num, line in com_dict.items():
    if '/*' in line and '*/' in line:
        pass
    else:
        print('INVALID COMMENT AT ' + str(ln_num) + ' '+ line)

output_file.close()
