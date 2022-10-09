from PIL import Image
import os

tree = list(os.walk('input'))
treeDel= list(os.walk('output'))

per1=input("Width: ")
per2=input("Height: ")

# отчиска перед редоктированием
# clean up before editing
if len(treeDel)!=1:
    for i in range(len(treeDel[0][1])):
        treeDelPak=list(os.walk(f'output\{treeDel[0][1][i]}'))
        for i in range(len(treeDelPak)):
            for x in range(len(treeDelPak[i][2])):
                if len(treeDelPak[i][2]) != 0:
                    os.remove(f'{treeDelPak[i][0]}\{treeDelPak[i][2][x]}')
        for i in range(len(treeDelPak)):
            os.rmdir(f'{treeDelPak[len(treeDelPak)-i-1][0]}')
    print('Delete complite')
else:
    print('В папке всё удалено')

if len(tree)!=1:
    for i in range(len(tree)-1):
        os.mkdir(f'output\{(tree[i+1][0])[6:]}')
    for i in range(len(tree)):
        for x in range(len(tree[i][2])):
            if len(tree[i][2]) != 0 and i!=0 and tree[i][2][x] == 'Thumbs.db':
                if x !=0:
                    tree[i][2].pop(x)
                else:
                    tree[i][2].pop(x)
                    break
        for x in tree[i][2]:
            img = Image.open(tree[i][0]+'\\'+x)
                            #|        |ширина, высота\width height
            img = img.resize((int(per1),int(per2)),Image.ANTIALIAS)
            img.save(f'output\{(tree[i][0])[6:]}\{x}')
    print('complet')
else:
    print('В папке input отцутвуют даные для обработки')
