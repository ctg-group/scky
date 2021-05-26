import random
from sys import platform
from colorama import Fore,init
if platform.startswith('win'):
  init()
R=Fore.RED
G=Fore.GREEN
N=Fore.RESET
C=Fore.CYAN
logo=f"""
{R} ________ _________  ________                                                            
{R}|\   ____\\___   ___\\   ____\     {G}gVynSb.3.ftdot.GI[j2hVWO2!H<EAnvBc47xc4[             
{R}\ \  \___\|___ \  \_\ \  \___|     {G}jveHB#!YCTGY(p<IsArT.woE5,j>*@!)7xpYGW4]             
{R} \ \  \       \ \  \ \ \  \  ___   {G}FP&)E)ry.HaCkEr]nxnoEgv$(h6I$!Y3x$Y,@DNp             
{R}  \ \  \____   \ \  \ \ \  \|\  \  {G}5AFJ%GS*D>192.168.0.100!(aD&id[caOjg3Odv             
{R}   \ \_______\  \ \__\ \ \_______\ {G}zeJa5H.Ey3Bz8N8.D,.Wy^zg5WoLwsc8p>%^j*bo             
{R}    \|_______|   \|__|  \|_______|{N} {G}cp2Ih[zOEB),xUBnCN%XfZ@c[Ge$uNUcXbnhZx)!             
{G}6cVXC(c5d%HG&nAoRbp(F,prcR/.1!i*yu3a43iI{R}  ________  ________  ___  __        ___    ___ 
{G}U.p<GU3y[(]!B0TNET,eRJhIRb(7)8F>!3(DBk6v{R} |\   ____\|\   ____\|\  \|\  \     |\  \  /  /|
{G}TELEGRAM,(]VhaF@j4C]hR#K.488h8#81#4dci13{R} \ \  \___|\ \  \___|\ \  \/  /|_   \ \  \/  / /
{G}zvx/%PBC1/UPV[AKjuPGc)%PythonLa>I2Ff/**g{R}  \ \_____  \ \  \    \ \   ___  \   \ \    / / 
{G}GG%]zR13Gc$j6Wrn[PU>1PKE6)ohsp(wF)7bp]D6{R}   \|____|\  \ \  \____\ \  \ \  \   \/   / /  
{G}VVkgEl>S(LB[w)>!iGWzb,BF<<HO)2Vp.FD4vjFW{R}     ____\_\  \ \_______\ \__\ \__\__/   / /   
{G}IsFk(.j7Lhl(fnI8/D]kf]e]BjFZ5r^O,XJA#Ic%{R}     |\_________\|_______|\|__| \|__|\___/ /    
{G}c,NfVlip.Erao]F#ocnYbU7SnDu.b[Kg!XN&D@YY{R}     \|_________|                   \|___|/     
{R} ___      ___  _____      ___   ___      {G}ZV[55/Exo.NJ*lx>kWBg>oOW)6RD$)hpu6xxeI!u       
{R}|\  \    /  /|/ __  \    |\  \ |\  \     {G}k!#CDGyAJzA2BBn<Hsodl[]K4cbFZA$Z$EHYi)nV       
{R}\ \  \  /  / /\/_|\  \   \ \  \\_\  \    {G}$eAv8b140.82.121.3Nx2#ge851PHkkAG(AVG#)L       
{R} \ \  \/  / /\|/ \ \  \   \ \______  \   {G}aepI<(%yYJy/N>K3Crg%F3yi%Ve#LfyIzC@[glHE       
{R}  \ \    / /      \ \  \ __\|_____|\  \  {G}U.p<GU3y[(]!B0TNET,eRJhIeV(7)8F>!3(DBk6V       
{R}   \ \__/ /        \ \__\\__\     \ \__\ {G}vEdvo8AxJ)X8#d]N>iV6A4!E/n21BG8Vhwg&pUrk       
{R}    \|__|/          \|__\|__|      \|__| {G},/hWElKLFl]5sH4^55L.Y,SR%kCY*ba]V@(Xw7s*       {N}
"""

builder_logo=f"""
{R} ________  ________  ________  ___  __   {G} ________  ________  ________  ________     
{R}|\   __  \|\   __  \|\   ____\|\  \|\  \ {G}|\   ___ \|\   __  \|\   __  \|\   __  \    
{R}\ \  \|\ /\ \  \|\  \ \  \___|\ \  \/  /|\{G} \  \_|\ \ \  \|\  \ \  \|\  \ \  \|\  \   
{R} \ \   __  \ \   __  \ \  \    \ \   ___  \{G} \  \ \\ \ \  \\\  \ \  \\\  \ \   _  _\  
{R}  \ \  \|\  \ \  \ \  \ \  \____\ \  \\ \  \{G} \  \_\\ \ \  \\\  \ \  \\\  \ \  \\  \| 
{R}   \ \_______\ \__\ \__\ \_______\ \__\\ \__\{G} \_______\ \_______\ \_______\ \__\\ _\ 
{R}    \|_______|\|__|\|__|\|_______|\|__| \|__|{G}\|_______|\|_______|\|_______|\|__|\|__|
{R} ________  ___  ___  ___  ___      {C} ________  _______   ________                     
{R}|\   __  \|\  \|\  \|\  \|\  \     {C}|\   ___ \|\  ___ \ |\   __  \                    
{R}\ \  \|\ /\ \  \\\  \ \  \ \  \    {C}\ \  \_|\ \ \   __/|\ \  \|\  \                   
{R} \ \   __  \ \  \\\  \ \  \ \  \    {C}\ \  \ \\ \ \  \_|/_\ \   _  _\                  
{R}  \ \  \|\  \ \  \\\  \ \  \ \  \____{C}\ \  \_\\ \ \  \_|\ \ \  \\  \|                 
{R}   \ \_______\ \_______\ \__\ \_______{C}\ \_______\ \_______\ \__\\ _\                 
{R}    \|_______|\|_______|\|__|\|_______|{C}\|_______|\|_______|\|__|\|__|                {N}
"""