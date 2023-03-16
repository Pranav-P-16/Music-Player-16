from PySimpleGUI import *
import pygame,random,pickle
from subprocess import call
import scipy,os
from pydub import AudioSegment
musics=[]
vis_el=False
for root,dirs,file in os.walk("/home/user/Desktop"):
    for i in file:
        if i[-3:] in "wav":
            msc=os.path.join(root,i)
            if msc[11]!=".":
                yu=msc.split("/")
                if yu[3]!="Recovered Files SD Card":
                    musics.append(msc)
favourite=False
repeat=False
m_c=0
mn=""
l=[]
try:
    f1=open("Data/maindata.dat","rb")
except:
    f1=open("Data/maindata.dat","wb")
    f1.close()
    f1=open("Data/maindata.dat","rb")
while True:
    try:
        k=pickle.load(f1)
        l.append(k)
    except:
        break
f1.close()
def fv():
    global l,m_c
    otc=False
    t=[]
    l2=[]
    if l==[]:
        t.append([Text("No Favourites Found",key="1",background_color="black",font=("Chilanka",25))])
    else:
        l.sort()
        for i in range(len(l)):
            name=""
            for j in l[i][::-1]:
                if j=="/":
                    break
                name+=j
            name=name[::-1]
            name=name.rstrip(".wav")
            l2.append(name)
            t.append([Button(name,key=str(l[i]),mouseover_colors=("yellow","black"),button_color=("white","black"),font=("Chilanka",25))]+[Button("",mouseover_colors=("black","black"),image_filename="Assets/delete.png",key="delx5"+str(l[i]),button_color=("black","black"))])
    column=[*t]
    k=False
    for i in l2:
        if len(i)>=21:
            k=True
    if k==True:
        otc=True
    else:
        otc=False
    if otc==True:
        t=False
    else:
        True
    theme("black")
    layout=[[Image(filename="Assets/fav_list.png")]+[Text("      ")]+[Text("Favourites",font=("Pricedown",30))]+[Text("       ")]+[Image(filename="Assets/fav_list.png")],[Text("\n")],[Column(column,size=(450,400),background_color="black",scrollable=True,vertical_scroll_only=t, key = "Column")],
            [Button("",image_filename="Assets/clear.png",key="clr",button_color=("black","black"),border_width=0)]+[Text("      ")]+[Button("",image_filename="Assets/return.png",key="re",button_color=("black","black"),border_width=0)]]
    window2 = Window('Favourites', layout,element_justification="c").Finalize()
    window2.TKroot.focus_force()
    while True:
        e,v=window2.read()
        if e==None or e=="re":
            window2.close()
            break
        elif e=="clr":
            l.clear()
            window2.close()
            fv()
            break
        elif "delx5" in e:
            e2=e.lstrip("delx5")
            l.remove(e2)
            window2.Element(e2).Update(visible=False)
            window2.Element(e).Update(visible=False)
        else:
            window2.close()
            if sh==True:
                for i in musics:
                    if e in i:
                        m_c=musics.index(i)
                        forward(None)
                        image_ch("r")
            else:
                for i in m_copy:
                    if e in i:
                        m_c=m_copy.index(i)
                        forward(None)
                        image_ch("r")
    return 1
def fv3():
    global musics,m_c
    t=[]
    l2=[]
    otc=False
    musics.sort()
    if musics==[]:
        t.append([Text("No Musics Found",key="1",background_color="black",font=("Chilanka",25))])
    else:
        for i in musics:
            i=i.split("/")
            i=i[-1]
            i=i.split(".")
            i=i[0]
            l2.append(i)
            t.append([Button(i,key=str(i),mouseover_colors=("yellow","black"),button_color=("white","black"),font=("Chilanka",25))])
    column = [*t]
    k=False
    for i in l2:
        if len(i)>=25:
            k=True
    if k==True:
        otc=True
    else:
        otc=False
    if otc==True:
        t=False
    else:
        True
    theme("black")
    layout=[[Image(filename="Assets/music.png")]+[Text("         ")]+[Text("All Songs",font=("Pricedown",30))]+[Text("          ")]+[Image(filename="Assets/music.png")],
            [Text("\n")],[Column(column,size=(450,400),background_color="black",scrollable=True,vertical_scroll_only=t, key = "Column")],
        [Button("",image_filename="Assets/return.png",key="re",button_color=("black","black"),border_width=0)]]
    window5 = Window('All Songs',layout,size=(480,580),element_justification="c",resizable=True).Finalize() 
    window5.TKroot.focus_force()
    while True:
        e,v=window5.read()
        if e==None or e=="re":
            window5.close()
            break
        else:
            window5.close()
            if sh==True:
                for i in musics:
                    if e in i:
                        m_c=musics.index(i)
                        forward(None)
                        image_ch("r")
            elif sh==False:
                for i in m_copy:
                    if e in i:
                        m_c=m_copy.index(i)
                        forward(None)
                        image_ch("r")
    return 1
def shortcut_keys():
    theme("black")
    layout=[[Image(filename="Assets/info.png")]+[Text("      ")]+[Text("Shortcut Keys",font=("Pricedown",30))]+[Text("       ")]+[Image(filename="Assets/info.png")],
        [Text("\n")],[Text("SPACE BAR -> For Pause/Play\nLEFT/RIGHT ARROW -> For playing\nnext/previous song\nUP/DOWN ARROW -> For controlling\nsound level\nS -> Shuffle\nR -> Repeat\nF -> Set song as favourite\nI -> Show Info Panel\nL -> Show favourites list\nG -> Play random GIF\nA -> Show all songs\nM -> Mute Audio\nE -> Expand Main Window\nO -> Toggle GIF On/Off",font=("Chilanka",20))],
            [Text("\n")],
            [Button("",image_filename="Assets/return.png",key="re",button_color=("black","black"),border_width=0)]]
    window3 = Window('Shortcut Keys', layout,element_justification="c").Finalize()
    window3.TKroot.focus_force()
    e,v=window3.read()
    if e==None or e=="re":
        window3.close()
def faq():
    theme("black")
    layout=[[Image(filename="Assets/info.png")]+[Text("      ")]+[Text("FAQ",font=("Pricedown",30))]+[Text("       ")]+[Image(filename="Assets/info.png")],
        [Text("\n")],[Text("? GIF's are not showing / lagging too much\nA : It Depends on your system configurations\n\n? Favourite songs list being reset\nA : Check your System permissions for drives\n\n? All Songs are not getting displayed\nA : Initially built for .wav music files",font=("Chilanka",15))],
            [Text("\n")],
            [Button("",image_filename="Assets/return.png",key="re",button_color=("black","black"),border_width=0)]]
    window3 = Window('FAQ', layout,element_justification="c").Finalize()
    window3.TKroot.focus_force()
    e,v=window3.read()
    if e==None or e=="re":
        window3.close()
def about():
    theme("DarkBrown2")
    layout=[[Image(filename="Assets/info.png")]+[Text("      ")]+[Text("ABOUT",font=("Pricedown",30),text_color="red")]+[Text("       ")]+[Image(filename="Assets/info.png")],
        [Text("\n")],[Text("Created and Compiled",font=("Chilanka",15))],[Text("By",font=("Chilanka",15))],[Text("PR @ 16 Creations",text_color="yellow",font=("Diploma",25))],
            [Text("\n")],
            [Button("",image_filename="Assets/home.png",key="re",button_color=("brown4","brown4"),border_width=0)]]
    window3 = Window('About', layout,element_justification="c").Finalize()
    window3.TKroot.focus_force()
    e,v=window3.read()
    if e=="re":
        window3.close()
        return 3
    else:
        window3.close()
        return None
def fv2():
    theme("black")
    layout=[[Image(filename="Assets/info.png")]+[Text("      ")]+[Text("Info",font=("Pricedown",30))]+[Text("       ")]+[Image(filename="Assets/info.png")],
        [Text("\n")],[Button("Shortcut Keys",size=(30,1),button_color="yellow")],[Button("FAQ",size=(30,1),button_color="green2")],[Button("About",size=(30,1),button_color="orange")],[Text("\n")],
            [Button("",image_filename="Assets/return.png",key="re",button_color=("black","black"),border_width=0)]]
    window2 = Window('Info', layout,element_justification="c").Finalize()
    window2.TKroot.focus_force()
    while True:
        e,v=window2.read()
        if e==None or e=="re":
            window2.close()
            break
        elif e=="Shortcut Keys":
            window2.Hide()
            shortcut_keys()
            window2.UnHide()
        elif e=="FAQ":
            window2.Hide()
            faq()
            window2.UnHide()
        else:
            window2.Hide()
            res=about()
            if res==None:
                window2.UnHide()
            else:
                window2.close()
    return 1
images=['Animations/spin1.gif', 'Animations/spin2.gif', 'Animations/spin3.gif', 'Animations/spin4.gif', 'Animations/spin5.gif', 'Animations/spin6.gif',
        'Animations/spin7.gif', 'Animations/spin8.gif', 'Animations/spin9.gif', 'Animations/spin10.gif', 'Animations/spin11.gif', 'Animations/spin12.gif',
        'Animations/spin13.gif', 'Animations/spin14.gif', 'Animations/spin15.gif', 'Animations/spin16.gif', 'Animations/spin17.gif', 'Animations/spin18.gif',
        'Animations/spin19.gif', 'Animations/spin20.gif', 'Animations/spin21.gif', 'Animations/spin22.gif', 'Animations/spin23.gif',
        'Animations/spin24.gif', 'Animations/spin25.gif', 'Animations/spin26.gif', 'Animations/spin27.gif', 'Animations/spin28.gif',
        'Animations/spin29.gif', 'Animations/spin30.gif', 'Animations/spin31.gif', 'Animations/spin32.gif', 'Animations/spin33.gif',
        'Animations/spin34.gif', 'Animations/spin35.gif', 'Animations/spin36.gif', 'Animations/spin37.gif', 'Animations/spin38.gif',
        'Animations/spin39.gif', 'Animations/spin40.gif', 'Animations/spin41.gif', 'Animations/spin42.gif', 'Animations/spin43.gif',
        'Animations/spin44.gif', 'Animations/spin45.gif', 'Animations/spin46.gif', 'Animations/spin47.gif', 'Animations/spin48.gif',
        'Animations/spin49.gif', 'Animations/spin50.gif']
c_g=0
m_copy=musics.copy()
#random.shuffle(images)
def image_ch(p="o"):
    global c_g,tl
    if tl==False:
        if p=="f":
            if c_g+1==len(images):
                c_g=0
            else:
                c_g+=1
        elif p=="o":
            c_g=0
        elif p=="r":
            c_g=random.randint(1,len(images))
            window.find_element("Prog_bar").Update(filename=images[c_g])
        else:
            if c_g-1<0:
                c_g=len(images)-1
            else:
                c_g-=1
    else:
        pass
def music():
    global m_c,c_g,sh,song,t,tm,mn
    mn=""
    if m_c==len(musics)-1:
        m_c=0
    if sh==True:
        pygame.mixer.music.load(musics[m_c])
        for i in musics[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(musics[m_c])
    else:
        pygame.mixer.music.load(m_copy[m_c])
        for i in m_copy[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(m_copy[m_c])
    audio = AudioSegment.from_file(song)
    t=int(audio.duration_seconds)
    window.find_element("sl").Update(range=(0,t))
    tm=0
    mn=mn[::-1]
    window.find_element("mname").Update(mn.rstrip(".wav"))
    pygame.mixer.music.play()
    image_ch()
    new_fav()
def forward(rpt=False):
    global m_c,c_g,sh,song,t,tm,mn
    mn=""
    if rpt==False:
        if m_c+1!=len(musics):
            m_c+=1
        else:
            m_c=0
    elif rpt==None:
        m_c=m_c
    else:
        m_c=m_c
    if sh==True:
        pygame.mixer.music.load(musics[m_c])
        for i in musics[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(musics[m_c])
    else:
        pygame.mixer.music.load(m_copy[m_c])
        for i in m_copy[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(m_copy[m_c])
    audio = AudioSegment.from_file(song)
    t=int(audio.duration_seconds)
    window.find_element("sl").Update(range=(0,t))
    tm=0
    mn=mn[::-1]
    window.find_element("mname").Update(mn.rstrip(".wav"))
    pygame.mixer.music.play()
    if pause==True:
        pygame.mixer.music.pause()
    if rpt==False:
        image_ch("f")
        if tl==False:
            window.find_element("Prog_bar").Update(images[c_g])
    if repeat==False:
        new_fav()
def backward():
    global m_c,c_g,song,sh,t,tm,mn
    mn=""
    if m_c-1>=0:
        m_c-=1
    else:
        m_c=len(musics)-1
    if sh==True:
        pygame.mixer.music.load(musics[m_c])
        for i in musics[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(musics[m_c])
    else:
        pygame.mixer.music.load(m_copy[m_c])
        for i in m_copy[m_c][::-1]:
            if i=="/":
                break
            mn+=i
        song=(m_copy[m_c])
    audio = AudioSegment.from_file(song)
    t=int(audio.duration_seconds)
    window.find_element("sl").Update(range=(0,t))
    tm=0
    mn=mn[::-1]
    window.find_element("mname").Update(mn.rstrip(".wav"))
    pygame.mixer.music.play()
    if pause==True:
        pygame.mixer.music.pause()
    image_ch("b")
    if tl==False:
        window.find_element("Prog_bar").Update(images[c_g])
    new_fav()
def sound():
    global music_playing,pause
    if music_playing==True:
        pygame.mixer.music.pause()
        music_playing=False
        pause=True
    else:
        pygame.mixer.music.unpause()
        music_playing=True
        pause=False
fav0=b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAAB3RJTUUH5QodCRMm3q1IkgAADiBJREFUaN7VmnuQ3lV5xz/POb/be999c9kEEiLhYoQGRREVMVw0yqWxaIFSNcyoiNWpQ5224jjDaBlH6Gg7ba06AwMFqwxQi6A0UURAmkC4aORiDLcQCLdNwu677+33+72/3zmnf+yF3exusouhnT4z78zOu+fy/T6Xc57nOa/wBkj7c5/EZSnih7hWC/PSi6A1esWbkDBCggipVChefsVB21MOxiKdSz5Let8m9MBSXJrg8hyXprTv20r9M+u9fMczGq3xjvmjvP2v3zPhu98Ofoj4HhJFuHYbf9VbKH332v8bIiPnfRhVq2F2PYeLY1R/f+ji+HBl7XEKjsK5FSKy0BlTQQTRasRZt8eJ7LCw3Sn9mOrv32UGXzESRdQ23kP74+dSueE//3eINC84h7033kr9g2swO59Brzxyucrztcq5P8mtPaFt7MCe3Og9xjBiLF1rUQhFJfRrxSJPs9DTWVGpF7RS91mlbrOed49tDO9RtX5sYxjvmNVUr/3BG0Nk+OzTkSwD7eGaI0ilskzl+YVYu34oy4/eGqdqS5zyeNLjhSynZSw953Bj85VAKEJNKVYEPqujgPcUQ1ZHYVb19CNO6Wts4P+H63ZfVdUamJzaf911cImMnHMmdmgvEoYQFQKJux8Vay8dzLK3/aIV85Nmh+1pRmzdBOiZNnDjnzF2FS0cF4V8tFpiTblg+z19r9H6G/rNq+40Tz/lyHMkCKhtuPsPJ9L+1MdINt2Ld9gK8LzFKssuS3Lz6V+2u4Vrh1tsS3rkgJ6PeScRsw5CJbyzEHJRvcK7itGwp/U/2ij6J/K87dKU4OhVlK66/vUTaa4/n+Tnt+OvOhaJCkeoPPv2YJad+b1Xm9w60qHj3OsiMJMYB3VPsb6vwoX9FVv19HU2jC51abKXPEevPo7qd66ZP5HhM0/BNRpIVEB8f5Uy+dVPx+nJX9/d4P5uMneTztNCCji7WuRvF/UxEAQ/Mp73l5KbQQT67tw84zy1v0Uly1HVGhIVlmljvvtknJ78lVeG2NxNkDeAxLhiHPCTZpfLB4d5Je2dq/P8WxQLVfyAxpmnzY9I46zTQXugvZJKkyt2pb3TLh8cZmvcO2iutK+4SX8r4BftmG/uadDIso+rbvdLDCxWeB4j562bNndGTO315+GMwe54ElUsfa5tzF9fuXtY3d1J0DIzgMmfcc0eSCxgnUOJEIgQKcE6MGPzBXiqlyGIvLMQHK87nd+7dmt7vPEe/mEGS063xhlrcFmOiHobJv/p94eay765p4HZF4gDT2CRp+nTCgd0rWPIGNrWzep+dkzjK3yP4wshKwIPXwQHJNayuZvw27g3oaSyEq5YsoAPVktbbRCuw9kXpVCkduvPJtb09t0k/8bXaG++FykUfd0cuWRb0lt23XCLjNf80I0BXF0IWFOKCEQYMhbjHEWlKCphZy/nrnZM09op/muBQ33NOdUSSz2PJ9Iev2rHvJwbUudY5GnWlgvpob6nNzS7HkDTOq4aanJcFBy/RKlPx1s2X15Y95H9W6TxoTW4LENpfXKWZT+9fHCo76aRzoQPOsAX+Gi1zBGhx8ZWl98nGcnYDaeABVrzgUqBZb7H9cMtBnODGiNxfBSwvr/Clm7Cz1sxDWNBXlOSdVDWYj9br7Klm6r7usnE/764sMbFC2o7XBB+CGeflnKZ2i0bJ/adyiwI0EsPUcqaC7cnvb5ftuMpgxRwQa3MisDjO3ub/LrbI3WvuZED9hjDDY0225Ie6/vKhCIY4NhwlMSNjTY3jXRoWouW0UAdn68F2tapDa2uOrUUURCZsORtzS4vZflKnWfn2pEGul6fgmtCmuf9MS5JsHt2H2GsO2Njq8teYyfMZhycUAg5Ngq4eqhJYwzINGWMfe5ox2gR3luMWKgVn6xXuGWkwwPddAL8TKKBZ3s5ngiH+Hoipp7tZdzbicG5j6j+en/+wgu4DRumE8l2PIPr9dDGnLonz5dtGrsvxsUX+FClyB3tmL253e8lJEBqHT9tdjitHPHJ/gpPphmbuzOffPtK5hyJc9S1nsjLcgd3t2M6xhwref521+vRvun66US8w1agly/Tgjt9W5LJc718SoAv8UdPp0fidE5gtMATaUbbOk4sRtza7Ey5K/YndoxMQb22kRJ4POnxXC8vaedOce023iFLR7FPnuziGBfHC3Fu9aNJSjwpj7IODg98hoxheJK7HUgMcGOjzb2dmL1jQT8XEcATwbip3w0by/a0x7GF8AQ9MBCmjz6WTrOIy3PEmGWJdYduS7IpV60DlnqaPbkln6taxzZ4Psu5v5vOfRIQiFBVimFjkElayx1sSzOMc0e6Xm8BeTaxzyR7WhQsbxtbfjnPpywAoJGxQmkeTMY0OVdLjCutTytCEQZzM836u3o5qXMLxNrFGDMDkTxHRJa2rfVGZnCfprVUlULJG5EuTtKng6MCnxFraOyLQ2CvMSTWFZVSi8YPggkizt0MIpDntcQ6UjdV60pGXWShpwneWB54Au8tRWyNe9PcWIDYOjLnAvK8DzuTRUQQ53Tm3JQgG1/ghSynoIQBz8O+UdYAjgh8BjzNA90ENYPSMufInQNrFZMyiiniwGqRaQsI0DCW3bnhhEKIc/OLk7mKBtZVi9zfTaZcxlPGyHTg04Idz+uGIvgzLGEdbOkmvKsYEqn5hO/cxDg4vhCy2NPc0YpnPSBCEXwlBs/roPVUIiLng1I45wZLWmxFy7SzSQn8Nu4RirA6Cqa53x8iDqhpxZ/WStze6k4P8vFxDvq1JhKJHeyZ2SJK4WBXWanuIu+11GCCLDBiLPd0YtZVi4QH0SgCnFsr8UpmuL8zexrjgEN8TahUw4rsln0tAiBaY0V2FZXafWTgz7iQErirHVNUipOK0UGxigFOKRU4MvT5QaM1rYCbLFrg6MDHE3kez9uD589gET+AIBz0RLYfFwV4s2S2Tev4UaPNOdUSizw1z+txOom3RQFnV4v821CLV/eT/jigpIRjogAR+W3ym4fbqlKZTiRY/RZsYzhF2Lw6Gg26mUBq4KE45fdpxvr+ChpeFxnD6MU3XqM82cv2mwFYRvO9lYFvrLA5XHUMrt2aTsTsegmJIoyoO5cF3vA7CiF2FoSO0WRwwNOsq5bmTcQCb/I9PlOvsKHZ5eE4PWB3RoD3FSPqnt5hld4sQUB04onTiVRu+DFq1L0eKyh1/1mVIgUlM4IUYMRarhpq8v5yYTRe5kHiUE9zUb3CHa2YuzvxAXMxByzUig9UCiilfl697LJdUiwSfvXK6UQAzNAQttOOrVL/fmIxyvZnFQXs6OVcM9Tk/FqJ46LggGQsMOBpPlWv8qtOwi878dxaRw5OLxc4OgyGrFI3jHz1a7i0NwXLFPFWrULCCKP1z2qe3vSJ/jJlLbO6jgJ+k/S4eaTDp/orrAy8Wck4oK4VF9er/DpO2bcfsD/yS33NBX1lQqVuc4XCQxKGRO9778SYaW55xSO/49KBOkCCUkOHaP3hl/M8+F2azaq58ZrDF+G8WpntaUZjnzaQY7TGuLhe5fks57ZmZ87FmQIuqlc5o1p60Wn9V67Xe0mco3z1D6aMmT7xsBVIVMAViz8raPX9i+tVjgn9/bqNAja0umzqxnxhwej4yYmlA86uFHHALSNzL3mNgzWliAv6ylYr9c/2sUe3qlIJf9UxU8bNeFBc+fh2vnz4MlyWWav0o/2Kkw7zvWUPdFNaYx3E2eSJsceeT/RXaFrLrsxggbdGAWvLRa4ebk1r2s1KAnhL5PPVgTrLg+AWGwSXycBAD+eo/nDqO+OsJ96VO57nSwtqiO838fzty7V6/2JP9z0Up3Td7GQE2JnlvJQbLqiVMW60ELq4XmPDWDNvLo0Lw+jx/HcDdd5ajB60nvd5Z8wr5Dn9v9g0o0fMKt7CBehaH645ssmJfOHMaumlyxb3M+Dp/acRwGNJj+8NNTm9XODSRf0MGcMDc2wFmbEK8etL6ryzGD1u4fMujp82Lz6PqtZm3XNWufLp5/jyEYdBEECSPKmC4MkjA++kVaHf93Sas3usXp4JmwKGjGVnlrGmFHHzSJvdB+i+jMfNyaWIrw3UOb4Y/cZ53meAh9XiAfTCxdR+vHFWTzigNNaePPpW0m5CGL1HOfut59LspGuHW9ze7NA0DiUzL+aAohISO3vLYvwdcbGnOL+vzMf6Kiz2vZ8Yrb/k0vQJ7/CV5C++SP+dm2bFOOfqu3HGaUgYYEcaiO8v18Zcmlh74YPdpHJzo82WbkrD2glrTF7YMfPrrnWjbYJFWnNqOeK8WpnVhXBQi/qu8fS3Jc+Hk8e2Uv7g2ZR/uP8fEcyrjdD684+Q7dyBKpahWvWk1VyrrL2ka8yp25JeeHcn4cFuws6xN/YcptU0Ska7gn1acUTgc1IpGk/hW6FStxul/kXu3LzFrT0Zl2eoFUdSu+6HB8Q2735I65K/wGzfBlrjul0kKpQl661Vzl1gnHtf05glz/dyebaX80KW86oxdMeO7JISFnma5b7HysDn0MAzFaWeE5G7rFI3uqjw367b6Um5DFlO38a754zrdTd2Gn+2DvfyIFIo4NIE1V/3Xbt9lHL2RGXtu4E3W+eWWOeqdtSDUGCUSENEXnbC76zIfU7Uw96KlTuzZ55yEoW4PMdffijla2+aF54/uEPV/psvkj/yEBJGuCTBZT2Gf/UgC846reh6vQrGlHFOAQ4Ri+e1JIpa2VNPJXrJEsTzkEIR10spnnIGwVe+8rpwHNRWW+uij2N2PIuUy5DnuF4PZ/KJQBER8EZ/2iRBgO12Cd/xLgpf//uDCeP/t/wPUvRvdSWzypoAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMTAtMjlUMDk6MTk6MjIrMDA6MDAYIE/bAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIxLTEwLTI5VDA5OjE5OjIyKzAwOjAwaX33ZwAAAABJRU5ErkJggg=='
fav1=b'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'
pause=b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAABGdBTUEAAK/INwWK6QAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAACTFBMVEUAAAAcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswbmswamcwbmcwuotBCq9VFrNU8qNMjnc4dmswxo9FDq9VErNU5p9MhnM1dt9vL6PPj8vnj8/nf8fik1+swo9Eem8xsvd7R6/Xd8PeW0OcpoM8sodDK5/P////9/v59xeI3ptLa7/f2+/1pvN0Zmcs0pdHm9Pmd0+lDrNXz+vz+//+HyuQZmMvn9Pqe1OmIyuT0+vwypNHf8PiUz+dAqtTs9/v9/v9/xuIinc2V0Of6/f5Qsdgnn8+n2OvT6/UqoM9qvd6Jy+WMzOWCx+NNsNcdm8xwv9+Ky+V+xuIamctpmH6TAAAAeXRSTlMAAAESKj5GUgUrYZzG3e70Bg9Nod/9okux8bIgke0hQ8UDXOFo61s93hy9iP6FBOblCDzqkB7R9/hMg7fSMOLsRPJFNCTYDMKXXi3jLgeoqlj2WRS/FWBfEa4QOzpm9QmN/BOelfp9UcyK5I/a2zUlZKvUJkJ+iZsC0m3d3AAAAAFiS0dEl+ZuG68AAAAHdElNRQflCh0DLSEMm0OaAAAAAW9yTlQBz6J3mgAAAsxJREFUSMeV1udD2kAUAHAOjSIuUKhSBcWFWGtR0bYuqji7abXbgdtOta5LrFpbO9TaXTrp3svuZaf/WC+BJCCEJO/be3e/XALJ3ZNIfAJ4hYQvqFnSoGAsJDQ0BAsOkvIxclgWJg+PiIyKhjA6KjIiXB6mCITQkDImVqWGHqFWLYtRchlUV8TFa6BPaJbHKfwiVExI1EK/oU3U+TGolJQMOSM5yccAoE9JhQEiNUXvbZBIS4cBIz3Ny6BFM3gEMhme9waAIZNPQJhpYAkAxix+AWGWkTboH1+RLYRkr8xxGwCwVWwdJ4hRrsyE0SQ31uNSx8bGJ47j7mTyxMmpU6dxZjA2F7gWyctnapNnzk7PzJ6bc136/IWL0zOXLl9hTH4etQyQmtn7uHrNgeL6DYLMiJu3yOz2HSczwSylSEEhUyHu3iMnOe5TxPngIZk8evyEmVBYQJG41R7kKUWeucgURRzPWbJmLSAfpQgKJ7AIPQxQFIshxQpEjCViSIkRkdIyMSS1FBGDRQyxGBBZVy6GlFcgUiGeYFoxRIshYjWJISYrIpVVYkhVJSLVNWJITTUi0loxpJZ8lUGdWjhR11Fv8voyTvJiKdmwkSKbNjOV0ZevqEmvXeTNWzKZf8d+YluoLxmArTa6gr//8BFNmv1EEfzzl3mUfR0j6HHbNtd+AbbXM1fBv33/sfDz1293Nvfn78K/cfbh6xvoTWmHjTVOHBKLbAbhIrMGtO1k9rFd8VBQ7N7Dbpd7VUJE5j5mU0Y7emMTv2hqBJ77eHOLnU/YW5q9DgvQ2qYOLNRtrd5nHwAN7R2BREd7g+9hqey0cAtLp9Lfkazv6uY4ZrK7u/R+Dn6y7dD17PcnTD06jqaEbGCsBw4u+ensh8yHZdxdDBrRH+nt69fQ8zX9fb1H9fy9Uk7CgHxwaHh4aFA+kJAjpCdztWQjMtkIRzP2H7XOVyvffYGZAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTEwLTI5VDAzOjQ1OjE4KzAwOjAwY+s9nAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0xMC0yOVQwMzo0NToxOCswMDowMBK2hSAAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
play=b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAABGdBTUEAAK/INwWK6QAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAACeVBMVEUAAAAcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswcmswbmswjnc4dmswamcwbmcwuotCDyOOw3O2QzuY/qtQgnM2W0Of9/v7////V7PZqvd0inc02pdLy+fye1Ok7qNMamcs+qdTd8PfR6/Vmu90hnM09qdPx+fyY0eg2ptL+///J5/Net9vs9/uRzuYypNEZmcv9/v/E5fJYtdkem8zq9vqLy+UvotD7/f694vBRstgdm8zj8vllu93G5fItotDX7fY4ptKl1+v2+/2q2ew6p9N2wuAnn8/5/f6z3e5Irdbh8vh9xeIpoM/6/f654O9NsNfn9PqGyeTB4/FTstg9qNONzOUwo9DF5fJZtdofm81kutze8Pj4/P3o9fqTz+czpNFAqtRjutxHrdZ9Qv5+AAAAeXRSTlMAAAESKj5GUgUrYZzG3e70Bg9Nod/9okux8bIgke0hQ8UDXOFo61s93hy9iP6FBOblCDzqkB7R9/hMg7fSMOLsRPJFNCTYDMKXXi3jLgeoqlj2WRS/FWBfEa4QOzpm9QmN/BOelfp9UcyK5I/a2zUlZKvUJkJ+iZsC0m3d3AAAAAFiS0dEh/vZC8sAAAAHdElNRQflCh0DLQPZ+wJ+AAAAAW9yTlQBz6J3mgAAAu1JREFUSMeN1mdbE0EQAGA2EAmhJUCECAFCC8GIoaq0SAc7CnZ6twLSNhhsyGJFFHtBBRsq9t57r7/IzYUke8nenfNx595nruzNjouLUwBWuAgFc5XI1U08xd19itjNVSTEzGmJh9TTy9vHF0JfH28vT6mHjA/hlNzPP0ABiVAETPWTcxm8LgsMUkKnUE4LlFERXgwOUUFqqEJCKQYvhYVDzggPczIAqCMiIU9ERqjZBouoaMgb0VEsg4vGCAhsYsh7A0ATKyQgjNXYCQDaOFbSSDdxWqvBX3y6jgTGnq0mGtHNiJ80AIhnEonebdt37NxlpFXSi60kwZ9c79vdj9DAnr20Qv4JwFIkMYlYNe0bQDj2Hzhoci6UlMiUAaJkcnXw0BBi4vCRYedCySKGpKSyyNFJgo4dP+FkUlMYEjiLTtDJU6f7etlk9hxgfpQ0yEEQOnP23AjbpOGHAbJ0boLOX7g4yrq7dBkm2gwegtDYpcukydBikpnFS9CVq9fG7enITEw0Bn6C0PUb9pdg0GAyN1uIoJsTNpOdg0mOMLl128QiYpUgudNj2zsqMSa5egFy9959+7PoczHJy+cnQw8eEm85Pw+TgkI+8ujxE9avU1iAiaiIhzx99py9Y4rMWxkUK7jIi5evHPqAopjZyfOyOMjrNxOOu3/+AoYsXEQl/W/fjTtsfQgXM38yAEtKSPLeQsY+fBxxBLBkqaVfgGWlxGrvxCdm03/+QukXpWXWprScLGP8+u37j5+/aA2mZIWtj60MIhOjv//8He6lCLhqtb1drgkgM6ZBE7XFxq61NWXc0csroGBUlAOyj1dWVQuJ6qpK1mEBamoV/EJRW8M++wAoq6vnE/V1Zc6HpbzBwC0MDXLakaxubNLRga6pUU05+M1jR2jzOprQN4dyDCXmASZ3/QaHV1e9MXmThHuKwRn15pbWNqX1emVba8sWtfCsFB/cLu3o7Orq7JC2B8f/z0xmGcm6JZJujmHsH4alRl8hlfVGAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTEwLTI5VDAzOjQ0OjUyKzAwOjAwrBMHFgAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0xMC0yOVQwMzo0NDo1MiswMDowMN1Ov6oAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC'
prev=b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAAB3RJTUUH5QodAwwlh2mSYAAAEG1JREFUaN61WnuQVNWZ/33fOffe7p5+zANmGN4MoAhoQPH9QhyT7FYSg4J5rJtaN1ur+0gqKd2qNUnFYHxRSYkayyy6G5MyFTWmNMSoGwXlEUBXVBAF0WBkFASGYV70dPe995xv/7i3e7rnJWhyq6a+vj237/1+5/e9z6X29sUEgDD2QQAklhYAl6UT5u1F61/GzY+IFL4ETP3HVS6aZ+ZM3fgcic1JIuOyDcmGYZHDwjEbBkfr9m3qf/fGFaVwbnTzT196vrLsCSDl55zwQe3ti1X8mYcqOaoksm6hi57etCO8dF6LfueKX7ZIIvsp0YkzhfhUIZ4mgkYLSoHgAACJBEQ0QLBdJPI+iXmdjP8KDxzdPuOJaw6+sOtg+Lnz5qpSqgVVgIbK0XQSihnRxweC2Bs4ZK/esst+/1/vS/qtnzrbeumlFmpJCJruG0kFVii0AiMQEQsRIoIARMIAmIk0ExwmcZkKmuQ9JWYdBQNrEvtfeXHdT/994J/Pn89+cjwBcjwgGIA5IUbuW7s+XP7lbyd6T/vqRaK9awPSi4uhbRgIrQTGwgri1RxtQaslhAlwFCOpmZKaexyYDRQUfprZvWbjDQ/dWnwo0u14mKkwokZHTVb7ffTMxlfCWTetPcWkW74dgpcfC1Gf9wMJ7QkpP9ohmgl1rqI6zT0Owt9wvuuu1T+4ZNedFy5UgVcvI5hbDSMcfxjRkUFs6468SYezc2jW7S9fZbITH8tb/qfDBZPtLfoILej4QYzpwxRaod5iiM5CkM1b9XWbaXnsuju2feVQ42mcOfgKQDz0htW6QrW1TccQMFIG0bD3eey+7O5E4bTlN4Q6dVt30UzpLYUw1vLxK39CzMAKqBBYhIJxnpdoD6ec6XQ3zd/WtvGeYKC5DaMwI6qtbXrZRwYvIJaGd57HzisfrrOTF/6wSN71nQNBKh9YPjEGPh4YAOQboZIRN+G656v6iQ2HZ1y8eca6H/mFWjA1jFAtIySpwzvx9mfuStjJp/+wCPffDudLumiE6RMrf0JgEFqhYmgp4bpn6ExT7sikMza27vhZ4GcmYegNVVvbdK5mRPl91Nl8JpcWfPn6InnXH8yXdOmvAuL4wBgBFUODpOsu1PUTTPFY7+Z0/z5YnahxPh5yR7p646smf/F/fDFQiRsO533nrwvi+JK4b4QP530nYO9bAxd8c9mVm14zQ1eDB0EQzli73qy8ZcPJ4qVv6ioEuUJoPzYIEYFYQKxA/gJgCqGlI4UgK27qe3ffunHukrXrDUCVG5R9hHSxW9688GrXtF2wojfAZ48UAnxcxxYRzG9J4vMnZTG7yUNnPkTeFxB9MjPzQwtXq3GpZMp7e0LDc5mDrxrrpAiAxIwQbvvjDusv/OpFAanlRwoBRD4+iCvn1mPNl6bigS9MxkNLJ+PnS6dgclZD5JMxIwB1FQLxSS0LTr3ior/b8oaNVydiROcP45HLv5uUCXNv6SrJ6b3FgKrc5oRALJtXj5/8TSum1ruwIlDMmN3oYv+xEFs78iD6ZAHAWCGtVCLtuZmXTpr3ZObddaF108QA6Otbd1nbdsGiALykpxDI8JuN/XCpAnHPZ1vRmnEQGgsigrUWxIxpWQfEBIaAiECfgJnuQiAB+GKZetY5z7y42wAkzKYk9zaD2au74phvG0rGjvLz4Q8tK8MQXFUDQsDMsNZCMaPkh9h+YACaAK0UHCJoZmgCmBg84v3H8BVj0e/bevZSl190SrNmUyKe+MJWyX/j2QmW9SW9pRAyJrfRQwgEJoCZoRm4an4D7iqDsAJmgpUITGgtfra1E0/t6ELC0XAVwdGqSgJaMRwG1DBQo/tKbykUS/rSwtUPT3j2+c2Gt3SIcLZ5vm/RNhAYGctCCYAiQtRPMBwmXDWvAas+PQGtGQfGCpgiM2MiGGvx4NZO3PxUB0qk4CmCqxRcBhyl4DJFUkXSUQStosXhivmNrEchMPAtpnN63IKJADicArD2ziqENhVaGQMAIgCK4SiGZsKyuTn8+LIWTIhBUAyCYhA/39qJFb/fh5J2kEp7sfKAq8sgeGTJCg4TFJcZGn6EVjAQ2iQ77hmTuwE1s4NcnrLgus5COP+Yb2goI0yA4vJKMRQzFBOuPCWHlR8B4uanOlByXGQa66CUhiIBK66YpYp9JJKRuRIRmCRmBFVRbrh5JTRTfcI5Kr+4b43WM8/JCmh6KZSos4yhUBUIRVSRTITL52Rx+6XNaEnrEUE8uq0LP37uA+ikhwlNdSBWgAiEOJJxlLPgSArDisAKUAoNikZBiY3AWQETw1iLsoplKMXQQkBTaPYlGa3qxuUC4sbA2BoQKnY+zVQD5gsnZ3Drkma01EUgAFRAiAhECHMmJHH/1bOhXQVWCiJRKBYrII4lRQEhCtHR99ZadBUsHt7Ziw37BsC2DMaCSIGMRQiJW2pCYAQCanJct1ETU0ZEUkZECEJEBB0rXQahiUBEOGtSEjcvHh+BkFq6y2AUCxZNSw+G0jLLxyshOGdyEtc+eQAv7i+CRUDEIGtBiGRoASMWRkQESLGbTLP2UgkQuyJChEjpeMoBzRxFJxXJy9rSmJh1hoEYCsZYgZVY4qNlaOzguRAm1Cl8ZlYGbuybkS6qolM5qkGEQOwo7SQ0EYQwuJrlCyM5yAoh+vxRR7WZHa8sJ89IClgTIFF+EbFgMAgRI9WtejlEs3KExS/6msjXTDIMRBxmI1YIz+7qwQfdJagxAJXLD6Wi6DO65BqptYol44OuEtbt6YUTh+JBXVDRSUU6iSIKpNjva4LtVYwBTymCmFoQFP+QovPX9x/D99Z04I6l09CSc2GH5B0iIDAWuw4U0FsIodSgg1s7dOWjFbVDGDrU5+PRbV3Y3hUi1ZBGaAxADDIWUAowBmCGwMBVijRjAMS9Wo4d7XPqmrqSmmeFIoOMxMMzXbFLQjqdxHN7esC/7cBtX5w6DIxIFK73dhax8g/70V80UR6ocujy1RL/QOLJjo1L/FIosERoaq2HZoCgQMaAFAPGRuEUFhaMpGY4TEdt/+Fe1Tp1epCYtuDSAUPzSqEZdC7FUXGnBs0t4Wl4rsabHX3Y11XE2TPSyCQ0qn2fAMxpTSKX1Hj9Qx+GGFpraM1QWkNrBaV1ZFJaRwkylqQUvISDxnFZJFPuYANYzj9E8QoQRIBswkG9i62Fvf/3K/X51zbYnu3dJxvwJcd8C4eJasDUOD4jmXSQcJ0IzJESzpqRRsbTNbmXAcybmMKUljp02gSyuRSamtJobEihsXFQNtQnUd+QRn0uiWx9HXK5JDK5FBxXg2jIqI0YFI+CJZ4lj0tqpJT8+qL/vOx51fKtH0B2Hkizm1za74cOE5PDcbnNQ80rAlWXdJHwHLzR0YeOGEzaU8MKiZmNDuoTjL09URJzlIqSq4rKHMUMZgJzVLYQc6UsIYmZqMpHQoP9jyJgfJ1XcIL8XQfC5ne42EBk893bEyx7065DigBVZU6qqndQzJU809iQwuRJDVj/Tj9WPPk+DvcHUWwfciye7uEr85PIeGqw6KzyO4erg8qgf6rKuaqcq1gHRUCdqynB8mdb6N3hn0OkZi0+l/ufuaNQt+Qbs8F8TsGIaAZppaAZcfiril7lbM+MdMpF0nPwxr4+dHSVsGj6yMxMyykcKVh80C9RgchRRmCO80BcIIIY8RZEzAgBYgczf1yjASSNCYeSSh7tvXPJ4968ucKiPbp8XylEoW9NxtXdSU0xaokr3cFVUFUgVMzY+MY0Zkxtwqa9x3DrUx+gcwRmNAMzGuKmqpybKlLVhvsyA5VnqhomFDMSmpF2VTeKfU/87Z7OUNw0MwBZd8ECXdy79SUXZm0u4ZLC4A+ZqOpGVPleV5lZc1MaM6eNwx/35nHr0/vR2R/UJE0LoLPfVOo3Z6hZVZnXcOWjBeWq82zCIRdmffG9V1/acN6pGoCNxkGpRvnwR9cWJSiszjp0NOEoUYiq39rViEBVHqioEggmNKUxe/o4bN6bx21P78f7R0tRhhBg09v9+MObPbFvUMxmLGN/VKrWV2p8Il5YJsDTWjIO9UhQWP3+7f9QQHq8AODygE5lmlPw8737U21nT1FKLwoFUARSquwjqjI8qC5jVGVVCdk6D6mkgx3v9WDL3n7sOVTEMzt78cjLXdCeh6ZcChQ3T2WJsk8MGTxITRIlSOQrknEVPLK/7N9w/+qc22XJS1c2eqLUmm7h3b+4sxT2fnh3SmNXncNR94bBSUfF3IYwpDhquBQTJo5LY25bMw72Gfz2tW48/1YvtOticku2pkrQTMNsvyy5SkahOSpvUpqRVLQ77Plw1c4HVxYp21qpIqm9fTEj2nqzAPHatS8ESx/cs5yTufvzvsmCiJ3qsDlCxh/sIAcVyBd89PQV4WqFpvokPFdXukArAhttmMJYCyNAaC2MBQJrEVpBYAZlYKOd1aTDfbbQe90T15z8aHv7YqeqFDblbYXKpsmMSeNU31tb3srMbyfX9S4UCDMxRY6tKj6ih0Sv6lXVzEglNMblUsilPbhaVUZIVAm1gzVNTf0Vm5VQBDgOujbhcEDBwMqu393y37OaFJP2qjd6qAYEAKZERpwD25B/a+NdHJbuTTrKKIKNsm5EMSMe11DUT/NIJlL+nqp7fq7t/2OT5NhnKrKcZ6KBhPW0MhyU/iv/pxdX0a7fCSVzQzdDZRgjAJgzzVJct8rwzAu3uLnmpOO4iwhgpRSVHb6idJxnmGtDs4pBlBWjuMynco6pYSJa+fKfFYn2nEUsEwIEhfsKHTtu6vvJsoJ70nmAyNDd58pmqKr9h7Aa3yb5/10Z0OSFm9zGSSXlOIuY4MXKklIjJyytVIWJsrNSHDAq5XFsVzUAaqYrECMWAumz/sAdx97efFvPPcsLiYVLALEjvQdQ2QwdYY9dWI9vk9K2X9m+P+/YnD5l8Z9Yu/NANF5F2ZeGZd0qpqIoVy5FGOX5jFTCa/lPIhmDMQLxjYEx4S5T6Lvh4OPf/x//hVWBN+f80UBYVH2gES8Qy7p1rjgDB/HI12Y/VurqWGaC0upS4Hf7VmCtFRDFPX/UM5QbqXLLy1yVM0gqphV9VzE1sSJSCi2KQdAT+qUH/KP7lz3ytdm/UYd3iTP1dEAsYfQ3MzDS9vSwC0m70tY2Q//+nu90tmZ5rTt5/ktWkAxBE61IMp4WilIMBkgxD/GNMhNRQyQEWAsJraAUGsoHhvJ+0FPyS08HA/03dq2/f/W2FX9/6Oz2xYqcmk3P0XTE0Fc4RgVTzjO2/6Dd8tJu237jA4nsyRecrVLZy7XSSxztzPQ0pxKOpvKwWhFEMVPkDZDQCPmR8iiGRopBOBCE5t0w9F8wxfzj/bvXb3vyjmsHlpx7GnO6iWrGimODqXmp5qNQ17zmZPNHad3m7eGZkx3d9t3N4510wwL2Uqcz82lK6WlM1MTMKSY4AJG11rfAgDXmqLXynjHBGzYovRz0Htr51o3nH3y9H/aSs+awyrUSaudmY+0IDXupZqw3g8beJwtL8uH6rfI5EbkGwDf/ZYWTm7skpzNNWRDltJtyQaCwOFAEpD/s7+rt27Op7/Z7v+P/GsDjRDR18bkE7R3Pntyoby/9P7LWcxNd7MOAAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTEwLTI5VDAzOjEyOjMzKzAwOjAwsELZIAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0xMC0yOVQwMzoxMjozMyswMDowMMEfYZwAAAAASUVORK5CYII='
nex=b'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'
shu=b'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'
pygame.mixer.init()
def new_fav():
    window.find_element("sh").Update(image_data=fav0)
theme("black")
layout=[[Button("",image_filename="Assets/gif_new.png",visible=True,key="tst",button_color=("black","black"),border_width=0)]+[Text("      ")]+[Text("@16 mUSIC PlaYEr",font=("Pricedown",30))]+[Text("      ")]+[Button("",image_filename="Assets/fav_list.png",key="fav_list",button_color=("black","black"),border_width=0)],
        [Image(filename=images[c_g],key = "Prog_bar",background_color="black")],
        [Text(" ",key="mname",font=("Chilanka",15))],
        [pin(Button("",visible=False,image_filename="Assets/allsongs.png",key="als",button_color=("black","black"),border_width=0))]+[pin(Text("      ",visible=False,key="als2"))]+[pin(Text("00:00/00:00",visible=False,key="timer"))]+[pin(Text("      ",visible=False,key="in2"))]+[pin(Button("",visible=False,image_filename="Assets/info.png",key="in",button_color=("black","black"),border_width=0))],
        [Slider(range=(0, 100),background_color="blue",trough_color="white",disable_number_display=True, key='sl', orientation='h', size=(50,5))],        
        [Button("",image_data=fav0,key="sh",button_color=("black","black"),border_width=0)]+[Text("        ")]+[Button("",image_data=prev,key="pr",button_color=("black","black"),border_width=0)]+[Button(" ",image_filename="Assets/pause.png",key="pl",button_color=("black","black"),border_width=0)]+[Button("",key="fv",image_data=nex,button_color=("black","black"),border_width=0)]+[Text("        ")]+[Button("",image_filename="Assets/shuffle.png",key="sh2",button_color=("black","black"),border_width=0)]]
window = Window('Music Player @ 16', layout,element_justification="c",return_keyboard_events=True).Finalize()
st="play"
window.TKroot.focus_force() # So that spacebar will be free from button focus
music_playing=True
pause=False
sh=False
tl=False
music()
tm=0
while True:
    if not pygame.mixer.music.get_busy():
        if pause==False:
            if repeat==False:
                forward()
            else:
                forward(rpt=True)
    tm=str(pygame.mixer.music.get_pos())
    tm=tm[:-3]
    if tm=="":
        tm=0
    else:
        tm=int(tm)
    def time_(tm,t):
        if tm>60:
            tm1=tm//60
            tm2=tm%60
        else:
            tm1="00"
            tm2=tm
        if t>60:
            t1=t//60
            t2=t%60
        else:
            t1="00"
            t2=t
        if len(str(t2))==1:
            t2="0"+str(t2)
        if len(str(tm2))==1:
            tm2="0"+str(tm2)
        window.find_element("timer").Update(str(tm1)+":"+str(tm2)+"/"+str(t1)+":"+str(t2))
    time_(tm,t)
    e,v=window.read(timeout=10)
    window.find_element("sl").Update(tm)
    if e==None:
        pygame.mixer.music.stop()
        window.close()
        f=open("Data/maindata.dat","wb")
        for i in l:
            pickle.dump(i,f)
        f.close()
        break
    if sh==True:
        if musics[m_c] in l:
            window.find_element("sh").Update(image_data=fav1)
            favourite=True
        else:
            window.find_element("sh").Update(image_data=fav0)
            favourite=False
    else:
        if m_copy[m_c] in l:
            window.find_element("sh").Update(image_data=fav1)
            favourite=True
        else:
            window.find_element("sh").Update(image_data=fav0)
            favourite=False
    if pause==False:
        if tl==False:
            window.find_element("Prog_bar").UpdateAnimation(images[c_g],time_between_frames=0)
    if e=="pl" or e==" ":
        if st=="play":
            if repeat==True:
                window.find_element("pl").Update(image_filename="Assets/repeat_play.png")
            else:
                window.find_element("pl").Update(image_filename="Assets/play.png")
            st="pause"
            sound()
        else:
            if repeat==False:
                window.find_element("pl").Update(image_filename="Assets/pause.png")
            else:
                window.find_element("pl").Update(image_filename="Assets/repeat_pause.png")
            st="play"
            sound()
    elif e=="tst" or e=="g":
        image_ch("r")
    elif e=="e":
        if vis_el==True:
            vis_el=False
            window.Element('als').Update(visible=False)
            window.Element('als2').Update(visible=False)
            window.Element('timer').Update(visible=False)
            window.Element('in').Update(visible=False)
            window.Element('in2').Update(visible=False)
        else:
            vis_el=True
            window.Element('als').Update(visible=True)
            window.Element('als2').Update(visible=True)
            window.Element('timer').Update(visible=True)
            window.Element('in').Update(visible=True)
            window.Element('in2').Update(visible=True)
    elif e=="m":
        call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
    elif e=="i" or e=="in":
        window.Hide()
        vl2=fv2()
        if vl2==1:
            window.UnHide()
    elif e=="fav_list" or e=="l":
        window.Hide()
        vl=fv()
        if vl==1:
            window.UnHide()
        #window.Element('tst').Update(visible=False) to hide an element
    elif e=="pr" or e=="Left:113":
        backward()
    elif e=="r":
        if repeat==False:
            if st=="play":
                window.find_element("pl").Update(image_filename="Assets/repeat_pause.png")
            else:
                window.find_element("pl").Update(image_filename="Assets/repeat_play.png")
            repeat=True
        else:
            if st=="play":
                window.find_element("pl").Update(image_filename="Assets/pause.png")
            else:
                window.find_element("pl").Update(image_filename="Assets/play.png")
            repeat=False
    elif e=="sh2" or e=="s":
        if sh==False:
            window.find_element("sh2").Update(image_filename="Assets/shuffle0.png")
            sh=True
            random.shuffle(musics)
            forward()
        else:
            sh=False
            window.find_element("sh2").Update(image_filename="Assets/shuffle.png")
            forward()
    elif e=="o":
        if tl==False:
            window.find_element("Prog_bar").Update("Animations/Black.png")
            tl=True
        else:
            tl=False
    elif e=="a" or e=="als":
        window.Hide()
        vt=fv3()
        if vt==1:
            window.UnHide()
    elif e=="sh" or e=="f":
        if sh==True:
            if favourite==False:
                favourite=True
                if musics[m_c] not in l:
                    l.append(musics[m_c])
                window.find_element("sh").Update(image_data=fav1)
            else:
                if musics[m_c] in l:
                    l.remove(musics[m_c])
                favourite=False
                window.find_element("sh").Update(image_data=fav0)
        else:
            if favourite==False:
                favourite=True
                if m_copy[m_c] not in l:
                    l.append(m_copy[m_c])
                window.find_element("sh").Update(image_data=fav1)
            else:
                if m_copy[m_c] in l:
                    l.remove(m_copy[m_c])
                favourite=False
                window.find_element("sh").Update(image_data=fav0)
    elif e=="fv" or e=="Right:114":
        forward()
    elif e=="Up:111":
        call(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
    elif e=="Down:116":
        call(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
