import re


COMMENTS_REGEX = r'^\s*(\/|\/\/|\/\*|\*|.*\/\/.*)'
POINTER_REGEX = r'\s*\*.*;$'
INVALID_REGEX_1 = r'(.*\/ )'
INVALID_REGEX_2 = r'^([\s\S]*?)\*/'

def comment_sticher(cmnt_lst: list):
    cmnt_dict = {}
    new_comment = ''
    for cmnt in cmnt_lst:
        count, comment = int(cmnt.split('::')[0]), cmnt.split('::')[1]
        if count < 100:
            new_comment += f'{comment} '
            if '/*' in new_comment and '*/' in new_comment or ' */ ' == new_comment :
                cmnt_dict[count] = new_comment
                new_comment = ''
        else:
            cmnt_dict[count] = comment
    return cmnt_dict


def second_try(cmnt_lst: list):
    cmnt_dict = {}
    dumb_dict = {}
    comment_list = [_.split('::') for _  in cmnt_lst]
    new_comment = ''
    counter = 0
    for count, cmnt in comment_list:
        count = int(count)
        counter_tuple = (count-1, count, count+1, count+2)
        if counter in counter_tuple:
            print(counter_tuple)
            new_comment += f'{cmnt} '
            if '/*' in new_comment and '*/' in new_comment or ' */ ' == new_comment:
                cmnt_dict[count] = new_comment
                new_comment = ''
                counter = count

        # if '/*' in new_comment and '*/' in new_comment or ' */ ' == new_comment :
        #     cmnt_dict[count] = new_comment
        #     new_comment = ''
        # else:
        #     dumb_dict[count] = new_comment

    print(cmnt_dict)
    print(dumb_dict)


if __name__ == '__main__':
    with open('cycle.c') as f:
        data = f.readlines()
    output_list = []
    comment_list = []
    for count, line in enumerate(data):
        count += 1
        match = re.search(COMMENTS_REGEX, line)
        if match:
            if re.match(POINTER_REGEX, line):
                new_line = line
            elif r'//' in line:
                new_line = line.split('//')[0]
                comment = '//' + line.split("//")[-1]
                # print(f'Comment line: {count}, between: ({len(new_line)}, {len(comment)}), Comment as: // {comment}')
            else:
                new_line = '\n'
                # print(f'Comment line: {count}, between: {match.span()}, Comment as: {line}')
                if '/*' in line and '*/' in line:
                    pass
                else:
                    if re.search(INVALID_REGEX_1, line):
                        print(f"INVALID_COMMENT AT {count+1} =", line)
                    else:
                        line = line.replace('\n','').replace('    ', '')
                        # comment_list.append(f"{line}::{count}")
                        comment_list.append(f"{count}::{line}")
        else:
            new_line = line
        output_list.append(new_line)

    cmnts = comment_sticher(comment_list)
    for k,v in cmnts.items():
        if str.startswith(v,'/*') and str.endswith(v,'*/ '):
            pass
        else:
            print(f'INVALID COMMENT AT {k} = {v}')

    # new_comment = ''
    # for _ in comment_list:
    #     count, comment = _.split('::')[0], _.split('::')[1]
    #     new_comment += f'{comment} '
    #     match = re.search(INVALID_REGEX_2, new_comment)
    #     if '/*' in new_comment and '*/' in new_comment:
    #         # print(match.group())
    #         new_comment = ''
    #     elif '/*' in new_comment and match:
    #         pass
    #     else:
    #         print(f'INVALID COMMENT AT {count}', comment)


    # with open('output.c', 'a+') as opt_fl:
    #     opt_fl.writelines(output_list)

    # val = ''.join(comment_list).split('/*')
    # for _ in val:
    #     count, _ = _.split('::')[-1], _.split('::')[0]
    #     if '*/' not in _:
    #             print(f"INVALID_COMMENT AT PiKA {count}", '/* '+_)
    #     else:
    #         print(re.search(INVALID_REGEX_2, _).group())
            # if re.sub(INVALID_REGEX_2, "", _) not in ('    '):
            #     print('INVALID COMMENT', re.sub(INVALID_REGEX_2, '', _))
