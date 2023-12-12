import random
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Dungeons and Dragons 5e Calculators")
window.minsize()

fontObj = tkFont.Font(size=11)
mainFrame = ttk.Frame(window,borderwidth=10)
titleFrame = ttk.Frame(mainFrame,borderwidth=10)
label = ttk.Label(titleFrame,text="Attack Average Damage Per Round Calculator", font=fontObj)

#Attack Roll Stuff

frameTop = ttk.Frame(mainFrame, borderwidth=10)
attackRoll = ttk.Label(frameTop,text="Attack Bonus")
initAttackVariable = tk.IntVar()
initAttackVariable.set(0)
aRollEntry = ttk.Entry(frameTop, text=initAttackVariable, width=5)

targetAC = ttk.Label(frameTop,text="Target AC")
initACVariable = tk.IntVar()
initACVariable.set(0)
acEntry = ttk.Entry(frameTop, text=initACVariable,width=5)

numOfAttacks = ttk.Label(frameTop, text="Number of Attacks")
initNumAttackVariable = tk.IntVar()
initNumAttackVariable.set(0)
numOfAttacksEntry = ttk.Entry(frameTop, width=5, text=initNumAttackVariable)

criticalNum = ttk.Label(frameTop, text="Dice Roll for Crit")
critVar = tk.IntVar()
critVar.set(20)
criticalNumEntry = ttk.OptionMenu(frameTop, critVar, 20, 20, 19, 18)


#Damage Die

bigFrameDice = ttk.Frame(mainFrame,borderwidth=10)
frameDice = ttk.Frame(bigFrameDice,borderwidth=10)

damageDie = ttk.Label(frameDice,text="Damage Dice for Normal Attacks")

frameDamageDie = ttk.Frame(frameDice, borderwidth=10)
initOneD4Variable = tk.IntVar()
initOneD4Variable.set(0)
damageDieD4 = ttk.Entry(frameDamageDie,width=2, text=initOneD4Variable)
d4Label = ttk.Label(frameDamageDie,text="d4")

initOneD6Variable = tk.IntVar()
initOneD6Variable.set(0)
damageDieD6 = ttk.Entry(frameDamageDie,width=2, text=initOneD6Variable)
d6Label = ttk.Label(frameDamageDie,text="d6")

initOneD8Variable = tk.IntVar()
initOneD8Variable.set(0)
damageDieD8 = ttk.Entry(frameDamageDie,width=2, text=initOneD8Variable)
d8Label = ttk.Label(frameDamageDie,text="d8")

initOneD10Variable = tk.IntVar()
initOneD10Variable.set(0)
damageDieD10 = ttk.Entry(frameDamageDie,width=2, text=initOneD10Variable)
d10Label = ttk.Label(frameDamageDie,text="d10")

initOneD12Variable = tk.IntVar()
initOneD12Variable.set(0)
damageDieD12 = ttk.Entry(frameDamageDie,width=2, text=initOneD12Variable)
d12Label = ttk.Label(frameDamageDie,text="d12")

adDamageLabel = ttk.Label(frameDamageDie,text="Fixed Damage")
initFixVariable = tk.IntVar()
initFixVariable.set(0)
adFixedDamage = ttk.Entry(frameDamageDie,width=5, text=initFixVariable)

#Normal Extra Damage

extraDamageDie = ttk.Label(frameDice,text="Damage Dice on First Hit (ex. Sneak Attack/Divine Smite)")

frameExtraDie = ttk.Frame(frameDice, borderwidth=10)

initExD4Variable = tk.IntVar()
initExD4Variable.set(0)
extraDieD4 = ttk.Entry(frameExtraDie,width=2, text=initExD4Variable)
extraD4Label = ttk.Label(frameExtraDie,text="d4")

initExD6Variable = tk.IntVar()
initExD6Variable.set(0)
extraDieD6 = ttk.Entry(frameExtraDie,width=2, text=initExD6Variable)
extraD6Label = ttk.Label(frameExtraDie,text="d6")

initExD8Variable = tk.IntVar()
initExD8Variable.set(0)
extraDieD8 = ttk.Entry(frameExtraDie,width=2, text=initExD8Variable)
extraD8Label = ttk.Label(frameExtraDie,text="d8")

initExD10Variable = tk.IntVar()
initExD10Variable.set(0)
extraDieD10 = ttk.Entry(frameExtraDie,width=2, text=initExD10Variable)
extraD10Label = ttk.Label(frameExtraDie,text="d10")

initExD12Variable = tk.IntVar()
initExD12Variable.set(0)
extraDieD12 = ttk.Entry(frameExtraDie,width=2, text=initExD12Variable)
extraD12Label = ttk.Label(frameExtraDie,text="d12")

extraDamageLabel = ttk.Label(frameExtraDie,text="Fixed Damage")
initExFixVariable = tk.IntVar()
initExFixVariable.set(0)
extraFixedDamage = ttk.Entry(frameExtraDie,width=5, text=initExFixVariable)

#Crit Extra Damage

critDamageDie = ttk.Label(frameDice,text="Extra Damage Dice on Critical Hit")

frameCritDie = ttk.Frame(frameDice, borderwidth=10)

initCritD4Variable = tk.IntVar()
initCritD4Variable.set(0)
critDieD4 = ttk.Entry(frameCritDie,width=2, text=initCritD4Variable)
critD4Label = ttk.Label(frameCritDie,text="d4")

initCritD6Variable = tk.IntVar()
initCritD6Variable.set(0)
critDieD6 = ttk.Entry(frameCritDie,width=2, text=initCritD6Variable)
critD6Label = ttk.Label(frameCritDie,text="d6")

initCritD8Variable = tk.IntVar()
initCritD8Variable.set(0)
critDieD8 = ttk.Entry(frameCritDie,width=2, text=initCritD8Variable)
critD8Label = ttk.Label(frameCritDie,text="d8")

initCritD10Variable = tk.IntVar()
initCritD10Variable.set(0)
critDieD10 = ttk.Entry(frameCritDie,width=2, text=initCritD10Variable)
critD10Label = ttk.Label(frameCritDie,text="d10")

initCritD12Variable = tk.IntVar()
initCritD12Variable.set(0)
critDieD12 = ttk.Entry(frameCritDie,width=2, text=initCritD12Variable)
critD12Label = ttk.Label(frameCritDie,text="d12")

critDamageLabel = ttk.Label(frameCritDie,text="Fixed Damage")
initCritFixVariable = tk.IntVar()
initCritFixVariable.set(0)
critFixedDamage = ttk.Entry(frameCritDie,width=5, text=initCritFixVariable)


#Bonus Attack Roll Stuff

bonusAttackFrame=ttk.Frame(bigFrameDice, borderwidth=20)
bonusFrameTop = ttk.Frame(mainFrame, borderwidth=20)

bonusAttackRoll = ttk.Label(bonusFrameTop,text="Bonus Action Attack Bonus")
initBonusAttackVariable = tk.IntVar()
initBonusAttackVariable.set(0)
bonusAttackRollEntry = ttk.Entry(bonusFrameTop, width=5, text=initBonusAttackVariable)

numOfBonusAttacks = ttk.Label(bonusFrameTop, text="Number of Bonus Action Attacks")
initNumBonAttackVariable = tk.IntVar()
initNumBonAttackVariable.set(0)
numOfBonusAttacksEntry = ttk.Entry(bonusFrameTop, width=5, text=initNumBonAttackVariable)

#Bonus Damage Die

bonusFrameDice = ttk.Frame(bonusAttackFrame,borderwidth=10)

bonusDamageDie = ttk.Label(bonusFrameDice,text="Damage Dice for Bonus Action Attacks")

bonusFrameDamageDie = ttk.Frame(bonusFrameDice, borderwidth=10)
initBonD4Variable = tk.IntVar()
initBonD4Variable.set(0)
bonusDamageDieD4 = ttk.Entry(bonusFrameDamageDie,width=2, text=initBonD4Variable)
bonusD4Label = ttk.Label(bonusFrameDamageDie,text="d4")

initBonD6Variable = tk.IntVar()
initBonD6Variable.set(0)
bonusDamageDieD6 = ttk.Entry(bonusFrameDamageDie,width=2, text=initBonD6Variable)
bonusD6Label = ttk.Label(bonusFrameDamageDie,text="d6")

initBonD8Variable = tk.IntVar()
initBonD8Variable.set(0)
bonusDamageDieD8 = ttk.Entry(bonusFrameDamageDie,width=2, text=initBonD8Variable)
bonusD8Label = ttk.Label(bonusFrameDamageDie,text="d8")

initBonD10Variable = tk.IntVar()
initBonD10Variable.set(0)
bonusDamageDieD10 = ttk.Entry(bonusFrameDamageDie,width=2, text=initBonD10Variable)
bonusD10Label = ttk.Label(bonusFrameDamageDie,text="d10")

initBonD12Variable = tk.IntVar()
initBonD12Variable.set(0)
bonusDamageDieD12 = ttk.Entry(bonusFrameDamageDie,width=2, text=initBonD12Variable)
bonusD12Label = ttk.Label(bonusFrameDamageDie,text="d12")

bonusAdDamageLabel = ttk.Label(bonusFrameDamageDie,text="Fixed Damage")
initBonFixVariable = tk.IntVar()
initBonFixVariable.set(0)
bonusAdFixedDamage = ttk.Entry(bonusFrameDamageDie,width=5, text=initBonFixVariable)

"""
#Bonus Extra Damage

bonusExtraDamageDie = ttk.Label(bonusFrameDice,text="Damage Dice on Bonus Action Hit (ex. Sneak Attack/Divine Smite)")

bonusFrameExtraDie = ttk.Frame(bonusFrameDice, borderwidth=10)

initBonExD4Variable = tk.IntVar()
initBonExD4Variable.set(0)
bonusExtraDieD4 = ttk.Entry(bonusFrameExtraDie,width=2, text=initBonExD4Variable)
bonusExtraD4Label = ttk.Label(bonusFrameExtraDie,text="d4")

initBonExD6Variable = tk.IntVar()
initBonExD6Variable.set(0)
bonusExtraDieD6 = ttk.Entry(bonusFrameExtraDie,width=2, text=initBonExD6Variable)
bonusExtraD6Label = ttk.Label(bonusFrameExtraDie,text="d6")

initBonExD8Variable = tk.IntVar()
initBonExD8Variable.set(0)
bonusExtraDieD8 = ttk.Entry(bonusFrameExtraDie,width=2, text=initBonExD8Variable)
bonusExtraD8Label = ttk.Label(bonusFrameExtraDie,text="d8")

initBonExD10Variable = tk.IntVar()
initBonExD10Variable.set(0)
bonusExtraDieD10 = ttk.Entry(bonusFrameExtraDie,width=2, text=initBonExD10Variable)
bonusExtraD10Label = ttk.Label(bonusFrameExtraDie,text="d10")

initBonExD12Variable = tk.IntVar()
initBonExD12Variable.set(0)
bonusExtraDieD12 = ttk.Entry(bonusFrameExtraDie,width=2, text=initBonExD12Variable)
bonusExtraD12Label = ttk.Label(bonusFrameExtraDie,text="d12")

bonusExtraDamageLabel = ttk.Label(bonusFrameExtraDie,text="Fixed Damage")
initBonExFixVariable = tk.IntVar()
initBonExFixVariable.set(0)
bonusExtraFixedDamage = ttk.Entry(bonusFrameExtraDie,width=5, text=initBonExFixVariable)

"""

#Bonus Crit Extra Damage

bonusCritDamageDie = ttk.Label(bonusFrameDice,text="Extra Damage Dice on Critical Hit for Bonus Attack")

bonusFrameCritDie = ttk.Frame(bonusFrameDice, borderwidth=10)

initBonCritD4Variable = tk.IntVar()
initBonCritD4Variable.set(0)
bonusCritDieD4 = ttk.Entry(bonusFrameCritDie,width=2, text=initBonCritD4Variable)
bonusCritD4Label = ttk.Label(bonusFrameCritDie,text="d4")

initBonCritD6Variable = tk.IntVar()
initBonCritD6Variable.set(0)
bonusCritDieD6 = ttk.Entry(bonusFrameCritDie,width=2, text=initBonCritD6Variable)
bonusCritD6Label = ttk.Label(bonusFrameCritDie,text="d6")

initBonCritD8Variable = tk.IntVar()
initBonCritD8Variable.set(0)
bonusCritDieD8 = ttk.Entry(bonusFrameCritDie,width=2, text=initBonCritD8Variable)
bonusCritD8Label = ttk.Label(bonusFrameCritDie,text="d8")

initBonCritD10Variable = tk.IntVar()
initBonCritD10Variable.set(0)
bonusCritDieD10 = ttk.Entry(bonusFrameCritDie,width=2, text=initBonCritD10Variable)
bonusCritD10Label = ttk.Label(bonusFrameCritDie,text="d10")

initBonCritD12Variable = tk.IntVar()
initBonCritD12Variable.set(0)
bonusCritDieD12 = ttk.Entry(bonusFrameCritDie,width=2, text=initBonCritD12Variable)
bonusCritD12Label = ttk.Label(bonusFrameCritDie,text="d12")

bonusCritDamageLabel = ttk.Label(bonusFrameCritDie,text="Fixed Damage")
initBonCritFixVariable = tk.IntVar()
initBonCritFixVariable.set(0)
bonusCritFixedDamage = ttk.Entry(bonusFrameCritDie,width=5, text=initBonCritFixVariable)

displayAnswer = tk.Label(mainFrame,text="",font=fontObj)


#functions

def callbackCritEntry():
    pass

def attackProb():
    try:
        probability = (21 - int(acEntry.get()) + int(aRollEntry.get()))/20
        return probability
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)


def criticalHitProb():
    return (21 - int(critVar.get()))/20


def damagePerHit():
    try:
        regDamageDie = {"d4":int(damageDieD4.get()),"d6":int(damageDieD6.get()),"d8":int(damageDieD8.get()),"d10":int(damageDieD10.get()),"d12":int(damageDieD12.get())}
        regDamage = {}
        for i in regDamageDie:
            if regDamageDie[i] > 0:
                regDamage[i] = regDamageDie[i]
        avgDamage = 0
        for i in regDamage:
            if i == "d4":
                avgDamage += regDamage[i] * (2.5)
            elif i == "d6":
                avgDamage += regDamage[i] * (3.5)
            elif i == "d8":
                avgDamage += regDamage[i] * (4.5)
            elif i == "d10":
                avgDamage += regDamage[i] * (5.5)
            elif i == "d12":
                avgDamage += regDamage[i] * (6.5)
        avgDamage += int(adFixedDamage.get()) + int(extraFixedDamage.get())
        return avgDamage
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)

def damagePerCrit():
    try:
        normalDamage = damagePerHit() - (int(adFixedDamage.get()))
        normalDamage = (2 * normalDamage) + (int(adFixedDamage.get()))
        critDamageDie = {"d4":int(critDieD4.get()),"d6":int(critDieD6.get()),"d8":int(critDieD8.get()),"d10":int(critDieD10.get()),"d12":int(critDieD12.get())}
        critDamage = {}
        for i in critDamageDie:
            if critDamageDie[i] > 0:
                critDamage[i] = critDamageDie[i]
        for i in critDamage:
            if i == "d4":
                normalDamage += critDamage[i] * (2.5)
            elif i == "d6":
                normalDamage += critDamage[i] * (3.5)
            elif i == "d8":
                normalDamage += critDamage[i] * (4.5)
            elif i == "d10":
                normalDamage += critDamage[i] * (5.5)
            elif i == "d12":
                normalDamage += critDamage[i] * (6.5)
        normalDamage += int(critFixedDamage.get())
        displayAnswer.config(text=normalDamage)
        return normalDamage
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)

def bonusAttackProb():
    try:
        bonusProbability = (21 - int(acEntry.get()) + int(bonusAttackRollEntry.get()))/20
        return bonusProbability
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)

def damagePerExtra():
    try:
        extDamageDie = {"d4":int(extraDieD4.get()),"d6":int(extraDieD6.get()),"d8":int(extraDieD8.get()),"d10":int(extraDieD10.get()),"d12":int(extraDieD12.get())}
        extDamage = {}
        for i in extDamageDie:
            if extDamageDie[i] > 0:
                extDamage[i] = extDamageDie[i]
        avgDamage = 0
        for i in extDamage:
            if i == "d4":
                avgDamage += extDamage[i] * (2.5)
            elif i == "d6":
                avgDamage += extDamage[i] * (3.5)
            elif i == "d8":
                avgDamage += extDamage[i] * (4.5)
            elif i == "d10":
                avgDamage += extDamage[i] * (5.5)
            elif i == "d12":
                avgDamage += extDamage[i] * (6.5)
        probAttack = (1 - int(attackProb())**(int(numOfAttacksEntry.get())))
        probBonusA = (1 - int(bonusAttackProb())**((int(numOfBonusAttacksEntry.get()))))
        if bonusAttackProb() > 0 or numOfBonusAttacksEntry.get() > 0:
            probOneHit = 1 - (probAttack * probBonusA)
        else:
            probOneHit = 1 - probAttack
        critDamage = avgDamage * 2
        critDamage += int(extraFixedDamage.get())
        avgDamage += int(extraFixedDamage.get())
        firstPart = attackProb() * avgDamage
        secondPart = ((attackProb()-criticalHitProb()) * (criticalHitProb()/attackProb())) * critDamage
        thirdPart = ((1-attackProb())*(bonusAttackProb()-criticalHitProb()) * (criticalHitProb()/bonusAttackProb()) * critDamage)
        fullDamage = firstPart + secondPart + thirdPart
        return fullDamage
    except:
        pass

def damagePerBonusHit():
    try:
        bonusDamageDie = {"d4":int(bonusDamageDieD4.get()),"d6":int(bonusDamageDieD6.get()),"d8":int(bonusDamageDieD8.get()),"d10":int(bonusDamageDieD10.get()),"d12":int(bonusDamageDieD12.get())}
        bonusDamage = {}
        for i in bonusDamageDie:
            if bonusDamageDie[i] > 0:
                bonusDamage[i] = bonusDamageDie[i]
        avgBonusDamage = 0
        for i in bonusDamage:
            if i == "d4":
                avgBonusDamage += bonusDamage[i] * (2.5)
            elif i == "d6":
                avgBonusDamage += bonusDamage[i] * (3.5)
            elif i == "d8":
                avgBonusDamage += bonusDamage[i] * (4.5)
            elif i == "d10":
                avgBonusDamage += bonusDamage[i] * (5.5)
            elif i == "d12":
                avgBonusDamage += bonusDamage[i] * (6.5)
        avgBonusDamage += int(bonusAdFixedDamage.get())
        return avgBonusDamage
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)

def damagePerBonusCrit():
    try:
        normalBonusDamage = damagePerBonusHit() - int(bonusAdFixedDamage.get())
        normalBonusDamage = normalBonusDamage * 2
        bonusCriticalDie = {"d4":int(bonusCritDieD4.get()),"d6":int(bonusCritDieD6.get()),"d8":int(bonusCritDieD8.get()),"d10":int(bonusCritDieD10.get()),"d12":int(bonusCritDieD12.get())}
        bonusCritDamage = {}
        for i in bonusCriticalDie:
            if bonusCriticalDie[i] > 0:
                bonusCritDamage[i] = bonusCriticalDie[i]
        for i in bonusCritDamage:
            if i == "d4":
                normalBonusDamage += bonusCritDamage[i] * (2.5)
            elif i == "d6":
                normalBonusDamage += bonusCritDamage[i] * (3.5)
            elif i == "d8":
                normalBonusDamage += bonusCritDamage[i] * (4.5)
            elif i == "d10":
                normalBonusDamage += bonusCritDamage[i] * (5.5)
            elif i == "d12":
                normalBonusDamage += bonusCritDamage[i] * (6.5)
        normalBonusDamage += int(bonusCritFixedDamage.get())
        return normalBonusDamage
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)
        

def damageFullBonus():
    try:
        bonusDamage = int(numOfBonusAttacksEntry.get())*(((bonusAttackProb() - criticalHitProb()) * damagePerBonusHit() + (criticalHitProb() * damagePerBonusCrit())))
        return bonusDamage
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)

def damagePerRound():
    try:
        DAMAGE = (int(numOfAttacksEntry.get())*((attackProb() - criticalHitProb()) * damagePerHit() + (criticalHitProb() * damagePerCrit()))) + damageFullBonus() + damagePerExtra()
        displayAnswer.config(text=round(DAMAGE,2))
    except:
        value = "Please enter only integer numbers"
        displayAnswer.config(text=value)
    

submitDPR = ttk.Button(mainFrame, text="Submit",command=lambda: damagePerRound())

#Saving Throw DPR (Layout being coded as the element is being made)
mainFrame2 = ttk.Frame(window, borderwidth=10)
rigBotFrame = ttk.Frame(mainFrame2, borderwidth=10)
mainFrame2.grid(columnspan=2,row=2)
rigBotFrame.grid(pady=5, column=0,row=0)

saveDCCalc = ttk.Label(rigBotFrame, text="Save Average Damage Per Round Calculator",font=fontObj)
saveDCCalc.grid()

topRigBotFrame = ttk.Frame(rigBotFrame,borderwidth=10)
topRigBotFrame.grid()

saveBonusLabel = ttk.Label(topRigBotFrame,text="Target Save Throw Bonus")
saveBonusLabel.grid(column=0,row=0,padx=5)

saveBonusVariable = tk.IntVar()
saveBonusVariable.set(0)
saveBonus = ttk.Entry(topRigBotFrame,width=5,text=saveBonusVariable)
saveBonus.grid(column=1,row=0,padx=2)

saveDCLabel = ttk.Label(topRigBotFrame, text="Save DC")
saveDCLabel.grid(column=2,row=0,padx=5)

saveDCVariable = tk.IntVar()
saveDCVariable.set(0)
saveDC = ttk.Entry(topRigBotFrame, width=5, text=saveDCVariable)
saveDC.grid(column=3,row=0,padx=2)

topRigBotFrame2 = ttk.Frame(rigBotFrame,borderwidth=10)
topRigBotFrame2.grid(row=2)

numOfTargetsLabel = tk.Label(topRigBotFrame2, text="Number of Targets")
numOfTargetsLabel.grid(column=3,row=2,padx=5)

numOfTargetsVariable = tk.IntVar()
numOfTargetsVariable.set(1)
numOfTargets = ttk.Entry(topRigBotFrame2, width=5, text=numOfTargetsVariable)
numOfTargets.grid(column=5,row=2,padx=2)

rigBotDieFrame = ttk.Frame(rigBotFrame,borderwidth=10)
rigBotDieFrame.grid()

saveDamageDie = ttk.Label(rigBotDieFrame,text="Damage Dice for Failed Save")
saveDamageDie.grid(row=0)

saveDieFrame = ttk.Frame(rigBotDieFrame, borderwidth=10)
saveDieFrame.grid(row=1)

saveD4Variable = tk.IntVar()
saveD4Variable.set(0)
saveDieD4 = ttk.Entry(saveDieFrame,width=2, text=saveD4Variable)
saveD4Label = ttk.Label(saveDieFrame,text="d4")
saveDieD4.grid(column=0,row=1)
saveD4Label.grid(column=1,row=1)

saveD6Variable = tk.IntVar()
saveD6Variable.set(0)
saveDieD6 = ttk.Entry(saveDieFrame,width=2, text=saveD6Variable)
saveD6Label = ttk.Label(saveDieFrame,text="d6")
saveDieD6.grid(column=2,row=1)
saveD6Label.grid(column=3,row=1)

saveD8Variable = tk.IntVar()
saveD8Variable.set(0)
saveDieD8 = ttk.Entry(saveDieFrame,width=2, text=saveD8Variable)
saveD8Label = ttk.Label(saveDieFrame,text="d8")
saveDieD8.grid(column=4,row=1)
saveD8Label.grid(column=5,row=1)

saveD10Variable = tk.IntVar()
saveD10Variable.set(0)
saveDieD10 = ttk.Entry(saveDieFrame,width=2, text=saveD10Variable)
saveD10Label = ttk.Label(saveDieFrame,text="d10")
saveDieD10.grid(column=6,row=1)
saveD10Label.grid(column=7,row=1)

saveD12Variable = tk.IntVar()
saveD12Variable.set(0)
saveDieD12 = ttk.Entry(saveDieFrame,width=2, text=saveD12Variable)
saveD12Label = ttk.Label(saveDieFrame,text="d12")
saveDieD12.grid(column=8,row=1)
saveD12Label.grid(column=9,row=1)

saveDamageLabel = ttk.Label(saveDieFrame,text="Fixed Damage")
saveFixVariable = tk.IntVar()
saveFixVariable.set(0)
saveFixedDamage = ttk.Entry(saveDieFrame,width=5, text=saveFixVariable)
saveDamageLabel.grid(column=10,row=1)
saveFixedDamage.grid(column=11,row=1)

displaySaveAnswer = ttk.Label(rigBotFrame,text='',font=fontObj)

#Save functions (My code is all over the place because for some reason it is only working betwee the display***Answer label and the submit button

def saveFailProb():
    return 1 - ((21-int(saveDC.get())+int(saveBonus.get()))/20)

def saveDamageDie():
    try:
        saveDamageDie = {"d4":int(saveDieD4.get()),"d6":int(saveDieD6.get()),"d8":int(saveDieD8.get()),"d10":int(saveDieD10.get()),"d12":int(saveDieD12.get())}
        saveDamage = {}
        for i in saveDamageDie:
            if saveDamageDie[i] > 0:
                saveDamage[i] = saveDamageDie[i]
        avgSaveDamage = 0
        for i in saveDamage:
            if i == "d4":
                avgSaveDamage += saveDamage[i] * (2.5)
            elif i == "d6":
                avgSaveDamage += saveDamage[i] * (3.5)
            elif i == "d8":
                avgSaveDamage += saveDamage[i] * (4.5)
            elif i == "d10":
                avgSaveDamage += saveDamage[i] * (5.5)
            elif i == "d12":
                avgSaveDamage += saveDamage[i] * (6.5)
        avgSaveDamage += int(saveFixedDamage.get())
        return avgSaveDamage
    except:
        pass

def saveDamagePerRound():
    try:
        evasionDAMAGE = int(numOfTargets.get())*(saveFailProb() * ((saveDamageDie()/2)+0.25))
        halfDAMAGE = int(numOfTargets.get())*(saveFailProb() * saveDamageDie() + (1-saveFailProb()) * ((saveDamageDie()/2)+0.25))
        noDAMAGE = int(numOfTargets.get())*(saveFailProb() * saveDamageDie())
        displayVariable = "Half Damage: " + str(round(halfDAMAGE,2)) + "   No Damage: " + str(round(noDAMAGE,2)) + "   Evasion: " + str(round(evasionDAMAGE,2))
        displaySaveAnswer.config(text=displayVariable)
        return displayVariable
    except:
        variable = "Please enter only integer numbers"
        displaySaveAnswer.config(text=variable)


submitSave = ttk.Button(rigBotFrame, text="Submit", command=lambda: saveDamagePerRound())
submitSave.grid()
displaySaveAnswer.grid(pady=10)

#Layout for Healing Per Round Calculator

leftBotFrame = ttk.Frame(mainFrame2, borderwidth=10)
leftBotFrame.grid(column=1,row=0)

leftTopBotFrame = ttk.Frame(leftBotFrame, borderwidth=10)
leftTopBotFrame.grid()

healingLabel = ttk.Label(leftTopBotFrame, text="Average Healing per Round Calculator",font=fontObj)
healingLabel.grid()

leftBotDieFrame = ttk.Frame(leftBotFrame,borderwidth=10)
leftBotDieFrame.grid()

healDamageDie = ttk.Label(leftBotDieFrame,text="Healing Dice")
healDamageDie.grid(row=0)

healDieFrame = ttk.Frame(leftBotDieFrame, borderwidth=10)
healDieFrame.grid(row=1)

healD4Variable = tk.IntVar()
healD4Variable.set(0)
healDieD4 = ttk.Entry(healDieFrame,width=2, text=healD4Variable)
healD4Label = ttk.Label(healDieFrame,text="d4")
healDieD4.grid(column=0,row=1)
healD4Label.grid(column=1,row=1)

healD6Variable = tk.IntVar()
healD6Variable.set(0)
healDieD6 = ttk.Entry(healDieFrame,width=2, text=healD6Variable)
healD6Label = ttk.Label(healDieFrame,text="d6")
healDieD6.grid(column=2,row=1)
healD6Label.grid(column=3,row=1)

healD8Variable = tk.IntVar()
healD8Variable.set(0)
healDieD8 = ttk.Entry(healDieFrame,width=2, text=healD8Variable)
healD8Label = ttk.Label(healDieFrame,text="d8")
healDieD8.grid(column=4,row=1)
healD8Label.grid(column=5,row=1)

healD10Variable = tk.IntVar()
healD10Variable.set(0)
healDieD10 = ttk.Entry(healDieFrame,width=2, text=healD10Variable)
healD10Label = ttk.Label(healDieFrame,text="d10")
healDieD10.grid(column=6,row=1)
healD10Label.grid(column=7,row=1)

healD12Variable = tk.IntVar()
healD12Variable.set(0)
healDieD12 = ttk.Entry(healDieFrame,width=2, text=healD12Variable)
healD12Label = ttk.Label(healDieFrame,text="d12")
healDieD12.grid(column=8,row=1)
healD12Label.grid(column=9,row=1)

healDamageLabel = ttk.Label(healDieFrame,text="Fixed Damage")
healFixVariable = tk.IntVar()
healFixVariable.set(0)
healFixedDamage = ttk.Entry(healDieFrame,width=5, text=healFixVariable)
healDamageLabel.grid(column=10,row=1)
healFixedDamage.grid(column=11,row=1)

displayHealAnswer = ttk.Label(leftBotFrame,text='',font=fontObj)

#Healing Functions

def heal():
    try:
        healDamageDie = {"d4":int(healDieD4.get()),"d6":int(healDieD6.get()),"d8":int(healDieD8.get()),"d10":int(healDieD10.get()),"d12":int(healDieD12.get())}
        healDamage = {}
        for i in healDamageDie:
            if healDamageDie[i] > 0:
                healDamage[i] = healDamageDie[i]
        avgHealDamage = 0
        for i in healDamage:
            if i == "d4":
                avgHealDamage += healDamage[i] * (2.5)
            elif i == "d6":
                avgHealDamage += healDamage[i] * (3.5)
            elif i == "d8":
                avgHealDamage += healDamage[i] * (4.5)
            elif i == "d10":
                avgHealDamage += healDamage[i] * (5.5)
            elif i == "d12":
                avgHealDamage += healDamage[i] * (6.5)
        avgHealDamage += int(healFixedDamage.get())
        displayHealAnswer.config(text=avgHealDamage)
        return avgHealDamage
    except:
        variable = "Please enter only integer numbers"
        displayHealAnswer.config(text=variable)

submitHeal = ttk.Button(leftBotFrame, text="Submit", command=lambda: heal())
submitHeal.grid()
displayHealAnswer.grid(pady=10)



#Layout for the main DPR calculator

mainFrame.grid(columnspan=2,row=0)
titleFrame.grid()
label.grid(pady=5)

frameTop.grid(row=1)
attackRoll.grid(column=0,row=1,padx=5)
aRollEntry.grid(column=1,row=1,padx=2)
targetAC.grid(column=2,row=1,padx=5)
acEntry.grid(column=3,row=1,padx=2)
numOfAttacks.grid(column=4,row=1,padx=5)
numOfAttacksEntry.grid(column=5,row=1,padx=2)
criticalNum.grid(column=6,row=1,padx=5)
criticalNumEntry.grid(column=7,row=1,padx=2)

bonusFrameTop.grid(row=2,column=0)

bigFrameDice.grid()

frameDice.grid(row=2,column=0)

damageDie.grid()
frameDamageDie.grid()
damageDieD4.grid(column=0,row=0)
d4Label.grid(column=1,row=0)
damageDieD6.grid(column=2, row=0)
d6Label.grid(column=3,row=0)
damageDieD8.grid(column=4,row=0)
d8Label.grid(column=5,row=0)
damageDieD10.grid(column=6,row=0)
d10Label.grid(column=7,row=0)
damageDieD12.grid(column=8,row=0)
d12Label.grid(column=9,row=0)
adDamageLabel.grid(column=10,row=0)
adFixedDamage.grid(column=11,row=0)

extraDamageDie.grid()
frameExtraDie.grid(sticky=tk.S)
extraDieD4.grid(column=0,row=0)
extraD4Label.grid(column=1,row=0)
extraDieD6.grid(column=2, row=0)
extraD6Label.grid(column=3,row=0)
extraDieD8.grid(column=4,row=0)
extraD8Label.grid(column=5,row=0)
extraDieD10.grid(column=6,row=0)
extraD10Label.grid(column=7,row=0)
extraDieD12.grid(column=8,row=0)
extraD12Label.grid(column=9,row=0)
extraDamageLabel.grid(column=10,row=0)
extraFixedDamage.grid(column=11,row=0)

critDamageDie.grid()
frameCritDie.grid(sticky=tk.S)
critDieD4.grid(column=0,row=0)
critD4Label.grid(column=1,row=0)
critDieD6.grid(column=2, row=0)
critD6Label.grid(column=3,row=0)
critDieD8.grid(column=4,row=0)
critD8Label.grid(column=5,row=0)
critDieD10.grid(column=6,row=0)
critD10Label.grid(column=7,row=0)
critDieD12.grid(column=8,row=0)
critD12Label.grid(column=9,row=0)
critDamageLabel.grid(column=10,row=0)
critFixedDamage.grid(column=11,row=0)

bonusAttackFrame.grid(row=2,column=1)

bonusAttackRoll.grid(row=2,column=1,padx=10)
bonusAttackRollEntry.grid(row=2,column=2,padx=5)

numOfBonusAttacks.grid(row=2,column=3,padx=10)
numOfBonusAttacksEntry.grid(row=2,column=4,padx=5)

bonusFrameDice.grid()

bonusDamageDie.grid()
bonusFrameDamageDie.grid()
bonusDamageDieD4.grid(column=0,row=0)
bonusD4Label.grid(column=1,row=0)
bonusDamageDieD6.grid(column=2, row=0)
bonusD6Label.grid(column=3,row=0)
bonusDamageDieD8.grid(column=4,row=0)
bonusD8Label.grid(column=5,row=0)
bonusDamageDieD10.grid(column=6,row=0)
bonusD10Label.grid(column=7,row=0)
bonusDamageDieD12.grid(column=8,row=0)
bonusD12Label.grid(column=9,row=0)
bonusAdDamageLabel.grid(column=10,row=0)
bonusAdFixedDamage.grid(column=11,row=0)

"""

bonusExtraDamageDie.grid()
bonusFrameExtraDie.grid(sticky=tk.S)
bonusExtraDieD4.grid(column=0,row=0)
bonusExtraD4Label.grid(column=1,row=0)
bonusExtraDieD6.grid(column=2, row=0)
bonusExtraD6Label.grid(column=3,row=0)
bonusExtraDieD8.grid(column=4,row=0)
bonusExtraD8Label.grid(column=5,row=0)
bonusExtraDieD10.grid(column=6,row=0)
bonusExtraD10Label.grid(column=7,row=0)
bonusExtraDieD12.grid(column=8,row=0)
bonusExtraD12Label.grid(column=9,row=0)
bonusExtraDamageLabel.grid(column=10,row=0)
bonusExtraFixedDamage.grid(column=11,row=0)

"""

bonusCritDamageDie.grid()
bonusFrameCritDie.grid(sticky=tk.S)
bonusCritDieD4.grid(column=0,row=0)
bonusCritD4Label.grid(column=1,row=0)
bonusCritDieD6.grid(column=2, row=0)
bonusCritD6Label.grid(column=3,row=0)
bonusCritDieD8.grid(column=4,row=0)
bonusCritD8Label.grid(column=5,row=0)
bonusCritDieD10.grid(column=6,row=0)
bonusCritD10Label.grid(column=7,row=0)
bonusCritDieD12.grid(column=8,row=0)
bonusCritD12Label.grid(column=9,row=0)
bonusCritDamageLabel.grid(column=10,row=0)
bonusCritFixedDamage.grid(column=11,row=0)

submitDPR.grid(pady=5, sticky=tk.N)
displayAnswer.grid(pady=10)

window.mainloop()
