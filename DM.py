##d&d char she
import os,sys
from tkinter import *

##tkclass##
class basewin:
    winsizexy = '800x600'
    wintitle = 'base title'
    def __init__(self):
        pass

class basemaster(basewin):
    def __init__(self):
        This_win = Tk()
        This_win.title(self.wintitle)
        This_win.geometry(self.winsizexy)
        This_win.mainloop()

class basetoplevel(basewin):
    def __init__(self):
        This_win = Toplevel()
        This_win.title(self.wintitle)
        This_win.geometry(self.winsizexy)
        This_win.mainloop()

class main_win:
    This_win = Tk()
    ##variables
    ##primary attributes
    primaryattributes_STR_BOX_VAR = StringVar()
    primaryattributes_DEX_BOX_VAR = StringVar()
    primaryattributes_CON_BOX_VAR = StringVar()
    primaryattributes_INT_BOX_VAR = StringVar()
    primaryattributes_WIS_BOX_VAR = StringVar()
    primaryattributes_CHR_BOX_VAR = StringVar()

    ##inspiration
    inspiration_STR_BOX_VAR = StringVar()
    
    ##proficiency bonus
    proficiencybonus_STR_BOX_VAR = StringVar()
    
    ##saving throws
    savingthrows_STR_CHK_VAR = IntVar()##chkboxes
    savingthrows_DEX_CHK_VAR = IntVar()
    savingthrows_CON_CHK_VAR = IntVar()
    savingthrows_INT_CHK_VAR = IntVar()
    savingthrows_WIS_CHK_VAR = IntVar()
    savingthrows_CHR_CHK_VAR = IntVar()
    
    savingthrows_STR_BOX_VAR = StringVar()##entries
    savingthrows_DEX_BOX_VAR = StringVar()
    savingthrows_CON_BOX_VAR = StringVar()
    savingthrows_INT_BOX_VAR = StringVar()
    savingthrows_WIS_BOX_VAR = StringVar()
    savingthrows_CHR_BOX_VAR = StringVar()

    
    ##secondary skills

    def __init__(self):
        
        self.This_win.title('Dungeon Master v1')
        self.This_win.geometry('640x720')
        ##widgets
        primaryattributes_LF = LabelFrame(self.This_win,text = 'primary\nattributes')
        primaryattributes_STR_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_STR_BOX_VAR).pack()
        primaryattributes_STR_LBL = Label(primaryattributes_LF,text = 'Strength').pack()
        primaryattributes_DEX_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_DEX_BOX_VAR).pack()
        primaryattributes_DEX_LBL = Label(primaryattributes_LF,text = 'Dexterity').pack()
        primaryattributes_CON_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_CON_BOX_VAR).pack()
        primaryattributes_CON_LBL = Label(primaryattributes_LF,text = 'Constitution').pack()
        primaryattributes_INT_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_INT_BOX_VAR).pack()
        primaryattributes_INT_LBL = Label(primaryattributes_LF,text = 'Intelligence').pack()
        primaryattributes_WIS_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_WIS_BOX_VAR).pack()
        primaryattributes_WIS_LBL = Label(primaryattributes_LF,text = 'Wisdom').pack()
        primaryattributes_CHR_BOX = Entry(primaryattributes_LF,width = 5,textvariable = self.primaryattributes_CHR_BOX_VAR).pack()
        primaryattributes_CHR_LBL = Label(primaryattributes_LF,text = 'Charisma').pack()
        primaryattributes_LF.place(x=50,y=50)
        
        #savingthrows_LF
        inspiration_LF = LabelFrame(self.This_win,text = 'inspiration points')
        inspiration_STR_BOX = Entry(inspiration_LF,width = 5,textvariable = self.inspiration_STR_BOX_VAR).grid(row = 0,column=1)#.pack()
        inspiration_STR_LBL = Label(inspiration_LF,text = 'inspiration').grid(row = 0,column=0)#.pack()
        inspiration_LF.place(x=0,y=50)
        
        proficiencybonus_LF = LabelFrame(self.This_win,text = 'proficiency Bonus')
        proficiencybonus_STR_BOX = Entry(proficiencybonus_LF,width = 5,textvariable = self.proficiencybonus_STR_BOX_VAR).grid(row = 1,column=1)#.pack()
        proficiencybonus_STR_LBL = Label(proficiencybonus_LF,text = 'Proficiency bonus').grid(row = 1,column=0)#.pack()
        proficiencybonus_LF.place(x=0,y=150)
        
        savingthrows_LF = LabelFrame(self.This_win,text = 'Saving\nThrows')
        savingthrows_STR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_STR_CHK_VAR).pack()
        savingthrows_STR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_STR_BOX_VAR).pack()
        savingthrows_STR_LBL = Label(savingthrows_LF,text = 'Strength').pack()
        savingthrows_DEX_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_DEX_CHK_VAR).pack()
        savingthrows_DEX_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_DEX_BOX_VAR).pack()
        savingthrows_DEX_LBL = Label(savingthrows_LF,text = 'Dexterity').pack()
        savingthrows_CON_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CON_CHK_VAR).pack()
        savingthrows_CON_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CON_BOX_VAR).pack()
        savingthrows_CON_LBL = Label(savingthrows_LF,text = 'Constitution').pack()
        savingthrows_INT_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_INT_CHK_VAR).pack()
        savingthrows_INT_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_INT_BOX_VAR).pack()
        savingthrows_INT_LBL = Label(savingthrows_LF,text = 'Intelligence').pack()
        savingthrows_WIS_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_WIS_CHK_VAR).pack()
        savingthrows_WIS_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_WIS_BOX_VAR).pack()
        savingthrows_WIS_LBL = Label(savingthrows_LF,text = 'Wisdom').pack()
        savingthrows_CHR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CHR_CHK_VAR).pack()
        savingthrows_CHR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CHR_BOX_VAR).pack()
        savingthrows_CHR_LBL = Label(savingthrows_LF,text = 'Charisma').pack()
        savingthrows_LF.place(x=150,y=50)

        #secondaryskills
        secondaryskills_LF = LabelFrame(self.This_win,text = 'skills')
        secondaryskills_ACR_CHK = Checkbutton(secondaryskills_LF).grid(row=0,column=0)#).pack(side=LEFT)
        secondaryskills_ACR_BOX = Entry(secondaryskills_LF,width = 5).grid(row=0,column=1)#.pack()
        secondaryskills_ACR_LBL = Label(secondaryskills_LF,text = 'acrobatics').grid(row=0,column=2)#.pack()
        secondaryskills_ANH_CHK = Checkbutton(secondaryskills_LF).grid(row=1,column=0)#.pack()
        secondaryskills_ANH_BOX = Entry(secondaryskills_LF,width = 5).grid(row=1,column=1)#.pack()
        secondaryskills_ANH_LBL = Label(secondaryskills_LF,text = 'animal handling').grid(row=1,column=2)#.pack()
        secondaryskills_ARC_CHK = Checkbutton(secondaryskills_LF).grid(row=2,column=0)#.pack()
        secondaryskills_ARC_BOX = Entry(secondaryskills_LF,width = 5).grid(row=2,column=1)#.pack()
        secondaryskills_ARC_LBL = Label(secondaryskills_LF,text = 'arcana').grid(row=2,column=2)#.pack()
        secondaryskills_ATH_CHK = Checkbutton(secondaryskills_LF).grid(row=3,column=0)#.pack()
        secondaryskills_ATH_BOX = Entry(secondaryskills_LF,width = 5).grid(row=3,column=1)#.pack()
        secondaryskills_ATH_LBL = Label(secondaryskills_LF,text = 'athletics').grid(row=3,column=2)#.pack()
        secondaryskills_DEC_CHK = Checkbutton(secondaryskills_LF).grid(row=4,column=0)#.pack()
        secondaryskills_DEC_BOX = Entry(secondaryskills_LF,width = 5).grid(row=4,column=1)#.pack()
        secondaryskills_DEC_LBL = Label(secondaryskills_LF,text = 'deception').grid(row=4,column=2)#.pack()
        secondaryskills_HIS_CHK = Checkbutton(secondaryskills_LF).grid(row=5,column=0)#.pack()
        secondaryskills_HIS_BOX = Entry(secondaryskills_LF,width = 5).grid(row=5,column=1)#.pack()
        secondaryskills_HIS_LBL = Label(secondaryskills_LF,text = 'history').grid(row=5,column=2)#.pack()
        secondaryskills_CHR_CHK = Checkbutton(secondaryskills_LF).grid(row=6,column=0)#.pack()
        secondaryskills_CHR_BOX = Entry(secondaryskills_LF,width = 5).grid(row=6,column=1)#.pack()
        secondaryskills_CHR_LBL = Label(secondaryskills_LF,text = 'insight').grid(row=6,column=2)#.pack()
        secondaryskills_IDT_CHK = Checkbutton(secondaryskills_LF).grid(row=7,column=0)#.pack()
        secondaryskills_IDT_BOX = Entry(secondaryskills_LF,width = 5).grid(row=7,column=1)#.pack()
        secondaryskills_IDT_LBL = Label(secondaryskills_LF,text = 'intimidation').grid(row=7,column=2)#.pack()
        secondaryskills_INV_CHK = Checkbutton(secondaryskills_LF).grid(row=8,column=0)#.pack()
        secondaryskills_INV_BOX = Entry(secondaryskills_LF,width = 5).grid(row=8,column=1)#.pack()
        secondaryskills_INV_LBL = Label(secondaryskills_LF,text = 'investigation').grid(row=8,column=2)#.pack()
        secondaryskills_MED_CHK = Checkbutton(secondaryskills_LF).grid(row=9,column=0)#.pack()
        secondaryskills_MED_BOX = Entry(secondaryskills_LF,width = 5).grid(row=9,column=1)#.pack()
        secondaryskills_MED_LBL = Label(secondaryskills_LF,text = 'medicine').grid(row=9,column=2)#.pack()
        secondaryskills_NAT_CHK = Checkbutton(secondaryskills_LF).grid(row=10,column=0)#.pack()
        secondaryskills_NAT_BOX = Entry(secondaryskills_LF,width = 5).grid(row=10,column=1)#.pack()
        secondaryskills_NAT_LBL = Label(secondaryskills_LF,text = 'nature').grid(row=10,column=2)#.pack()
        secondaryskills_PER_CHK = Checkbutton(secondaryskills_LF).grid(row=11,column=0)#.pack()
        secondaryskills_PER_BOX = Entry(secondaryskills_LF,width = 5).grid(row=11,column=1)#.pack()
        secondaryskills_PER_LBL = Label(secondaryskills_LF,text = 'perception').grid(row=11,column=2)#.pack()
        secondaryskills_PRF_CHK = Checkbutton(secondaryskills_LF).grid(row=12,column=0)#.pack()
        secondaryskills_PRF_BOX = Entry(secondaryskills_LF,width = 5).grid(row=12,column=1)#.pack()
        secondaryskills_PRF_LBL = Label(secondaryskills_LF,text = 'performance').grid(row=12,column=2)#.pack()
        secondaryskills_PRS_CHK = Checkbutton(secondaryskills_LF).grid(row=13,column=0)#.pack()
        secondaryskills_PRS_BOX = Entry(secondaryskills_LF,width = 5).grid(row=13,column=1)#.pack()
        secondaryskills_PRS_LBL = Label(secondaryskills_LF,text = 'persuasion').grid(row=13,column=2)#.pack()
        secondaryskills_REL_CHK = Checkbutton(secondaryskills_LF).grid(row=14,column=0)#.pack()
        secondaryskills_REL_BOX = Entry(secondaryskills_LF,width = 5).grid(row=14,column=1)#.pack()
        secondaryskills_REL_LBL = Label(secondaryskills_LF,text = 'religion').grid(row=14,column=2)#.pack()
        secondaryskills_SOH_CHK = Checkbutton(secondaryskills_LF).grid(row=15,column=0)#.pack()
        secondaryskills_SOH_BOX = Entry(secondaryskills_LF,width = 5).grid(row=15,column=1)#.pack()
        secondaryskills_SOH_LBL = Label(secondaryskills_LF,text = 'sleight of hand').grid(row=15,column=2)#.pack()
        secondaryskills_STE_CHK = Checkbutton(secondaryskills_LF).grid(row=16,column=0)#.pack()
        secondaryskills_STE_BOX = Entry(secondaryskills_LF,width = 5).grid(row=16,column=1)#.pack()
        secondaryskills_STE_LBL = Label(secondaryskills_LF,text = 'stealth').grid(row=16,column=2)#.pack()
        secondaryskills_SRV_CHK = Checkbutton(secondaryskills_LF).grid(row=17,column=0)#.pack()
        secondaryskills_SRV_BOX = Entry(secondaryskills_LF,width = 5).grid(row=17,column=1)#.pack()
        secondaryskills_SRV_LBL = Label(secondaryskills_LF,text = 'survival').grid(row=17,column=2)#.pack()
        secondaryskills_LF.place(x=150,y=50)        
        
        HPmiscskills_LF = LabelFrame(self.This_win,text = 'HP/misc')
        HPmiscskills_AMC_BOX = Entry(HPmiscskills_LF,width = 5)             .grid(row=1,column=0)#.pack()
        HPmiscskills_AMC_LBL = Label(HPmiscskills_LF,text = 'armour class') .grid(row=0,column=0)#.pack()
        HPmiscskills_INI_BOX = Entry(HPmiscskills_LF,width = 5)             .grid(row=1,column=1)#.pack()
        HPmiscskills_INI_LBL = Label(HPmiscskills_LF,text = 'initiative')   .grid(row=0,column=1)#.pack()
        HPmiscskills_SPD_BOX = Entry(HPmiscskills_LF,width = 5)             .grid(row=1,column=2)#.pack()
        HPmiscskills_SPD_LBL = Label(HPmiscskills_LF,text = 'Speed')        .grid(row=0,column=2)#.pack()
        HPmiscskills_HMX_BOX = Entry(HPmiscskills_LF,width = 5)             .grid(row=2,column=1)#.pack()
        HPmiscskills_HMX_LBL = Label(HPmiscskills_LF,text = 'MAX hp')        .grid(row=2,column=0)#.pack()
        HPmiscskills_HTP_BOX = Entry(HPmiscskills_LF,width = 5)             .grid(row=1,column=2)#.pack()
        HPmiscskills_HTP_LBL = Label(HPmiscskills_LF,text = 'temp HP')        .grid(row=0,column=2)#.pack()
        HPmiscskills_LF.place(x=300,y=50)

        attackplusspells_LF = LabelFrame(self.This_win,text = 'attack/magic stats')
        attackplusspells_WNM_LBL = Label(attackplusspells_LF,text = 'name') .grid(row=0,column=0)#.pack()
        attackplusspells_WN1_BOX = Entry(attackplusspells_LF,width = 7)             .grid(row=1,column=0)#.pack()
        attackplusspells_WN2_BOX = Entry(attackplusspells_LF,width = 7)             .grid(row=2,column=0)#.pack()
        attackplusspells_WN3_BOX = Entry(attackplusspells_LF,width = 7)             .grid(row=3,column=0)#.pack()
        attackplusspells_ATK_LBL = Label(attackplusspells_LF,text = 'atk bonus') .grid(row=0,column=1)#.pack()
        attackplusspells_AB1_BOX = Entry(attackplusspells_LF,width = 3)             .grid(row=1,column=1)#.pack()
        attackplusspells_AB2_BOX = Entry(attackplusspells_LF,width = 3)             .grid(row=2,column=1)#.pack()
        attackplusspells_AB3_BOX = Entry(attackplusspells_LF,width = 3)             .grid(row=3,column=1)#.pack()
        attackplusspells_DTY_LBL = Label(attackplusspells_LF,text = 'damage/type') .grid(row=0,column=2)#.pack()
        attackplusspells_DT1_BOX = Entry(attackplusspells_LF,width = 9)             .grid(row=1,column=2)#.pack()
        attackplusspells_DT2_BOX = Entry(attackplusspells_LF,width = 9)             .grid(row=2,column=2)#.pack()
        attackplusspells_DT3_BOX = Entry(attackplusspells_LF,width = 9)             .grid(row=3,column=2)#.pack()

        #add txt to fill spaces
        attackplusspells_LF.place(x=300,y=150)

        ##print(self.get_primaryattributes())
        #print(self.get_savingthrows())
        self.This_win.mainloop()
    def get_primaryattributes(self):
        return[ self.primaryattributes_STR_BOX_VAR.get(),
                self.primaryattributes_DEX_BOX_VAR.get(),
                self.primaryattributes_CON_BOX_VAR.get(),
                self.primaryattributes_INT_BOX_VAR.get(),
                self.primaryattributes_WIS_BOX_VAR.get(),
                self.primaryattributes_CHR_BOX_VAR.get()]
    def get_inspiration(self):
        return self.inspiration_STR_BOX_VAR.get()
    def get_proficiencybonus(self):
        return self.proficiencybonus_STR_BOX_VAR.get()
    def get_savingthrows(self):
        return[
            (self.savingthrows_STR_CHK_VAR.get(),self.savingthrows_STR_BOX_VAR.get()),
            (self.savingthrows_DEX_CHK_VAR.get(),self.savingthrows_DEX_BOX_VAR.get()),
            (self.savingthrows_CON_CHK_VAR.get(),self.savingthrows_CON_BOX_VAR.get()),
            (self.savingthrows_INT_CHK_VAR.get(),self.savingthrows_INT_BOX_VAR.get()),
            (self.savingthrows_WIS_CHK_VAR.get(),self.savingthrows_WIS_BOX_VAR.get()),
            (self.savingthrows_CHR_CHK_VAR.get(),self.savingthrows_CHR_BOX_VAR.get())]##return tuples of each attribute(proficient,throw)
            
            
            
            
            
            
            
#datastructs#
##heroclass##
class entity:## root class for any interaction classes
    def __init__(self):
        pass
class enemytype(entity):##enemies
    def __init__(self):
        pass
class characterhero(entity):
    def __init__(self):
        pass
class shopkeeper(entity):
    def __init__(self):
        pass
##itemclass##
class shop:
    def __init__(self):
        pass
##class person:
##    def __init__(self):
##        pass
    
    
m = main_win()

