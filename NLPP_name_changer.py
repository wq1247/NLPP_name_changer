import os,sys
from struct import unpack, pack

root=os.getcwd()

def name_unpack(file):
    file_path=data_path+file
    save_file=open(file_path,'rb')
    #print(txt_path)
    save_file.read(4)
    名前b=b''
    苗字b=b''
    for i in range(12):
        b=save_file.read(1)
        flag=unpack('B',b)[0]
        if flag == 0:
            break
        else:
            名前b+=b
    save_file.seek(20)
    for i in range(12):
        b=save_file.read(1)
        flag=unpack('B',b)[0]
        if flag == 0:
            break
        else:
            苗字b+=b
    #print(苗字b,名前b)
    save_file.close()
    return(苗字b.decode('utf-8'),名前b.decode('utf-8'))
    
def name_pack(file):
    clib=open("char1_2.txt",'r',encoding="utf-8")
    clib=clib.readline()
    苗字,名前=input().split(" ")
    for w in 苗字:
        try:
            clib.index(w)
        except:
            print("你所使用的字符“"+w+"”不在字库中，请修改后重试")
            sys.exit()
    for w in 名前:
        try:
            clib.index(w)
        except:
            print("你所使用的字符“"+w+"”不在字库中，请修改后重试")
            sys.exit()
    苗字b,名前b=苗字.encode('utf-8'),名前.encode('utf-8')
    if len(苗字b) > 12:
        print("姓超长，请重试")
        sys.exit()
    if len(名前b) > 12:
        print("名超长，请重试")
        sys.exit()
    while len(苗字b) < 12:
        苗字b+=pack("B",0)
    while len(名前b) < 12:
        名前b+=pack("B",0)
    
    new_path=root+"/"+file
    new_file=open(new_path,'wb')
    file_path=data_path+file
    save_file=open(file_path,'rb')
    data=save_file.read(4)
    save_file.seek(16)
    data+=名前b+save_file.read(4)+苗字b
    save_file.read(12)
    data+=save_file.read(166)
    save_file.close()
    new_file.write(data)
    new_file.close()

def find_file():
    file_list=os.listdir(root)
    for file in file_list:
        if file=="00000001":
            return(file)
            break
        try:
            file.index("-")
            return(file)
            break
        except:
            continue
        
def main_():
    苗字1,名前1=name_unpack("savedata8")
    苗字2,名前2=name_unpack("savedata33")
    苗字3,名前3=name_unpack("savedata58")
    print("你现有的存档名称分别为：")
    print("存档1：",苗字1,名前1)
    print("存档2：",苗字2,名前2)
    print("存档3：",苗字3,名前3)
    print("请输入你想修改的存档编号：(1/2/3)")
    num=input()
    if num != "1":
        if num != "2":
            if num !="3":
                print("输入信息错误，请重试")
                sys.exit()
    print("请输入你要修改的名字：（姓 名，中间使用空格隔开，姓和名的长度均不得超过12字节）")
    try:
        name_pack("savedata"+str((int(num)-1)*25+8))
        print("修改成功")
    except:
        print("修改失败，请检查你输入的字符")

data_path=root+"/"+find_file()+"/"
main_()
print("按回车键退出")
input()
    
    
