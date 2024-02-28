import os
import re

def change_name(files, path):
    print("Files in the current directory:", files)
    for file in files:

        new_name = ''
        # print('\n old name: ', file)

        if file.startswith('noun') and file.endswith('.svg'):
            new_name = re.findall((r'\w+-(\w+)-'), file)[0]
            print('renaming: ', file, ' to ', new_name + 'Icon.svg')
            os.rename(path + '/' + file, path + '/' + new_name + 'Icon.svg')
            # print(file)


def edit_svg(file, path):
    with open(path + '/' + file, 'r') as f:
        text = f.read()
        # print('\n TEXT: \n', text)

        namespace_matches = re.findall(r'(:\w)\w+=', text)
        # print('\n NAMESPACE_MATCH: \n', namespace_matches)

        text_matches = re.findall(r'<text.*</text>', text)

        if len(text_matches) == 0 and len(namespace_matches) == 0:
            return None

        for match in namespace_matches:
            text = text.replace(match, match[1].upper())
        
        for match in text_matches:
            text = text.replace(match, '')

        # print(text)
    with open(path + '/' + file, 'w') as f:
        print('writing ' + str(len(text_matches) + len(namespace_matches)) + ' changes to ' + file)
        f.write(text)

if __name__ == "__main__":
    path = '/Users/sandraconnors/Desktop/React-Comm-Board/react-comm-board/src/images/'
    # file = 'noun-doing-5859459 (1).svg'
    files = os.listdir(path)
    # print(files)

    for file in files:
        if file.endswith('.svg'):
            edit_svg(file, path)
            # break

    # edit_svg(file, path)

    # change_name(files, path)