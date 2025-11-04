#********* FEATURES INCLUDED ********
##1.Pencil(Mandatory)
##2.Eraser(Mandatory)
##3.Brush(Mandatory)
##4.Line(Mandatory)
##5.Rectangle(Mandatory)
##6.Oval(Mandatory)
##7.Color(Mandatory)
##8.Shapefill(Mandatory)
##9.Stamp(Mandatory)
#10.Load/SaveImages(Mandatory)
#11.Fillscreen
#12.Eyedrop
#13.StampOptionChange
#14.Normal/Hover/Select
#15.Thicknesschange
#16.Music
#17.ToolDescription
#18.ChangeBackground
#19.ModifiedBackgroundEraser
#20.ChangeColorwithSliders
#21.Undo/Redo
#22.ClearScreen





from pygame import *
from math import *
from tkinter import *
from tkinter import filedialog

Tk().withdraw()#hides the extra tk screen

width,height=1000,650
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

tool="" #sets the tool variable, changes depedning on conditions
r=0
g=0
b=0
col=(r,g,b)#the original col value
init() # need init to initialize the mixer
font.init()#allows for text

#imports in all the pictures so they can be used
Backpic=image.load('pics/Back.jpg')
Halalpic=image.load('pics/halal.png')
paintpic=image.load('pics/paint.png')
rgbpic=image.load('pics/rbg.jpg')
pencilpic=image.load('pics/pencil.png')
eraserpic=image.load('pics/eraser.png')
brushpic=image.load('pics/brush.png')
fillpic=image.load('pics/fill.png')
linepic=image.load('pics/line.png')
rectpic=image.load('pics/rect.png')
fillrectpic=image.load('pics/fillrect.png')
ovalpic=image.load('pics/oval.png')
fillovalpic=image.load('pics/filloval.png')
stamppic=image.load('pics/stamp.png')
eyedroppic=image.load('pics/eyedrop.png')
clearpic=image.load('pics/clear.png')
boypic=image.load('pics/boy.png')
girlpic=image.load('pics/girl.png')
datespic=image.load('pics/dates.png')
Masjidpic=image.load('pics/Masjid.png')
Islampic=image.load('pics/Islam.png')
savepic=image.load('pics/save.png')
openpic=image.load('pics/open.png')
undopic=image.load('pics/undo.png')
redopic=image.load('pics/redo.png')
canvaspic=image.load('pics/canvas.png')
backpic=image.load('pics/back.webp')
back2pic=image.load('pics/back2.jpg')
back3pic=image.load('pics/back3.webp')
back4pic=image.load('pics/back4.jpg')
playpic=image.load('pics/play.png')
pausepic=image.load('pics/pause.png')
previouspic=image.load('pics/previous.png')
nextpic=image.load('pics/next.png')
prevpic=image.load('pics/prev.png')
next2pic=image.load('pics/next2.png')



background=transform.scale(Backpic,(1000,650))#makes the background picture bigger
Halal=transform.scale(Halalpic,(150,100))
rgb=transform.scale(rgbpic,(100,100))
pencil=transform.scale(pencilpic,(50,50))
eraser=transform.scale(eraserpic,(50,50))
brush=transform.scale(brushpic,(50,50))
fill=transform.scale(fillpic,(50,50))
line=transform.scale(linepic,(50,50))
rect=transform.scale(rectpic,(40,40))
fillrect=transform.scale(fillrectpic,(50,50))
oval=transform.scale(ovalpic,(40,40))
filloval=transform.scale(fillovalpic,(40,40))
stamp=transform.scale(stamppic,(50,50))
eyedrop=transform.scale(eyedroppic,(40,40))
clear=transform.scale(clearpic,(50,50))
boy=transform.scale(boypic,(100,100))
girl=transform.scale(girlpic,(100,100))
dates=transform.scale(datespic,(100,100))
Masjid=transform.scale(Masjidpic,(100,100))
Islam=transform.scale(Islampic,(100,100))
save=transform.scale(savepic,(50,50))
openn=transform.scale(openpic,(50,50))
undo=transform.scale(undopic,(50,50))
redo=transform.scale(redopic,(50,50))
canvas=transform.scale(canvaspic,(600,400))
back=transform.scale(backpic,(600,400))
back2=transform.scale(back2pic,(600,400))
back3=transform.scale(back3pic,(600,400))
back4=transform.scale(back4pic,(600,400))
play=transform.scale(playpic,(40,40))
pause=transform.scale(pausepic,(50,50))
previous=transform.scale(previouspic,(50,50))
nextt=transform.scale(nextpic,(50,50))
prev=transform.scale(prevpic,(50,100))
next2=transform.scale(next2pic,(50,100))



screen.blit(background,(0,0))#displays the new background
#displays most of the outside pictures
screen.blit(Halal,(355,0))
calibri50=font.SysFont('Calibri',50)
Halaltext=calibri50.render('Paint',True,BLACK)
screen.blit(paintpic,(420,-62))
screen.blit(pencil,(5,100))
screen.blit(eraser,(65,100))
screen.blit(brush,(125,100))
screen.blit(fill,(125,220))
screen.blit(line,(125,160))
screen.blit(rect,(10,165))
screen.blit(fillrect,(65,165))
screen.blit(oval,(10,225))
screen.blit(filloval,(70,225))
screen.blit(stamp,(5,280))
screen.blit(eyedrop,(70,285))
screen.blit(clear,(125,280))
screen.blit(save,(5,0))
screen.blit(openn,(65,0))
screen.blit(undo,(125,0))
screen.blit(redo,(185,0))
screen.blit(previous,(770,0))
screen.blit(pause,(828,0))
screen.blit(play,(893,5))
screen.blit(nextt,(944,0))



#All the rectangles
pencilRect=Rect(5,100,50,50)
eraserRect=Rect(65,100,50,50)
brushRect=Rect(125,100,50,50)
fillRect=Rect(125,220,50,50)
lineRect=Rect(125,160,50,50)
rectRect=Rect(5,160,50,50)
rectfillRect=Rect(65,160,50,50)
ovalRect=Rect(5,220,50,50)
ovalfillRect=Rect(65,220,50,50)
stampRect=Rect(5,280,50,50)
stampsRect=Rect(460,545,100,100)
backsRect=Rect(700,545,200,100)
prevstampRect=Rect(410,545,50,100)
prevbackRect=Rect(650,545,50,100)
nextstampRect=Rect(560,545,50,100)
nextbackRect=Rect(900,545,50,100)
eyedropRect=Rect(65,280,50,50)
clearRect=Rect(125,280,50,50)
saveRect=Rect(5,0,50,50)
openRect=Rect(65,0,50,50)
undoRect=Rect(125,0,50,50)
redoRect=Rect(185,0,50,50)
draw.rect(screen,WHITE,(185,220,170,110))#the rectnagle behind the thickness bar
barRect=Rect(315,225,30,85)#rectangle fro the thickness bar
barRect2=Rect(315,225,30,99)#2nd rectangle for the thickness bar 
y=309
thickRect=Rect(315,y,30,15)#rectangle for the thickeness slider
draw.rect(screen,WHITE,(5,375,290,270))#the rectangle behind the color sliders and color pallete
xr=15
redRect=Rect(15,500,256,35)#the rectangle for the red bar
redRect2=Rect(15,500,270,35)#the 2nd rectangle for the red bar
redsliderRect=Rect(xr,500,15,35)
xg=15
greenRect=Rect(15,550,256,35)#the rectangle for the green bar
greenRect2=Rect(15,550,270,35)#the 2nd rectangle for the green bar
greensliderRect=Rect(xg,550,15,35)
xb=15
blueRect=Rect(15,600,256,35)#the rectangle for the blue bar
blueRect2=Rect(15,600,270,35)#the 2nd rectangle for the blue bar
bluesliderRect=Rect(xb,600,15,35)
canvasRect=Rect(370,100,600,400)#the canvas
cpRect=Rect(370,500,600,15)#the rectangle where the position of the mouse on the canvas will be displayed
palRect=Rect(15,385,100,100)#the color pallete
colRect=Rect(162,435,50,50)#rectangle that displays the selected color
colOutline=Rect(162,435,50,50)
calibri26=font.SysFont('Calibri',26)
selected=calibri26.render('Selected',True,BLACK)
color=calibri26.render('Colour:',True,BLACK)
previousnRect=Rect(770,0,50,50)
pauseRect=Rect(828,0,50,50)
playRect=Rect(886,0,50,50)
nextnRect=Rect(944,0,50,50)
draw.rect(screen,WHITE,cpRect)
draw.rect(screen,BLACK,cpRect,1)#the outline for the cpRect
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,saveRect,2)
draw.rect(screen,BLACK,openRect,2)
draw.rect(screen,BLACK,undoRect,2)
draw.rect(screen,BLACK,redoRect,2)
draw.rect(screen,BLACK,previousnRect,2)
draw.rect(screen,BLACK,pauseRect,2)
draw.rect(screen,BLACK,playRect,2)
draw.rect(screen,BLACK,nextnRect,2)


#list of the tools rectangles:
rects=[pencilRect,eraserRect,brushRect,fillRect,lineRect,rectRect,rectfillRect,ovalRect,ovalfillRect,stampRect, eyedropRect,clearRect]
#list of the tools:
tools=['pencil',  'eraser',   'brush',  'fill', 'line', 'rect',  'rectfill',   'oval',  'ovalfill', 'stamp',    'eyedrop','clear']
#list of the 3 states(default,hover,select). Right now all 0 but will be changed when certain conditions are met
select=[0      ,     0     ,     0   ,     0  ,    0   ,   0   ,    0    ,    0  ,      0,          0  ,          0  ,          0]
#list of the stamps:
stamps=[boy,girl,dates,Masjid,Islam]
#list of the backgrounds:
backgrounds=[canvas,back,back2,back3,back4]
#list of the nasheeds:
nasheeds=["Moula Ya Salli","Tabalagho Bil Qaleel","Wonders",
          "Like The Strong Wind","The-Way-Of-The-Tears"]

#the lines of the description box:
dline1=['The Pencil tool: Draws a line','The Eraser tool: Erases any of the ','The Brush tool: Draws like the','The Fill Screen tool: Fills the',
        'The Line tool: Draws a line','The Rectangle tool: Draws a','The Filled Rectangle tool: Same','The Oval tool: Draws an oval by',
        'The Filled Oval tool: Same as the','The Stamps tool: Stamps the','The Eyedrop tool: Picks a colour','The Clear Screen tool: Clears any']
dline2=['across the canvas in the selected','tools used on the canvas, eraser','pencil in the selected colour,','screen with the selected colour.',
        'connecting from one point to','rectangle by resting one point,','as the rectangle, but filled in the','resting one point, then dragging',
        'oval, but filled in the selected','selected stamp picture onto the','from the point pressed on the','work done on the canvas.']

dline3=['colour. Thickness cannot be','changes depending on the','but thickness can be adjusted.','','another in the selected colour.',
        'then dragging the other to form a ','selected colour. There is no ','the other to form an oval of your','colour. There is no thickness','canvas.','canvas, then relays it as the','']

dline4=['adjusted.','background. Thickness can be','','','Thickness can be adjusted.','rectangle of your choice in the',
        'thickness to be adjusted.','choice in the selected colour.','to be adjusted.','','selected colour.','']
dline5=['','adjusted.','','','','selected colour. Thickness of the',
        '','Thickness of the outline can be','','','','']

dline6=['','','','','','outline can be adjusted.', '','adjusted.','','','','']

#the lists of rectangles of the feautures at the top of the screen
rectscorner=[saveRect,openRect,undoRect,redoRect,previousnRect,pauseRect,playRect,nextnRect]
#the descirptions of these features
dlinef=['Saves the canvas to a place you','Loads a picture you choose onto','Undos the last action on the',
        'Redos the last action on the','Play the previous Nasheed.','Pause the Nasheed.','Play the Nasheed.','Play the next Nasheed.',]
dlinef2=['choose.','the canvas.','canvas.','canvas.','','','','']
        
undos=[]
redos=[]


calibriFont=font.SysFont('Calibri',18)
calibri12=font.SysFont('Calibri',12)
calibri14=font.SysFont('Calibri',14)
text=calibri12.render('Welcome to Halal Paint! Choose',True,BLACK)
text2=calibri12.render('a tool to get started!',True,BLACK)
describeRect=Rect(185,100,170,110)#descirption rectangle
draw.rect(screen,WHITE,describeRect)
screen.blit(text,(190,105))
screen.blit(text2,(190,120))

pos=0#the position in the stamps list
pos2=0#the position in the backgrounds list
posn=0#the position in the nasheeds list
playnasheed='no'#prevents nasheeds from being played before clicking play button
pause=0#determines whether play button will start a Nasheed, or unpause a Nasheed
draw.rect(screen,WHITE,(770,55,224,40))#the rectangle for the nasheed playing
playtext=calibriFont.render('Playing:',True,BLACK)
screen.blit(playtext,(773,60))
    

#all the rectangles for the bars and sliders and the things included in the boxes behind the sliders
screen.blit(rgb,(15,385))
draw.rect(screen,BLACK,palRect,1)
screen.blit(selected,(145,385))
screen.blit(color,(145,410))
draw.rect(screen,col,colRect)
draw.rect(screen,BLACK,colOutline,2)
draw.rect(screen,BLACK,barRect)
draw.rect(screen,BLACK,barRect2)
thicktext=calibri26.render('Thickness',True,BLACK)
thicktext2=calibri26.render('Change:',True,BLACK)
screen.blit(thicktext,(195,250))
screen.blit(thicktext2,(195,270))
draw.rect(screen,RED,thickRect)
draw.rect(screen,RED,redRect)
draw.rect(screen,RED,redRect2)
draw.rect(screen,BLACK,redsliderRect)
draw.rect(screen,GREEN,greenRect)
draw.rect(screen,GREEN,greenRect2)
draw.rect(screen,BLACK,greensliderRect)
draw.rect(screen,BLUE,blueRect)
draw.rect(screen,BLUE,blueRect2)
draw.rect(screen,BLACK,bluesliderRect)


canvasCopy=screen.subsurface(canvasRect).copy()#takes screenshot of the canvas area
undos.append(canvasCopy)#appends the blank canvas into the undos list, this canvas cannot be undone


running=True

while running:
    thick=310-y#calculates the thickess for eraser,brush,line, and unfilled rectangle and oval
    r=xr-15#calculates the red value of the selected color(default 0)
    g=xg-15#calculates the green value of the selected color(defualt 0)
    b=xb-15#calculates the blue value of the selected color(default 0)
    
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:#left button pressed
                if undoRect.collidepoint(mx,my) and len(undos)>1:
                    redos.append(undos[-1])#appends the last item of the undos list into redos list
                    undos.pop()#removes the last item from the list
                    screen.blit(undos[-1],canvasRect)#takes the last item from the undos list and displays it
                    
                if redoRect.collidepoint(mx,my) and len(redos)>0:
                    undos.append(redos[-1])#appedsn the last item of the redos list into the undos list
                    redos.pop()#removes the last item from the list
                    screen.blit(undos[-1],canvasRect)#takes the last item from the undos list and displays it
                    print("r",len(undos),len(redos))
                    
                sx,sy=evt.pos#sets up the previous points
            
           
                if palRect.collidepoint(mx,my):#and the mouse is pressed
                    col=screen.get_at((mx,my))#the color selected will turn into the color of the point the mouse pressed on
                    
                    rp=col[0]+15
                    gp=col[1]+15
                    bp=col[2]+15
                    #colors from the pallettte
                    xr=rp
                    draw.rect(screen,RED,redRect)
                    draw.rect(screen,RED,redRect2)
                    redsliderRect=Rect(xr,500,15,35)
                    draw.rect(screen,BLACK,redsliderRect)
                    #alligns the red color of the color pallete with the silders position on the red bar
                    xg=gp
                    draw.rect(screen,GREEN,greenRect)
                    draw.rect(screen,GREEN,greenRect2)
                    greensliderRect=Rect(xg,550,15,35)
                    draw.rect(screen,BLACK,greensliderRect)
                    #alligns the green color of the color pallete with the silders position on the green bar
                    xb=bp
                    draw.rect(screen,BLUE,blueRect)
                    draw.rect(screen,BLUE,blueRect2)
                    bluesliderRect=Rect(xb,600,15,35)
                    draw.rect(screen,BLACK,bluesliderRect)
                    #alligns the blue color of the color pallete with the silders position on the blue barRect
                    draw.rect(screen,col,colRect)#displays the color chosen
                    draw.rect(screen,BLACK,colOutline,2)
                    
            
                if nextstampRect.collidepoint(mx,my):
                    pos=(pos+1)%len(stamps)#changes the position in the stamps list to the next position

                if prevstampRect.collidepoint(mx,my):
                    pos=(pos-1+5)%len(stamps)#changes the position in the stamps list to the previous position
                        
                screen.blit(stamps[pos],(460,530))#prints the new stamp that allgins with the new position

                if nextbackRect.collidepoint(mx,my):
                    pos2=(pos2+1)%len(backgrounds)#changes the position in the backgrounds list to the next position
                    screen.blit(backgrounds[pos2].subsurface(0,0,600,400),(370,100))
                    canvasCopy=screen.subsurface(canvasRect).copy()
                    #copies the canvas once the background is changed so it can be appended to the undos list
                    undos.append(canvasCopy)
                    
                    
                elif prevbackRect.collidepoint(mx,my):
                    pos2=(pos2-1+5)%len(backgrounds)#changes the position in the stamps list to the previous position
                    screen.blit(backgrounds[pos2].subsurface(0,0,600,400),(370,100))
                    canvasCopy=screen.subsurface(canvasRect).copy()
                    #copies the canvas once the background is changed so it can be appended to the undos list
                    undos.append(canvasCopy)
            
                if nextnRect.collidepoint(mx,my):
                    if playnasheed=='yes':#will only allow next nasheed to be played or change position if the play button is clicked first
                        posn=(posn+1)%len(nasheeds)#changes the position in the nasheeds list to the next position
                        mixer.music.stop()#stops the current nasheed
                        mixer.music.load(f'music/{nasheeds[posn]}.mp3')#loads the next nasheed
                        mixer.music.play()#plays it
                        playing=calibriFont.render(f'Playing:{nasheeds[posn]}',True,BLACK)
                        draw.rect(screen,WHITE,(770,55,224,40))
                        screen.blit(playing,(773,60))
                        #displays which nasheed is being played
                        
                    

                if previousnRect.collidepoint(mx,my):
                    if playnasheed=='yes':#will only allow previous nasheed to be played or change position if the play button is clicked first
                        posn=(posn-1+5)%len(nasheeds)#changes the position in the nasheeds list to the previous position
                        mixer.music.stop()#stops the current nasheed
                        mixer.music.load(f'music/{nasheeds[posn]}.mp3')#loads the previous nasheed
                        mixer.music.play()#plays it
                        playing=calibriFont.render(f'Playing:{nasheeds[posn]}',True,BLACK)
                        draw.rect(screen,WHITE,(770,55,224,40))
                        screen.blit(playing,(773,60))
                        #displays which nasheed is being played
                        
                    
                if playRect.collidepoint(mx,my):
                    if pause==0:#if the Nasheed has not been paused
                        mixer.music.load(f'music/{nasheeds[posn]}.mp3')
                        mixer.music.play()
                        playing=calibriFont.render(f'Playing:{nasheeds[posn]}',True,BLACK)
                        draw.rect(screen,WHITE,(770,55,224,40))
                        screen.blit(playing,(773,60))
                        playnasheed='yes'#allows the next/previous nasheeds to play
                        pause=2#this makes sure that the nasheed will only pause once it has been played first
                    elif pause==1:#if Nasheed is paused
                        mixer.music.unpause()
                        #will resume the Nasheed from where it was paused
                        playing=calibriFont.render(f'Playing:{nasheeds[posn]}',True,BLACK)
                        draw.rect(screen,WHITE,(770,55,224,40))
                        screen.blit(playing,(773,60))
                        #displays what Nasheed is being played
                        playnasheed='yes'#allows the next/previous nasheeds to play
                        pause=2#allows for the pause to work
                        
                if pauseRect.collidepoint(mx,my):
                    if pause==2:#Nasheed will only pause once it has been played first
                        mixer.music.pause()
                        pause=calibriFont.render(f'Playing:',True,BLACK)
                        draw.rect(screen,WHITE,(770,55,224,40))
                        screen.blit(pause,(773,60))
                        playnasheed='no'#prevents the next/previous nasheed from being played until play is pressed
                        pause=1#will allow Nasheed to resume where it let off, and not restart everytime
                     
                
                    
                        
                    
                        
                    
                    
##            
        if evt.type==MOUSEBUTTONUP:
            canvasCopy=screen.subsurface(canvasRect).copy()
            #copies canvas 
        
            if tool!='' and tool!='eyedrop' and canvasRect.collidepoint(mx,my):
                
                undos.append(canvasCopy)
                redos=[]#if somnething new is added to the canvas, the redos will reset
               
            


    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    
    #draws all the shapes on the outside that are not in the rects loop
    draw.rect(screen,WHITE,(410,520,200,30))#on top of stampsrect
    draw.rect(screen,BLACK,(410,520,200,30),1)#outline
    stamptext=calibri14.render('Change Stamp',True,BLACK)
    screen.blit(stamptext,(465,525))
    draw.rect(screen,WHITE,stampsRect)#the white square behind the different stamp options
    draw.rect(screen,BLACK,stampsRect,1)#outline of the stampsRect
    draw.rect(screen,WHITE,backsRect)#the white square behind the different background options
    screen.blit(stamps[pos],(460,545))#displays the first stamp in the white square
    backpreview=transform.scale(backgrounds[pos2],(200,100))#changes the size of the current background to a small preview
    screen.blit(backpreview,(700,545))#displays the preview of the background
    draw.rect(screen,BLACK,backsRect,1)#outline of the backsRect
    draw.rect(screen,WHITE,(650,520,300,25))#on top of backsrect
    draw.rect(screen,BLACK,(650,520,300,25),1)#outline
    backtext=calibri14.render('Change Background',True,BLACK)
    screen.blit(backtext,(740,525))
    draw.rect(screen,WHITE,prevstampRect)#the previous stamp rectangle
    draw.rect(screen,BLACK,prevstampRect,1)#the previous stamp rectangle outline
    screen.blit(prev,(410,545))
    draw.rect(screen,WHITE,prevbackRect)#the previous background rectangle
    draw.rect(screen,BLACK,prevbackRect,1)#the previous background rectangle outline
    screen.blit(prev,(650,545))
    draw.rect(screen,WHITE,nextstampRect)#the next stamp rectangle
    draw.rect(screen,BLACK,nextstampRect,1)#the next stamp rectangle outline
    screen.blit(next2,(560,545))
    draw.rect(screen,WHITE,nextbackRect)#the next background rectangle
    draw.rect(screen,BLACK,nextbackRect,1)#the next background rectangle outline
    screen.blit(next2,(900,545))

    
    
    

    
    for i in rects:
        ind=rects.index(i)#sets up the position in the 'rects' list for the rectangle that was pressed
        
        
        if i.collidepoint(mx,my):#if the left mouse button presses any of the rectangles in the 'rects' list

            if mb[0]:
                tool=tools[ind]#alligns the rectangle pressed with its coressponding tool in the 'tools' list
                select=[0      ,     0     ,     0   ,     0  ,    0   ,   0   ,    0 ,0, 0,0,0,0]#resets the list everytime so the list cannot have more than 1 "1s" or "2s"
                select[ind]=2#allgins the rectangle pressed with its parallel element in the 'select' list and changes that element to 2

            
            if select[ind]==0:#if the paralell element is 0 and the mouse hovers over the respective rectangle
                select[ind]=1#the hovered rectangle will only turn red if the rectangle it is hovering is black 
               
               
        if select[ind]==0:#if the paralell element is 0(default option)
            draw.rect(screen,BLACK,rects[ind],2)#the rectangles will have black outline
            
        elif select[ind]==1:#if the paralell element is 1(hovering)
            draw.rect(screen,RED,rects[ind],2)#the hovered rectangle will have a red outline
            select[ind]=0#this makes sure multiple rectangles cannot be red at once by turning it "0" once it exits the rectangle
               
        elif select[ind]==2:#if the paralell element is 2(chosen)
            draw.rect(screen,GREEN,rects[ind],2)#the chosen rectangle will have a green outline
            #the description of the tool selected:
            draw.rect(screen,WHITE,describeRect)
            line1=calibri12.render(dline1[ind],True,BLACK)
            screen.blit(line1,(190,105))
            line2=calibri12.render(dline2[ind],True,BLACK)
            screen.blit(line2,(190,120))
            line3=calibri12.render(dline3[ind],True,BLACK)
            screen.blit(line3,(190,135))
            line4=calibri12.render(dline4[ind],True,BLACK)
            screen.blit(line4,(190,150))
            line5=calibri12.render(dline5[ind],True,BLACK)
            screen.blit(line5,(190,165))
            line6=calibri12.render(dline6[ind],True,BLACK)
            screen.blit(line6,(190,180))
            

    for f in rectscorner:
        ind2=rectscorner.index(f)#sets up the position in the 'rectscorner' list for the rectangle that was pressed
        draw.rect(screen,BLACK,rectscorner[ind2],2)
        if f.collidepoint(mx,my):#if the left mouse button hovers over any of the rectangles in the 'rectscorner' list
            draw.rect(screen,RED,rectscorner[ind2],2)#draws the red hover rect
            #displays the descritption
            draw.rect(screen,WHITE,describeRect)
            linef=calibri12.render(dlinef[ind2],True,BLACK)
            screen.blit(linef,(190,105))
            linef2=calibri12.render(dlinef2[ind2],True,BLACK)
            screen.blit(linef2,(190,120))
        

    if mb[0]:
        if saveRect.collidepoint(mx,my):
            fname=filedialog.asksaveasfilename(defaultextension='.png')#allows canvas to be saved to where user chooses
                                                                       #will set extension as .png if user does not specify it
            if fname!='':#will only save if user inputs a file name
                image.save(screen.subsurface(canvasRect),fname)#saves the canvas
                
        if openRect.collidepoint(mx,my):
            fname=filedialog.askopenfilename(filetypes=[("Picture files", "*.png; *.jpg")])
            #allows user to load an image of choice onto the canvas
            #only allows for the extenstions mentioned in the list to be shown to the user to pick
            if fname!='':
                screen.blit(backgrounds[pos2],(370,100))#clears the canvas before inserting picture
                load=image.load(fname)#loads the image
                wl=load.get_width()#gets width of image
                hl=load.get_height()#gets height of image
                if wl>600 or hl>400:#if the pictures dimensions exceed the canvas:
                    load2=transform.scale(load,(600,400))#the picture will be resized
                    screen.blit(load2,(370,100))#then displayed
                    canvasCopy=screen.subsurface(canvasRect).copy()#copies the image
                    undos.append(canvasCopy)#appends it to undos

                else:#if the dimensions are ok
                    screen.blit(load,(370,100))#displays the image without resizing
                    canvasCopy=screen.subsurface(canvasRect).copy()#copies the image
                    undos.append(canvasCopy)#appends it to undos
    
            
        if barRect.collidepoint(mx,my):
                y=my#alligns the y position of the slider with the mouse
                draw.rect(screen,BLACK,barRect)
                draw.rect(screen,BLACK,barRect2)
                thickRect=Rect(315,y,30,15)#rectangle for the thickeness slider
                draw.rect(screen,RED,thickRect)
                #will draw rectangles to overlap the bar so multiple sliders are not displayed at once

                    
        if redRect.collidepoint(mx,my):
                xr=mx#alligns the x position of the slider with the mouse
                draw.rect(screen,RED,redRect)
                draw.rect(screen,RED,redRect2)
                redsliderRect=Rect(xr,500,15,35)
                draw.rect(screen,BLACK,redsliderRect)
                #will draw rectangles to overlap the bar so multiple sliders are not displayed at once
                r=xr-15
                g=xg-15
                b=xb-15
                #calculates the color values
                col=(r,g,b)
                draw.rect(screen,col,colRect)#displays the color chosen
                draw.rect(screen,BLACK,colOutline,2)
        if greenRect.collidepoint(mx,my):
                xg=mx#alligns the x position of the slider with the mouse
                draw.rect(screen,GREEN,greenRect)
                draw.rect(screen,GREEN,greenRect2)
                greensliderRect=Rect(xg,550,15,35)
                draw.rect(screen,BLACK,greensliderRect)
                #will draw rectangles to overlap the bar so multiple sliders are not displayed at once
                r=xr-15
                g=xg-15
                b=xb-15
                #calculates the color values
                col=(r,g,b)
                draw.rect(screen,col,colRect)#displays the color chosen
                draw.rect(screen,BLACK,colOutline,2)
        if blueRect.collidepoint(mx,my):
                xb=mx#alligns the x position of the slider with the mouse
                draw.rect(screen,BLUE,blueRect)
                draw.rect(screen,BLUE,blueRect2)
                bluesliderRect=Rect(xb,600,15,35)
                draw.rect(screen,BLACK,bluesliderRect)
                #will draw rectangles to overlap the bar so multiple sliders are not displayed at once
                r=xr-15
                g=xg-15
                b=xb-15
                #calculates the color values
                col=(r,g,b)
                draw.rect(screen,col,colRect)#displays the color chosen
                draw.rect(screen,BLACK,colOutline,2)
                
     
            
            
    draw.rect(screen,WHITE,cpRect)#prevents coordiantes from being displayed when the mouse is not in the canvas
    draw.rect(screen,BLACK,cpRect,1)#the outline for this same rectangle
    c=calibri12.render(f'Coordinates:',True,BLACK)
    screen.blit(c,(375,502))
    

    if canvasRect.collidepoint(mx,my):#if the mouse is inside the canvas:#if the left mousebutton is clicked
        cpx=mx-370#canvas point(x)
        cpy=my-100#canvas point(y)
        cp1=calibri12.render(f'Coordinates:{cpx}',True,BLACK)
        cp2=calibri12.render(f' {cpy}',True,BLACK)
        draw.rect(screen,WHITE,cpRect)
        draw.rect(screen,BLACK,cpRect,1)
        screen.blit(cp1,(375,502))
        screen.blit(cp2,(455,502))
        
        
        if mb[0]:#if the left mousebutton is clicked    
            screen.set_clip(canvasRect)#makes sure tools can only be used on the canvas
            
            
                        
            if tool=='pencil':#if the tool selected is the pencil:
                draw.line(screen,col,(omx,omy),(mx,my))
                #draws a line from the selected color from the previous point the
                #mouse was at and the current point of the mouse
                
            if tool=='eraser':#if the tool selected is the eraser:
                
                if pos2==0:
                    dx=mx-omx#horiz distance
                    dy=my-omy#vertical distance
                    dist=sqrt(dx**2+dy**2)

                    for d in range(1,int(dist)):#1,31,61,91...
                        dotX=omx+d*dx/dist#run
                        dotY=omy+d*dy/dist#rise
                        draw.circle(screen,WHITE,(int(dotX),int(dotY)),thick)
                        #draws white circles that makes it appear to dissapear but it is just covered in white
                else:
                    try:
                        dx=mx-omx#horiz distance
                        dy=my-omy#vertical distance
                        dist=sqrt(dx**2+dy**2)

                        for d in range(1,int(dist)):#1,31,61,91...
                            dotX=omx+d*dx/dist#run
                            dotY=omy+d*dy/dist#rise
                            eraser=backgrounds[pos2].subsurface((dotX-350,dotY-100,thick,thick))
                            #indentifies the posisition of the background where the mouse
                            screen.blit(eraser,(dotX,dotY))
                            #displays the alligned background position while the mouse is pressed
                    except:
                        pass
    
            if tool=='brush':#if the tool selected is the brush:
                dx=mx-omx#horiz distance
                dy=my-omy#vertical distance
                dist=sqrt(dx**2+dy**2)

                for d in range(1,int(dist)):#1,31,61,91...
                    dotX=omx+d*dx/dist#run
                    dotY=omy+d*dy/dist#rise
                    draw.circle(screen,col,(int(dotX),int(dotY)),thick)#draws the rise and run so circles can be drawn without unwanted gaps
                    #draws circles from the selected color without any gaps between circles
                    
                    
            if tool=='fill':#if the tool selected is fill screen
                screen.fill(col)
                #fills the canvas with the selected color
            if tool=='line':#if the tool selected is the line
                screen.blit(canvasCopy,canvasRect)#prevents multiple lines to be drawn at once
                draw.line(screen,col,(sx,sy),(mx,my),thick)
                #draws a line from one point to another
                
            if tool=='rect' or tool=='rectfill':#if the tool selected is either fill or unfilled rect(in same if statement because only 1 thing is changing)
                RECT=Rect(sx,sy,mx-sx,my-sy)#the coordinates for the rectangle
                RECT.normalize()#allows for rectangle to go backwards(negative)
                screen.blit(canvasCopy,canvasRect)#prevents multiple rectangles to be drawn at once
                if tool=='rectfill':#if the tool is filled rectangle
                    draw.rect(screen,col,RECT)#the rectangle will be drawn filled
                    
                else:#if tool is anything else(unfilled rectangle in this case)
                    draw.rect(screen,col,RECT,thick)#the rectangle will be drawn unfilled
                    
                     #draws a rectangle from the previous point to the point of the mouse
                    
            if tool=='oval' or tool=='ovalfill':#if the tool selected is either fill or unfilled oval(in same if statement because only 1 thing is changing)
                OVAL=Rect(sx,sy,mx-sx,my-sy)#the coordiangtes for the oval
                OVAL.normalize()#allows for the oval to be drawn backwards(negative)
                screen.blit(canvasCopy,canvasRect)#prevents multiple ovals to be drawn at once
                if tool=='ovalfill':#if tool is filled oval
                    draw.ellipse(screen,col,OVAL)#the oval will be drawn filled
                else:#if tool is anything else(not filled oval in this case)
                    draw.ellipse(screen,col,OVAL,thick)#the ovaal will be drawn unfilled
                #draws a oval from the previous point to the point of the mouse
                    
            if tool=='stamp':#if the tool selected is stamp
                w=stamps[pos].get_width()#used for centering the stamp to the mouse
                h=stamps[pos].get_height()#used for the centering the stamp to the mouse
                screen.blit(canvasCopy,canvasRect)#allows for only 1 stamp to be displayed while the mouse is pressed
                screen.blit(stamps[pos],(mx-w//2,my-h//2))#displays the selected stamp(centered to the mouse pointer)
                

            if tool=='clear':#if the tool selected is 'clear'
                draw.rect(screen,WHITE,canvasRect)
                pos2=0#resets the background when cleared

            screen.set_clip(None)#allows actions outside the canvas to function again
            
            if tool=='eyedrop':#if tool selected is eyedrop
                col=screen.get_at((mx,my))
                #it gets the color of the point pressed on the canvas(this color will be used for the other tools
                re=col[0]+15
                ge=col[1]+15
                be=col[2]+15
                #color values for the color pressed on the canvas
                xr=re
                draw.rect(screen,RED,redRect)
                draw.rect(screen,RED,redRect2)
                redsliderRect=Rect(xr,500,15,35)
                draw.rect(screen,BLACK,redsliderRect)
                #alligns the red color of the color with the silders position on the red bar
                xg=ge
                draw.rect(screen,GREEN,greenRect)
                draw.rect(screen,GREEN,greenRect2)
                greensliderRect=Rect(xg,550,15,35)
                draw.rect(screen,BLACK,greensliderRect)
                #alligns the green color of the color with the silders position on the green bar
                xb=be
                draw.rect(screen,BLUE,blueRect)
                draw.rect(screen,BLUE,blueRect2)
                bluesliderRect=Rect(xb,600,15,35)
                draw.rect(screen,BLACK,bluesliderRect)
                #alligns the blue color of the color with the silders position on the blue barRect
                draw.rect(screen,col,colRect)#displays the color chosen
                draw.rect(screen,BLACK,colOutline,2)
            

        
                    

                

            
            
    

    omx,omy=mx,my #allows program to read previous points of the mouse
    display.flip()

    
    
       
    

quit()

