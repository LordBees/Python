##d&d char she
import os,sys,random
from tkinter import *
from tkinter import messagebox,filedialog

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
    ##class related variables
    QS_path_currfile = ''
    ##TK start
    This_win = Tk()
    ##variables

    ##charbase_name
    charbase_name_CNM_BOX_VAR = StringVar()
    charbase_name_IRL_BOX_VAR = StringVar()
    charbase_name_CLS_BOX_VAR = StringVar()
    charbase_name_LVL_BOX_VAR = StringVar()
    charbase_name_FAC_BOX_VAR = StringVar()
    charbase_name_RAC_BOX_VAR = StringVar()
    charbase_name_EXP_BOX_VAR = StringVar()
    
    ##primary attributes
    primaryattributes_STR_BOX_VAR = StringVar()
    primaryattributes_DEX_BOX_VAR = StringVar()
    primaryattributes_CON_BOX_VAR = StringVar()
    primaryattributes_INT_BOX_VAR = StringVar()
    primaryattributes_WIS_BOX_VAR = StringVar()
    primaryattributes_CHR_BOX_VAR = StringVar()

    #roll modifier
    primaryattributes_STR_MOD_BOX_VAR = StringVar()
    primaryattributes_DEX_MOD_BOX_VAR = StringVar()
    primaryattributes_CON_MOD_BOX_VAR = StringVar()
    primaryattributes_INT_MOD_BOX_VAR = StringVar()
    primaryattributes_WIS_MOD_BOX_VAR = StringVar()
    primaryattributes_CHR_MOD_BOX_VAR = StringVar()
    
    #perception
    Perception_PER_BOX_VAR = StringVar()
    
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
    secondaryskills_ACR_CHK_VAR = IntVar()
    secondaryskills_ACR_BOX_VAR = StringVar()
    secondaryskills_ANH_CHK_VAR = IntVar()
    secondaryskills_ANH_BOX_VAR = StringVar()
    secondaryskills_ARC_CHK_VAR = IntVar()
    secondaryskills_ARC_BOX_VAR = StringVar()
    secondaryskills_ATH_CHK_VAR = IntVar()
    secondaryskills_ATH_BOX_VAR = StringVar()
    secondaryskills_DEC_CHK_VAR = IntVar()
    secondaryskills_DEC_BOX_VAR = StringVar()
    secondaryskills_HIS_CHK_VAR = IntVar()
    secondaryskills_HIS_BOX_VAR = StringVar()
    secondaryskills_CHR_CHK_VAR = IntVar()
    secondaryskills_CHR_BOX_VAR = StringVar()
    secondaryskills_IDT_CHK_VAR = IntVar()
    secondaryskills_IDT_BOX_VAR = StringVar()
    secondaryskills_INV_CHK_VAR = IntVar()
    secondaryskills_INV_BOX_VAR = StringVar()
    secondaryskills_MED_CHK_VAR = IntVar()
    secondaryskills_MED_BOX_VAR = StringVar()
    secondaryskills_NAT_CHK_VAR = IntVar()
    secondaryskills_NAT_BOX_VAR = StringVar()
    secondaryskills_PER_CHK_VAR = IntVar()
    secondaryskills_PER_BOX_VAR = StringVar()
    secondaryskills_PRF_CHK_VAR = IntVar()
    secondaryskills_PRF_BOX_VAR = StringVar()
    secondaryskills_PRS_CHK_VAR = IntVar()
    secondaryskills_PRS_BOX_VAR = StringVar()
    secondaryskills_REL_CHK_VAR = IntVar()
    secondaryskills_REL_BOX_VAR = StringVar()
    secondaryskills_SOH_CHK_VAR = IntVar()
    secondaryskills_SOH_BOX_VAR = StringVar()
    secondaryskills_STE_CHK_VAR = IntVar()
    secondaryskills_STE_BOX_VAR = StringVar()
    secondaryskills_SRV_CHK_VAR = IntVar()
    secondaryskills_SRV_BOX_VAR = StringVar()

    
    ##hpmiscskills
    HPmiscskills_AMC_BOX_VAR = StringVar()
    HPmiscskills_INI_BOX_VAR = StringVar()
    HPmiscskills_SPD_BOX_VAR = StringVar()
    HPmiscskills_HMX_BOX_VAR = StringVar()
    HPmiscskills_HTP_BOX_VAR = StringVar()
    HPmiscskills_HCR_BOX_VAR = StringVar()

    #di
    diceandsavesmisc_HTD_BOX_VAR = StringVar()
    diceandsavesmisc_DTO_BOX_VAR = StringVar()
    diceandsavesmisc_DS1_CHK_VAR = IntVar()
    diceandsavesmisc_DS2_CHK_VAR = IntVar()
    diceandsavesmisc_DS3_CHK_VAR = IntVar()
    diceandsavesmisc_DF1_CHK_VAR = IntVar()
    diceandsavesmisc_DF2_CHK_VAR = IntVar()
    diceandsavesmisc_DF3_CHK_VAR = IntVar()
    
     #attackplusspells
    attackplusspells_WN1_BOX_VAR = StringVar()
    attackplusspells_WN2_BOX_VAR = StringVar()
    attackplusspells_WN3_BOX_VAR = StringVar()
     #atk bonus
    attackplusspells_AB1_BOX_VAR = StringVar()
    attackplusspells_AB2_BOX_VAR = StringVar()
    attackplusspells_AB3_BOX_VAR = StringVar()
     #damage/type
    attackplusspells_DT1_BOX_VAR = StringVar()
    attackplusspells_DT2_BOX_VAR = StringVar()
    attackplusspells_DT3_BOX_VAR = StringVar()
    attackplusspells_MSC_TXT = StringVar()##hack for getting data out of text box(assigned as stringvar temp to ensure .get() can be found

    ##hack for getting data out of text box(assigned as stringvar temp to ensure .get() can be found before assignment
    #traits/lang box
    languagesplusskills_TBX_TXT = StringVar()
    #equip/inventory
    equipmain_TBX_TXT = StringVar()
    #traits
    personalinfo_traits_TBX_TXT = StringVar()
    personalinfo_ideals_TBX_TXT = StringVar()
    personalinfo_bonds_TBX_TXT = StringVar()
    personalinfo_flaws_TBX_TXT = StringVar()
    personalinfo_features_TBX_TXT = StringVar()

    def __init__(self):
        
        self.This_win.title('Dungeon Master v1')
        self.This_win.geometry('640x720')
        ##widgets

        ##charbase_name
        charbase_name_LF = LabelFrame(self.This_win,text = 'primary info')
        charbase_name_CNM_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_CNM_BOX_VAR).grid(row=0,column=1)
        charbase_name_CNM_LBL = Label(charbase_name_LF,text = 'character name:').grid(row=0,column=0)
        charbase_name_IRL_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_IRL_BOX_VAR).grid(row=1,column=1)
        charbase_name_IRL_LBL = Label(charbase_name_LF,text = 'player name:').grid(row=1,column=0)
        charbase_name_CLS_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_CLS_BOX_VAR).grid(row=1,column=3)
        charbase_name_CLS_LBL = Label(charbase_name_LF,text = 'player class:').grid(row=1,column=2)
        charbase_name_LVL_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_LVL_BOX_VAR).grid(row=0,column=3)
        charbase_name_LVL_LBL = Label(charbase_name_LF,text = 'player level:').grid(row=0,column=2)
        charbase_name_FAC_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_FAC_BOX_VAR).grid(row=0,column=5)
        charbase_name_FAC_LBL = Label(charbase_name_LF,text = 'player faction:').grid(row=0,column=4)
        charbase_name_RAC_BOX = Entry(charbase_name_LF,textvariable = self.charbase_name_RAC_BOX_VAR).grid(row=1,column=5)
        charbase_name_RAC_LBL = Label(charbase_name_LF,text = 'player race:').grid(row=1,column=4)
        charbase_name_EXP_BOX = Entry(charbase_name_LF,width = 5,textvariable = self.charbase_name_EXP_BOX_VAR).grid(row=0,column=7)
        charbase_name_EXP_LBL = Label(charbase_name_LF,text = 'player experience:').grid(row=0,column=6)
        
        charbase_name_LF.place(x=400,y=0)
        #primaryattributes_LF
        primaryattributes_LF = LabelFrame(self.This_win,text = 'primary\nattributes')
        primaryattributes_STR_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_STR_BOX_VAR).pack()
        primaryattributes_STR_LBL = Label(primaryattributes_LF,text = 'Strength').pack()
        primaryattributes_DEX_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_DEX_BOX_VAR).pack()
        primaryattributes_DEX_LBL = Label(primaryattributes_LF,text = 'Dexterity').pack()
        primaryattributes_CON_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_CON_BOX_VAR).pack()
        primaryattributes_CON_LBL = Label(primaryattributes_LF,text = 'Constitution').pack()
        primaryattributes_INT_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_INT_BOX_VAR).pack()
        primaryattributes_INT_LBL = Label(primaryattributes_LF,text = 'Intelligence').pack()
        primaryattributes_WIS_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_WIS_BOX_VAR).pack()
        primaryattributes_WIS_LBL = Label(primaryattributes_LF,text = 'Wisdom').pack()
        primaryattributes_CHR_BOX = Entry(primaryattributes_LF,width = 3,textvariable = self.primaryattributes_CHR_BOX_VAR).pack()
        primaryattributes_CHR_LBL = Label(primaryattributes_LF,text = 'Charisma').pack()
        primaryattributes_LF.place(x=50,y=50)##was w3

        ##roll modifier
        #primaryattributes_LF
        primaryattributes_MOD_LF = LabelFrame(self.This_win,text = 'Roll\nModifiers')
        primaryattributes_STR_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_STR_MOD_BOX_VAR).pack()
        primaryattributes_STR_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Strength').pack()
        primaryattributes_DEX_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_DEX_MOD_BOX_VAR).pack()
        primaryattributes_DEX_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Dexterity').pack()
        primaryattributes_CON_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_CON_MOD_BOX_VAR).pack()
        primaryattributes_CON_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Constitution').pack()
        primaryattributes_INT_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_INT_MOD_BOX_VAR).pack()
        primaryattributes_INT_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Intelligence').pack()
        primaryattributes_WIS_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_WIS_MOD_BOX_VAR).pack()
        primaryattributes_WIS_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Wisdom').pack()
        primaryattributes_CHR_MOD_BOX = Entry(primaryattributes_MOD_LF,width = 5,textvariable = self.primaryattributes_CHR_MOD_BOX_VAR).pack()
        primaryattributes_CHR_MOD_LBL = Label(primaryattributes_MOD_LF,text = 'Charisma').pack()
        primaryattributes_MOD_LF.place(x=125,y=50)

        ##Perception
        Perception_LF = LabelFrame(self.This_win,text = 'passive wisdom')
        Perception_PER_BOX = Entry(Perception_LF,width = 5,textvariable = self.Perception_PER_BOX_VAR).grid(row = 0,column=0)#.pack()
        Perception_PER_BOX = Label(Perception_LF,text = 'Perception').grid(row = 0,column=1)#.pack()
        Perception_LF.place(x=50,y=325)

    
        ##inspiration_LF
        inspiration_LF = LabelFrame(self.This_win,text = ' inspiration points ')
        inspiration_STR_BOX = Entry(inspiration_LF,width = 5,textvariable = self.inspiration_STR_BOX_VAR).grid(row = 0,column=1)#.pack()
        inspiration_STR_LBL = Label(inspiration_LF,text = 'inspiration            ').grid(row = 0,column=0)#.pack()
        inspiration_LF.place(x=225,y=50)

        #proficiencybonus_LF
        proficiencybonus_LF = LabelFrame(self.This_win,text = ' proficiency Bonus ')
        proficiencybonus_STR_BOX = Entry(proficiencybonus_LF,width = 5,textvariable = self.proficiencybonus_STR_BOX_VAR).grid(row = 1,column=1)#.pack()
        proficiencybonus_STR_LBL = Label(proficiencybonus_LF,text = 'Proficiency bonus').grid(row = 1,column=0)#.pack()
        proficiencybonus_LF.place(x=225,y=90)

        #savingthrows_LF
        savingthrows_LF = LabelFrame(self.This_win,text = 'Saving Throws')
        savingthrows_STR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_STR_CHK_VAR).grid(row = 0,column=0)#.pack()
        savingthrows_STR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_STR_BOX_VAR).grid(row = 0,column=1)#.pack()
        savingthrows_STR_LBL = Label(savingthrows_LF,text = 'Strength')                                     .grid(row = 0,column=2)#.pack()
        savingthrows_DEX_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_DEX_CHK_VAR).grid(row = 1,column=0)#.pack()
        savingthrows_DEX_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_DEX_BOX_VAR).grid(row = 1,column=1)#.pack()
        savingthrows_DEX_LBL = Label(savingthrows_LF,text = 'Dexterity')                                    .grid(row = 1,column=2)#.pack()
        savingthrows_CON_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CON_CHK_VAR).grid(row = 2,column=0)#.pack()
        savingthrows_CON_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CON_BOX_VAR).grid(row = 2,column=1)#.pack()
        savingthrows_CON_LBL = Label(savingthrows_LF,text = 'Constitution')                                 .grid(row = 2,column=2)#.pack()
        savingthrows_INT_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_INT_CHK_VAR).grid(row = 3,column=0)#.pack()
        savingthrows_INT_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_INT_BOX_VAR).grid(row = 3,column=1)#.pack()
        savingthrows_INT_LBL = Label(savingthrows_LF,text = 'Intelligence')                                 .grid(row = 3,column=2)#.pack()
        savingthrows_WIS_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_WIS_CHK_VAR).grid(row = 4,column=0)#.pack()
        savingthrows_WIS_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_WIS_BOX_VAR).grid(row = 4,column=1)#.pack()
        savingthrows_WIS_LBL = Label(savingthrows_LF,text = 'Wisdom')                                       .grid(row = 4,column=2)#.pack()
        savingthrows_CHR_CHK = Checkbutton(savingthrows_LF,variable =           self.savingthrows_CHR_CHK_VAR).grid(row = 5,column=0)#.pack()
        savingthrows_CHR_BOX = Entry(savingthrows_LF,width = 5,textvariable =   self.savingthrows_CHR_BOX_VAR).grid(row = 5,column=1)#.pack()
        savingthrows_CHR_LBL = Label(savingthrows_LF,text = 'Charisma')                                     .grid(row = 5,column=2)#.pack()
        savingthrows_LF.place(x=225,y=130)

        #secondaryskills_LF
        secondaryskills_LF = LabelFrame(self.This_win,text = 'skills')
        secondaryskills_ACR_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ACR_CHK_VAR).grid(row=0,column=0)#).pack(side=LEFT)
        secondaryskills_ACR_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ACR_BOX_VAR).grid(row=0,column=1)#.pack()
        secondaryskills_ACR_LBL = Label(secondaryskills_LF,text = 'acrobatics').grid(row=0,column=2)#.pack()
        secondaryskills_ANH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ANH_CHK_VAR).grid(row=1,column=0)#.pack()
        secondaryskills_ANH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ANH_BOX_VAR).grid(row=1,column=1)#.pack()
        secondaryskills_ANH_LBL = Label(secondaryskills_LF,text = 'animal handling').grid(row=1,column=2)#.pack()
        secondaryskills_ARC_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ARC_CHK_VAR).grid(row=2,column=0)#.pack()
        secondaryskills_ARC_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ARC_BOX_VAR).grid(row=2,column=1)#.pack()
        secondaryskills_ARC_LBL = Label(secondaryskills_LF,text = 'arcana').grid(row=2,column=2)#.pack()
        secondaryskills_ATH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_ATH_CHK_VAR).grid(row=3,column=0)#.pack()
        secondaryskills_ATH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_ATH_BOX_VAR).grid(row=3,column=1)#.pack()
        secondaryskills_ATH_LBL = Label(secondaryskills_LF,text = 'athletics').grid(row=3,column=2)#.pack()
        secondaryskills_DEC_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_DEC_CHK_VAR).grid(row=4,column=0)#.pack()
        secondaryskills_DEC_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_DEC_BOX_VAR).grid(row=4,column=1)#.pack()
        secondaryskills_DEC_LBL = Label(secondaryskills_LF,text = 'deception').grid(row=4,column=2)#.pack()
        secondaryskills_HIS_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_HIS_CHK_VAR).grid(row=5,column=0)#.pack()
        secondaryskills_HIS_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_HIS_BOX_VAR).grid(row=5,column=1)#.pack()
        secondaryskills_HIS_LBL = Label(secondaryskills_LF,text = 'history').grid(row=5,column=2)#.pack()
        secondaryskills_CHR_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_CHR_CHK_VAR).grid(row=6,column=0)#.pack()
        secondaryskills_CHR_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_CHR_BOX_VAR).grid(row=6,column=1)#.pack()
        secondaryskills_CHR_LBL = Label(secondaryskills_LF,text = 'insight').grid(row=6,column=2)#.pack()
        secondaryskills_IDT_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_IDT_CHK_VAR).grid(row=7,column=0)#.pack()
        secondaryskills_IDT_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_IDT_BOX_VAR).grid(row=7,column=1)#.pack()
        secondaryskills_IDT_LBL = Label(secondaryskills_LF,text = 'intimidation').grid(row=7,column=2)#.pack()
        secondaryskills_INV_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_INV_CHK_VAR).grid(row=8,column=0)#.pack()
        secondaryskills_INV_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_INV_BOX_VAR).grid(row=8,column=1)#.pack()
        secondaryskills_INV_LBL = Label(secondaryskills_LF,text = 'investigation').grid(row=8,column=2)#.pack()
        secondaryskills_MED_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_MED_CHK_VAR).grid(row=9,column=0)#.pack()
        secondaryskills_MED_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_MED_BOX_VAR).grid(row=9,column=1)#.pack()
        secondaryskills_MED_LBL = Label(secondaryskills_LF,text = 'medicine').grid(row=9,column=2)#.pack()
        secondaryskills_NAT_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_NAT_CHK_VAR).grid(row=10,column=0)#.pack()
        secondaryskills_NAT_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_NAT_BOX_VAR).grid(row=10,column=1)#.pack()
        secondaryskills_NAT_LBL = Label(secondaryskills_LF,text = 'nature').grid(row=10,column=2)#.pack()
        secondaryskills_PER_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PER_CHK_VAR).grid(row=11,column=0)#.pack()
        secondaryskills_PER_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PER_BOX_VAR).grid(row=11,column=1)#.pack()
        secondaryskills_PER_LBL = Label(secondaryskills_LF,text = 'perception').grid(row=11,column=2)#.pack()
        secondaryskills_PRF_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRF_CHK_VAR).grid(row=12,column=0)#.pack()
        secondaryskills_PRF_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRF_BOX_VAR).grid(row=12,column=1)#.pack()
        secondaryskills_PRF_LBL = Label(secondaryskills_LF,text = 'performance').grid(row=12,column=2)#.pack()
        secondaryskills_PRS_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_PRS_CHK_VAR).grid(row=13,column=0)#.pack()
        secondaryskills_PRS_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_PRS_BOX_VAR).grid(row=13,column=1)#.pack()
        secondaryskills_PRS_LBL = Label(secondaryskills_LF,text = 'persuasion').grid(row=13,column=2)#.pack()
        secondaryskills_REL_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_REL_CHK_VAR).grid(row=14,column=0)#.pack()
        secondaryskills_REL_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_REL_BOX_VAR).grid(row=14,column=1)#.pack()
        secondaryskills_REL_LBL = Label(secondaryskills_LF,text = 'religion').grid(row=14,column=2)#.pack()
        secondaryskills_SOH_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SOH_CHK_VAR).grid(row=15,column=0)#.pack()
        secondaryskills_SOH_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SOH_BOX_VAR).grid(row=15,column=1)#.pack()
        secondaryskills_SOH_LBL = Label(secondaryskills_LF,text = 'sleight of hand').grid(row=15,column=2)#.pack()
        secondaryskills_STE_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_STE_CHK_VAR).grid(row=16,column=0)#.pack()
        secondaryskills_STE_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_STE_BOX_VAR).grid(row=16,column=1)#.pack()
        secondaryskills_STE_LBL = Label(secondaryskills_LF,text = 'stealth').grid(row=16,column=2)#.pack()
        secondaryskills_SRV_CHK = Checkbutton(secondaryskills_LF,               variable = self.secondaryskills_SRV_CHK_VAR).grid(row=17,column=0)#.pack()
        secondaryskills_SRV_BOX = Entry(secondaryskills_LF,width = 5,           textvariable = self.secondaryskills_SRV_BOX_VAR).grid(row=17,column=1)#.pack()
        secondaryskills_SRV_LBL = Label(secondaryskills_LF,text = 'survival').grid(row=17,column=2)#.pack()
        secondaryskills_LF.place(x=225,y=300)        
        
        HPmiscskills_LF = LabelFrame(self.This_win,text = 'HP/misc')
        HPmiscskills_AMC_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_AMC_BOX_VAR)             .grid(row=1,column=0)#.pack()
        HPmiscskills_AMC_LBL = Label(HPmiscskills_LF,text = 'armour class') .grid(row=0,column=0)#.pack()
        HPmiscskills_INI_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_INI_BOX_VAR)             .grid(row=1,column=1)#.pack()
        HPmiscskills_INI_LBL = Label(HPmiscskills_LF,text = 'initiative')   .grid(row=0,column=1)#.pack()
        HPmiscskills_SPD_BOX = Entry(HPmiscskills_LF,width = 5,textvariable = self.HPmiscskills_SPD_BOX_VAR)             .grid(row=1,column=2)#.pack()
        HPmiscskills_SPD_LBL = Label(HPmiscskills_LF,text = 'Speed')        .grid(row=0,column=2)#.pack()
        
        HPmiscskills_HMX_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HMX_BOX_VAR)             .grid(row=4,column=1)#.pack()
        HPmiscskills_HMX_LBL = Label(HPmiscskills_LF,text = 'MAX HP')        .grid(row=4,column=0)#.pack()
        HPmiscskills_HTP_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HTP_BOX_VAR)              .grid(row=5,column=1)#.pack()
        HPmiscskills_HTP_LBL = Label(HPmiscskills_LF,text = 'temp HP')        .grid(row=5,column=0)#.pack()
        HPmiscskills_HCR_BOX = Entry(HPmiscskills_LF,width = 4,textvariable = self.HPmiscskills_HCR_BOX_VAR)              .grid(row=6,column=1)#.pack()
        HPmiscskills_HCR_LBL = Label(HPmiscskills_LF,text = 'current HP')        .grid(row=6,column=0)#.pack()
        HPmiscskills_LF.place(x=400,y=50)##was 375

        ##hitdicedeathsave
        #diceandsavesmisc
        diceandsavesmisc_LF = LabelFrame(self.This_win,text = 'dice/death saves')
        diceandsavesmisc_HTD_BOX = Entry(diceandsavesmisc_LF,width = 5,textvariable = self.diceandsavesmisc_HTD_BOX_VAR)             .grid(row=1,column=0)#.pack()
        diceandsavesmisc_HTD_LBL = Label(diceandsavesmisc_LF,text = 'hit dice') .grid(row=0,column=0)#.pack()
        diceandsavesmisc_DTO_BOX = Entry(diceandsavesmisc_LF,width = 5,textvariable = self.diceandsavesmisc_DTO_BOX_VAR)             .grid(row=3,column=0)#.pack()
        diceandsavesmisc_DTO_LBL = Label(diceandsavesmisc_LF,text = 'dice total')   .grid(row=2,column=0)#.pack()
        diceandsavesmisc_DSS_LBL = Label(diceandsavesmisc_LF,text = 'sucesses')        .grid(row=1,column=1)#.pack()
        diceandsavesmisc_DS1_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS1_CHK_VAR)        .grid(row=1,column=2)#.pack()
        diceandsavesmisc_DS2_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS2_CHK_VAR)        .grid(row=1,column=3)#.pack()
        diceandsavesmisc_DS3_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DS3_CHK_VAR)        .grid(row=1,column=4)#.pack()
        diceandsavesmisc_DSF_LBL = Label(diceandsavesmisc_LF,text = 'fails')        .grid(row=2,column=1)#.pack()
        diceandsavesmisc_DF1_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF1_CHK_VAR)        .grid(row=2,column=2)#.pack()
        diceandsavesmisc_DF2_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF2_CHK_VAR)        .grid(row=2,column=3)#.pack()
        diceandsavesmisc_DF3_CHK = Checkbutton(diceandsavesmisc_LF,variable = self.diceandsavesmisc_DF3_CHK_VAR)        .grid(row=2,column=4)#.pack()
        diceandsavesmisc_LF.place(x=400,y=175)

        
        attackplusspells_LF = LabelFrame(self.This_win,text = 'attack/magic stats')
        attackplusspells_WNM_LBL = Label(attackplusspells_LF,text = 'name') .grid(row=0,column=0)#.pack()
        attackplusspells_WN1_BOX = Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN1_BOX_VAR)             .grid(row=1,column=0)#.pack()
        attackplusspells_WN2_BOX = Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN2_BOX_VAR)             .grid(row=2,column=0)#.pack()
        attackplusspells_WN3_BOX = Entry(attackplusspells_LF,width = 7,textvariable = self.attackplusspells_WN3_BOX_VAR)             .grid(row=3,column=0)#.pack()
        attackplusspells_ATK_LBL = Label(attackplusspells_LF,text = 'atk bonus') .grid(row=0,column=1)#.pack()
        attackplusspells_AB1_BOX = Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB1_BOX_VAR)             .grid(row=1,column=1)#.pack()
        attackplusspells_AB2_BOX = Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB2_BOX_VAR)             .grid(row=2,column=1)#.pack()
        attackplusspells_AB3_BOX = Entry(attackplusspells_LF,width = 3,textvariable = self.attackplusspells_AB3_BOX_VAR)             .grid(row=3,column=1)#.pack()
        attackplusspells_DTY_LBL = Label(attackplusspells_LF,text = 'damage/type') .grid(row=0,column=2)#.pack()
        attackplusspells_DT1_BOX = Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT1_BOX_VAR)             .grid(row=1,column=2)#.pack()
        attackplusspells_DT2_BOX = Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT2_BOX_VAR)             .grid(row=2,column=2)#.pack()
        attackplusspells_DT3_BOX = Entry(attackplusspells_LF,width = 9,textvariable = self.attackplusspells_DT3_BOX_VAR)             .grid(row=3,column=2)#.pack()
        attackplusspells_NTS_LF =  LabelFrame(self.This_win,text = 'atk/mag notes')#position by magic/stats
        self.attackplusspells_MSC_TXT = Text(attackplusspells_NTS_LF,height = 25,width = 25)#add scrollbar to list
        self.attackplusspells_MSC_TXT                                                                                                .grid(row=4,column=0)#.pack() ##was height 10
        attackplusspells_NTS_LF.place(x=400,y=400)
        #add txt to fill spaces
        attackplusspells_LF.place(x=400,y=300)

        languagesplusskills_LF = LabelFrame(self.This_win,text = 'proficiencies and languages')
        self.languagesplusskills_TBX_TXT = Text(languagesplusskills_LF,height = 25,width = 25)#add scrollbar to list
        self.languagesplusskills_TBX_TXT.grid(row=0,column=0)
        #languagesplusskills_LF.place(x=0,y=0)

        equipmain_LF = LabelFrame(self.This_win,text = 'inventory')
        self.equipmain_TBX_TXT = Text(equipmain_LF,height = 25,width = 25)#add scrollbar to list
        self.equipmain_TBX_TXT.grid(row=0,column=0)
        #equipmain_LF.place(x=0,y=0)

        #personalinfo_basic
        personalinfo_traits_LF = LabelFrame(self.This_win,text = 'personality traits')
        self.personalinfo_traits_TBX_TXT = Text(personalinfo_traits_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_traits_TBX_TXT.grid(row=0,column=0)
        personalinfo_traits_LF.place(x=600,y=50)
        
        personalinfo_ideals_LF = LabelFrame(self.This_win,text = 'ideals')
        self.personalinfo_ideals_TBX_TXT = Text(personalinfo_ideals_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_ideals_TBX_TXT.grid(row=0,column=0)
        personalinfo_ideals_LF.place(x=600,y=100)
        
        personalinfo_bonds_LF = LabelFrame(self.This_win,text = 'bonds')
        self.personalinfo_bonds_TBX_TXT = Text(personalinfo_bonds_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_bonds_TBX_TXT.grid(row=0,column=0)
        personalinfo_bonds_LF.place(x=600,y=200)
        
        personalinfo_flaws_LF = LabelFrame(self.This_win,text = 'flaws')
        self.personalinfo_flaws_TBX_TXT = Text(personalinfo_flaws_LF,height = 5,width = 25)#add scrollbar to list
        self.personalinfo_flaws_TBX_TXT.grid(row=0,column=0)
        personalinfo_flaws_LF.place(x=600,y=300)

        personalinfo_features_LF = LabelFrame(self.This_win,text = 'personality traits')
        self.personalinfo_features_TBX_TXT = Text(personalinfo_features_LF,height = 25,width = 25)#add scrollbar to list
        self.personalinfo_features_TBX_TXT.grid(row=0,column=0)
        personalinfo_features_LF.place(x=825,y=50)

##        languagesplusskills_TBX_TXT
##        equipmain_TBX_TXT
##        personalinfo_traits_TBX_TXT
##        personalinfo_ideals_TBX_TXT
##        personalinfo_bonds_TBX_TXT
##        personalinfo_flaws_TBX_TXT
##        personalinfo_features_TBX_TXT

        ###print(self.get_primaryattributes())
        ##print(self.get_savingthrows())
        #print(self.attackplusspells_MSC_TXT)
        Menu_main = Menu(self.This_win)
        
        Menu_FileIO = Menu(Menu_main,tearoff = 0)
        Menu_FileIO.add_command(label="Load", command=self.sub_button_loadfile)
        Menu_FileIO.add_command(label="Save", command=self.sub_button_savefile)
        Menu_FileIO.add_command(label="Save As", command=self.sub_button_savefile_as)
        
        Menu_settings = Menu(Menu_main,tearoff = 0)
        #Menu_settings = Menu(menubar, tearoff=0)
        Menu_settings.add_command(label="dice roller", command=dicewin)
        Menu_settings.add_command(label="custom link")#, command=Menu_customchoose_window)

        Menu_main.add_cascade(label = '|File|',menu = Menu_FileIO)
        Menu_main.add_cascade(label = '|Tools|',menu = Menu_settings)
        Menu_main.add_command(label="|Options|",command = optwin)#, command=Menu_preview_window)
        Menu_main.add_command(label="|create new preset character|",command = createcharwin)#, command=Menu_preview_window)
        self.This_win.config(menu=Menu_main)#title = 'Link Roulette'
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop()
    def Alt_loop(self):
        ##additional event loop code here
        #print(self.get_attackplusspells())
        #print(self.get_secondaryskills())
        print(self.get_ALL())
        self.set_primaryattributes([random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()])
        ##end
        self.This_win.after(1500,self.Alt_loop)

    def array2csv(array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn

    def readfile(self,fname):
        try:
            f = open(fname,'r')
            data = f.readlines()
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
        return data

    def writefile(self,fname,dat,ARRAY = True):
        try:
            f = open(fname,'w')
            if ARRAY == True:
                for x in dat:
                    f.write(str(x)+'\n')
                    print('ln=',x)
            else:
                f.write(dat)
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
                
    def loadfile(self):
        pass
    def savefile(self):
        pass
    def internal_save_current(self):
        pass #self.QS_path_currfile
    def internal_loadfile(self,fname):
        pass
    def internal_savefile(self,fname,dat):
        pass
    def internal_savefileaskchecker(self):##returns name and true if file exists
        FPath = filedialog.asksaveasfilename(filetypes=(("D&D character sheet", "*.ADV"),("All Files", "*.*") ))##adv extention is forced onto ##EDIT took out this defaultextension=".ADV", 
        EXISTS_FLAG = False
        if os.path.isfile(FPath):# or os.path.isfile(FPath.strip('.ADV')):##hack to get around
            EXISTS_FLAG = True
        else:
            EXISTS_FLAG = False
        print(os.path.isfile(FPath))
        return[FPath,EXISTS_FLAG]
    
##    def internal_update_Charsheet(self,data):
##        self.set_ALL(data)
        
    
    def sub_button_loadfile(self):##load file menubutton
        FPath = filedialog.askopenfilename(defaultextension=".ADV", filetypes=(("D&D character sheet", "*.ADV"),("All Files", "*.*") ))
        dat = self.readfile(FPath)
        self.QS_path_currfile = FPath##sets var for quicksaving

    def sub_button_savefile(self):##save file menubutton
        FPath = self.QS_path_currfile
    def sub_button_savefile_as(self):
        FP = self.internal_savefileaskchecker()
        print(FP)
        if FP[1] == True:
            if messagebox.askokcancel(title = 'confirm',message = 'this will OVERWRITE the selected file with data\nare you sure?'):
                pass
            else:
                pass
        else:
            pass
        #self.internal_savefile(FP[0])
    def get_charbase_name(self):
        return[
            self.charbase_name_CNM_BOX_VAR.get(),
            self.charbase_name_IRL_BOX_VAR.get(),
            self.charbase_name_CLS_BOX_VAR.get(),
            self.charbase_name_LVL_BOX_VAR.get(),
            self.charbase_name_FAC_BOX_VAR.get(),
            self.charbase_name_RAC_BOX_VAR.get(),
            self.charbase_name_EXP_BOX_VAR.get()]
    
    def get_primaryattributes(self):
        return[ self.primaryattributes_STR_BOX_VAR.get(),
                self.primaryattributes_DEX_BOX_VAR.get(),
                self.primaryattributes_CON_BOX_VAR.get(),
                self.primaryattributes_INT_BOX_VAR.get(),
                self.primaryattributes_WIS_BOX_VAR.get(),
                self.primaryattributes_CHR_BOX_VAR.get()]

    
    def get_rollmod(self):
        return[ self.primaryattributes_STR_MOD_BOX_VAR.get(),
                self.primaryattributes_DEX_MOD_BOX_VAR.get(),
                self.primaryattributes_CON_MOD_BOX_VAR.get(),
                self.primaryattributes_INT_MOD_BOX_VAR.get(),
                self.primaryattributes_WIS_MOD_BOX_VAR.get(),
                self.primaryattributes_CHR_MOD_BOX_VAR.get()]

    def get_Perception(self):
        return self.Perception_PER_BOX_VAR.get()
    
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

    
    def get_secondaryskills(self):
        return[[
            self.secondaryskills_ACR_BOX_VAR.get(),
            self.secondaryskills_ANH_BOX_VAR.get(),
            self.secondaryskills_ARC_BOX_VAR.get(),
            self.secondaryskills_ATH_BOX_VAR.get(),
            self.secondaryskills_DEC_BOX_VAR.get(),
            self.secondaryskills_HIS_BOX_VAR.get(),
            self.secondaryskills_CHR_BOX_VAR.get(),
            self.secondaryskills_IDT_BOX_VAR.get(),
            self.secondaryskills_INV_BOX_VAR.get(),
            self.secondaryskills_MED_BOX_VAR.get(),
            self.secondaryskills_NAT_BOX_VAR.get(),
            self.secondaryskills_PER_BOX_VAR.get(),
            self.secondaryskills_PRF_BOX_VAR.get(),
            self.secondaryskills_PRS_BOX_VAR.get(),
            self.secondaryskills_REL_BOX_VAR.get(),
            self.secondaryskills_SOH_BOX_VAR.get(),
            self.secondaryskills_STE_BOX_VAR.get(),
            self.secondaryskills_SRV_BOX_VAR.get(),
            ],[
            self.secondaryskills_ACR_CHK_VAR.get(),
            self.secondaryskills_ANH_CHK_VAR.get(),
            self.secondaryskills_ARC_CHK_VAR.get(),
            self.secondaryskills_ATH_CHK_VAR.get(),
            self.secondaryskills_DEC_CHK_VAR.get(),
            self.secondaryskills_HIS_CHK_VAR.get(),
            self.secondaryskills_CHR_CHK_VAR.get(),
            self.secondaryskills_IDT_CHK_VAR.get(),
            self.secondaryskills_INV_CHK_VAR.get(),
            self.secondaryskills_MED_CHK_VAR.get(),
            self.secondaryskills_NAT_CHK_VAR.get(),
            self.secondaryskills_PER_CHK_VAR.get(),
            self.secondaryskills_PRF_CHK_VAR.get(),
            self.secondaryskills_PRS_CHK_VAR.get(),
            self.secondaryskills_REL_CHK_VAR.get(),
            self.secondaryskills_SOH_CHK_VAR.get(),
            self.secondaryskills_STE_CHK_VAR.get(),
            self.secondaryskills_SRV_CHK_VAR.get()]]
            
    def get_hpmiscskills(self):
        ##hpmiscskills
        return[
        self.HPmiscskills_AMC_BOX_VAR.get(),
        self.HPmiscskills_INI_BOX_VAR.get(),
        self.HPmiscskills_SPD_BOX_VAR.get(),
        self.HPmiscskills_HMX_BOX_VAR.get(),
        self.HPmiscskills_HTP_BOX_VAR.get(),
        self.HPmiscskills_HCR_BOX_VAR.get()]


    def get_diceandsavesmisc(self):
        #di
        return[
        self.diceandsavesmisc_HTD_BOX_VAR.get(),
        self.diceandsavesmisc_DTO_BOX_VAR.get(),
        self.diceandsavesmisc_DS1_CHK_VAR.get(),
        self.diceandsavesmisc_DS2_CHK_VAR.get(),
        self.diceandsavesmisc_DS3_CHK_VAR.get(),
        self.diceandsavesmisc_DF1_CHK_VAR.get(),
        self.diceandsavesmisc_DF2_CHK_VAR.get(),
        self.diceandsavesmisc_DF3_CHK_VAR.get()]

    
    def get_attackplusspells_VAR(self):#[weaps/notes][data][weapno]
                                       #weapno
                                       #1=name
                                       #2=attack bonus
                                       #3=damagetype
        return[
        ##name
            [
                self.attackplusspells_WN1_BOX_VAR.get(),
                self.attackplusspells_WN2_BOX_VAR.get(),
                self.attackplusspells_WN3_BOX_VAR.get()
            ],
        ##atk bonus
            [
                self.attackplusspells_AB1_BOX_VAR.get(),
                self.attackplusspells_AB2_BOX_VAR.get(),
                self.attackplusspells_AB3_BOX_VAR.get()
            ],
        ##damage/type
            [
                self.attackplusspells_DT1_BOX_VAR.get(),
                self.attackplusspells_DT2_BOX_VAR.get(),
                self.attackplusspells_DT3_BOX_VAR.get()
            ]]
        #text hack
        #self.attackplusspells_MSC_TXT
    def get_attackplusspells_TXT(self):
        #text hack
        return self.attackplusspells_MSC_TXT.get(1.0, 'end-1c')##char1 2 end
    def get_attackplusspells(self):
        return [self.get_attackplusspells_VAR(),self.get_attackplusspells_TXT()]
    #text boxes additionally need to be added
    def get_ALL(self):
        return[
        self.get_charbase_name(),
        self.get_primaryattributes(),
        self.get_rollmod(),
        self.get_Perception(),
        self.get_inspiration(),
        self.get_proficiencybonus(),
        self.get_savingthrows(),
        self.get_secondaryskills(),
        self.get_hpmiscskills(),
        self.get_diceandsavesmisc(),
        self.get_attackplusspells()]
        #add txt boxes


    ##SETTING DATA
    #base stats
    def set_charbase_name(self,data):
        self.charbase_name_CNM_BOX_VAR.set(data[0])
        self.charbase_name_IRL_BOX_VAR.set(data[1])
        self.charbase_name_CLS_BOX_VAR.set(data[2])
        self.charbase_name_LVL_BOX_VAR.set(data[3])
        self.charbase_name_FAC_BOX_VAR.set(data[4])
        self.charbase_name_RAC_BOX_VAR.set(data[5])
        self.charbase_name_EXP_BOX_VAR.set(data[6])
    #primaryattributes
    def set_primaryattributes(self,data):
        self.primaryattributes_STR_BOX_VAR.set(data[0])
        self.primaryattributes_DEX_BOX_VAR.set(data[1])
        self.primaryattributes_CON_BOX_VAR.set(data[2])
        self.primaryattributes_INT_BOX_VAR.set(data[3])
        self.primaryattributes_WIS_BOX_VAR.set(data[4])
        self.primaryattributes_CHR_BOX_VAR.set(data[5])

    #rollmod
    def set_rollmod(self,data):
        self.primaryattributes_STR_MOD_BOX_VAR.set(data[0])
        self.primaryattributes_DEX_MOD_BOX_VAR.set(data[1])
        self.primaryattributes_CON_MOD_BOX_VAR.set(data[2])
        self.primaryattributes_INT_MOD_BOX_VAR.set(data[3])
        self.primaryattributes_WIS_MOD_BOX_VAR.set(data[4])
        self.primaryattributes_CHR_MOD_BOX_VAR.set(data[5])

    #perception
    def set_Perception(self,data):
        self.Perception_PER_BOX.set(data[0])

    #inspiration
    def set_inspiration(self,data):
        self.inspiration_STR_BOX_VAR.set(data[0])

    # proviciency bonus
    def set_proficiencybonus(self,data):
        self.proficiencybonus_STR_BOX_VAR.set(data[0])

    #saving throws
    def set_savingthrows(self,data):
        self.savingthrows_STR_BOX_VAR.set(data[0][0])
        self.savingthrows_DEX_BOX_VAR.set(data[0][1])
        self.savingthrows_CON_BOX_VAR.set(data[0][2])
        self.savingthrows_INT_BOX_VAR.set(data[0][3])
        self.savingthrows_WIS_BOX_VAR.set(data[0][4])
        self.savingthrows_CHR_BOX_VAR.set(data[0][5])
        
        self.savingthrows_STR_CHK_VAR.set(data[1][0])
        self.savingthrows_DEX_CHK_VAR.set(data[1][1])
        self.savingthrows_CON_CHK_VAR.set(data[1][2])
        self.savingthrows_INT_CHK_VAR.set(data[1][3])
        self.savingthrows_WIS_CHK_VAR.set(data[1][4])
        self.savingthrows_CHR_CHK_VAR.set(data[1][5])

    #secondary stats
    def set_secondaryskills(self,data):#[boxdata/checkboxdata][data]
        self.secondaryskills_ACR_BOX_VAR.set(data[0][0])
        self.secondaryskills_ANH_BOX_VAR.set(data[0][1])
        self.secondaryskills_ARC_BOX_VAR.set(data[0][2])
        self.secondaryskills_ATH_BOX_VAR.set(data[0][3])
        self.secondaryskills_DEC_BOX_VAR.set(data[0][4])
        self.secondaryskills_HIS_BOX_VAR.set(data[0][5])
        self.secondaryskills_CHR_BOX_VAR.set(data[0][6])
        self.secondaryskills_IDT_BOX_VAR.set(data[0][7])
        self.secondaryskills_INV_BOX_VAR.set(data[0][8])
        self.secondaryskills_MED_BOX_VAR.set(data[0][9])
        self.secondaryskills_NAT_BOX_VAR.set(data[0][10])
        self.secondaryskills_PER_BOX_VAR.set(data[0][11])
        self.secondaryskills_PRF_BOX_VAR.set(data[0][12])
        self.secondaryskills_PRS_BOX_VAR.set(data[0][13])
        self.secondaryskills_REL_BOX_VAR.set(data[0][14])
        self.secondaryskills_SOH_BOX_VAR.set(data[0][15])
        self.secondaryskills_STE_BOX_VAR.set(data[0][16])
        self.secondaryskills_SRV_BOX_VAR.set(data[0][17])
        
        self.secondaryskills_ACR_CHK_VAR.set(data[1][0])
        self.secondaryskills_ANH_CHK_VAR.set(data[1][1])
        self.secondaryskills_ARC_CHK_VAR.set(data[1][2])
        self.secondaryskills_ATH_CHK_VAR.set(data[1][3])
        self.secondaryskills_DEC_CHK_VAR.set(data[1][4])
        self.secondaryskills_HIS_CHK_VAR.set(data[1][5])
        self.secondaryskills_CHR_CHK_VAR.set(data[1][6])
        self.secondaryskills_IDT_CHK_VAR.set(data[1][7])
        self.secondaryskills_INV_CHK_VAR.set(data[1][8])
        self.secondaryskills_MED_CHK_VAR.set(data[1][9])
        self.secondaryskills_NAT_CHK_VAR.set(data[1][10])
        self.secondaryskills_PER_CHK_VAR.set(data[1][11])
        self.secondaryskills_PRF_CHK_VAR.set(data[1][12])
        self.secondaryskills_PRS_CHK_VAR.set(data[1][13])
        self.secondaryskills_REL_CHK_VAR.set(data[1][14])
        self.secondaryskills_SOH_CHK_VAR.set(data[1][15])
        self.secondaryskills_STE_CHK_VAR.set(data[1][16])
        self.secondaryskills_SRV_CHK_VAR.set(data[1][17])

    def set_hpmiscskills(self,data):
        ##hpmiscskills
        self.HPmiscskills_AMC_BOX_VAR.set(data[0])
        self.HPmiscskills_INI_BOX_VAR.set(data[1])
        self.HPmiscskills_SPD_BOX_VAR.set(data[2])
        self.HPmiscskills_HMX_BOX_VAR.set(data[3])
        self.HPmiscskills_HTP_BOX_VAR.set(data[4])
        self.HPmiscskills_HCR_BOX_VAR.set(data[5])


    def set_diceandsavesmisc(self,data):
        #di
        self.diceandsavesmisc_HTD_BOX_VAR.set(data[0])
        self.diceandsavesmisc_DTO_BOX_VAR.set(data[1])
        self.diceandsavesmisc_DS1_CHK_VAR.set(data[2])
        self.diceandsavesmisc_DS2_CHK_VAR.set(data[3])
        self.diceandsavesmisc_DS3_CHK_VAR.set(data[4])
        self.diceandsavesmisc_DF1_CHK_VAR.set(data[5])
        self.diceandsavesmisc_DF2_CHK_VAR.set(data[6])
        self.diceandsavesmisc_DF3_CHK_VAR.set(data[7])

    
    def set_attackplusspells_VAR(self,data):#[weaps/notes][data][weapno]
                                       #weapno
                                       #1=name
                                       #2=attack bonus
                                       #3=damagetype
        ##name
                self.attackplusspells_WN1_BOX_VAR.set(data[0][0])
                self.attackplusspells_WN2_BOX_VAR.set(data[0][1])
                self.attackplusspells_WN3_BOX_VAR.set(data[0][2])
                
        ##atk bonus
                self.attackplusspells_AB1_BOX_VAR.set(data[1][0])
                self.attackplusspells_AB2_BOX_VAR.set(data[1][1])
                self.attackplusspells_AB3_BOX_VAR.set(data[1][2])

        ##damage/type
                self.attackplusspells_DT1_BOX_VAR.set(data[2][0])
                self.attackplusspells_DT2_BOX_VAR.set(data[2][1])
                self.attackplusspells_DT3_BOX_VAR.set(data[2][2])
        #text hack
        #self.attackplusspells_MSC_TXT
    def set_attackplusspells_TXT(self,data):
        #text hack
        return self.attackplusspells_MSC_TXT.set(data[0])##char1 2 end
    def set_attackplusspells(self,data):
        return [self.set_attackplusspells_VAR(data[0]),self.set_attackplusspells_TXT(data[1])]
    #text boxes additionally need to be added
    
    def set_ALL(self,data):
        self.set_charbase_name(data[0])
        self.set_primaryattributes(data[1])
        self.set_rollmod(data[2])
        self.set_Perception(data[3])
        self.set_inspiration(data[4])
        self.set_proficiencybonus(data[5])
        self.set_savingthrows(data[6])
        self.set_secondaryskills(data[7])
        self.set_hpmiscskills(data[8])
        self.set_diceandsavesmisc(data[9])
        self.set_attackplusspells(data[10])
        #add txt boxes
    def get_a():
        pass
            
            
class dicewin:
    #This_win = Toplevel
    #print('init')
    ##variables
    Diceroller_DX1_RAD_VAR = IntVar()#StringVar()
    Diceroller_RDR_LBL_VAR = StringVar()
    
    def __init__(self):
        #self.This_win = Toplevel()##minus the ()?
        self.This_win = Toplevel()
        self.This_win.title('Dice roller')
        self.This_win.geometry('450x200')
        ##widgets
        Diceroller_LF = LabelFrame(self.This_win)
        Diceroller_DXX_LBL = Label(Diceroller_LF,text = 'select a dice').grid(row=0,column=0)
        Diceroller_DX1_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 4,text = 'D4').grid(row=1,column=0)##dicetypes
        Diceroller_DX2_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 8,text = 'D8').grid(row=1,column=1)
        Diceroller_DX3_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 6,text = 'D6').grid(row=1,column=2)
        Diceroller_DX4_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 12,text = 'D12').grid(row=1,column=3)
        Diceroller_DX5_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 10,text = 'D10').grid(row=1,column=4)
        Diceroller_DX6_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 100,text = 'D100').grid(row=1,column=5)
        Diceroller_DX7_RAD = Radiobutton(Diceroller_LF,variable = self.Diceroller_DX1_RAD_VAR,value = 20,text = 'D20').grid(row=1,column=6)
        Diceroller_RTD_BTN = Button(Diceroller_LF,text = 'Roll!',command = self.roll_die).grid(row=2,column=0)
        Diceroller_RDR_LBL = Label(Diceroller_LF,textvariable = self.Diceroller_RDR_LBL_VAR,text = 'you rolled a |').grid(row=2,column=1)
        Diceroller_LF.place(x=50,y=50)
        
        ## post widget code
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop() 
        

    def Alt_loop(self):
        ##additional event loop code here
        print(self.get_diceroller())
        ##end
        self.This_win.after(1500,self.Alt_loop)

    def roll_die(self):##maybe problem
        d = self.get_diceroller()
        r = 0##random roll
        if str(d) == '100':
            r= (self.internal_roller(10)*10)
        elif str(d) == '0':
            r = 'No dice Selected!'
        else:
            r= self.internal_roller(int(d))
        self.set_rollerlabel(r)
        
    def internal_roller(self,number):
        return random.randint(0,number)
    def get_diceroller(self):
        return self.Diceroller_DX1_RAD_VAR.get()
    def set_rollerlabel(self,data):
        self.Diceroller_RDR_LBL_VAR.set('you rolled a |'+str(data))
class createcharwin(main_win):
    def __init__(self):
        self.This_win = Toplevel()
        self.This_win.title('Character Creation Setup')
        self.This_win.geometry('640x720')
        ##widgets
        
        ## post widget code
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop() 
        

    def Alt_loop(self):
        ##additional event loop code here

        ##end
        self.This_win.after(1500,self.Alt_loop)

class optwin:
    def __init__(self):
        self.This_win = Toplevel()
        self.This_win.title('Options Menu')
        self.This_win.geometry('600x200')
        ##widgets
        
        ## post widget code
        self.This_win.after(1500,self.Alt_loop)
        self.This_win.mainloop() 
        

    def Alt_loop(self):
        ##additional event loop code here

        ##end
        self.This_win.after(1500,self.Alt_loop)
        
class fileIO:##unused atm
    Dat_Main_Path = '' 
            
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

