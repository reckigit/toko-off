import os,sys
from menusdict import *



# unicode strings
vellipsis = '⋮' 
right ='👉' 


# format strings
pemakai = f"{Huruf.merahterang}{os.getlogin()}{Huruf.netral}"
aplikasi = f"{Huruf.hijauterang}toko-off{Huruf.netral}"
file = f"{Huruf.kuningterang}{(sys.argv[0]).rsplit('.', 1)[0]}{Huruf.netral}/"
menuaktif=""


def header():

    os.system('clear')

    # res.1366x768 fscr w:150 -- 
    print("="*150)
    print(vellipsis*2 + " dari RECKI©".ljust(15),"H O M E".center(120),\
    (Huruf.bergarisbawah + "Q" + Huruf.netral + "uit" + vellipsis*2).rjust(18))
    print("="*150)


def main_menu():

    print("~"*150)
    print(f"{vellipsis} {matas['i']} {vellipsis} {matas['p']} {vellipsis} {matas['o']}{vellipsis}")
    print("~"*150)


def cmd_prompt():

    lokasi = "{}@{} {}{}👉 "
    matas_opsi = input(lokasi.format(pemakai,aplikasi,file,menuaktif))


    if (matas_opsi.lower() == 'q') or (matas_opsi.lower() == 'quit'):
        exit()

    elif (matas_opsi.lower() == 'i') or (matas_opsi.lower() == 'input'):

        input_menu()
        
    elif (matas_opsi.lower() == 'p') or (matas_opsi.lower() == 'proses'):
        proses_menu()

    elif (matas_opsi.lower() == 'o') or (matas_opsi.lower() == 'output'):
        output_menu()

    elif (matas_opsi.lower() == 'h') or (matas_opsi.lower() == 'home'):

        home_()

    else:
        pesankeliru()


def home_():

    header()
    main_menu()

    global menuaktif
    menuaktif = ""

    cmd_prompt()


def input_menu():

    header()
    main_menu()

    for key in minput:
        print(vellipsis.ljust(1),minput[key],vellipsis.rjust(33 - len(minput[key])))
        
    print("".rjust(0),"`"*19)

    global menuaktif
    menuaktif = f"{Huruf.kuningterang}input/{Huruf.netral}"

    cmd_prompt()


def proses_menu():

    header()
    main_menu()
    
    for key in mproses:
        print(vellipsis.rjust(9),mproses[key],vellipsis.rjust(33 - len(mproses[key])))
        
    print("".rjust(8),"`"*19)

    global menuaktif
    menuaktif = f"{Huruf.kuningterang}proses/{Huruf.netral}"

    cmd_prompt()


def output_menu():

    header()
    main_menu()
    
    for key in moutput:
        print(vellipsis.rjust(18),moutput[key],vellipsis.rjust(33 - len(moutput[key])))
        
    print("".rjust(17),"`"*19)

    global menuaktif
    menuaktif = f"{Huruf.kuningterang}output/{Huruf.netral}"

    cmd_prompt()


def pesankeliru():

    header()
    main_menu()

    pesan = "{}Perintah tidak dikenali{}"
    print(pesan.format(Huruf.merahterang,Huruf.netral))

    global menuaktif
    menuaktif = ""

    cmd_prompt()


    

header()
main_menu()
cmd_prompt()






