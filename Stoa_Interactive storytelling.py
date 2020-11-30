from tkinter import * 
from tkinter import messagebox
import tkinter as tk
import random
root=Tk()
global s
s=1
i=1

c1c1 = "\n It is that time of the year where your life takes huge turns.\n Be it taking a new life or facing your death.\n How would you like the story of your life to begin?"

c1c2 = "\n The songbirds tuttled their eggs and waited for the arrival of the hatchlings,while the drowsy owl turned away in denial.\n The bats hung upside down from the creaking beams while the rodents chewed away at the wood.\n The lovebirds entagled, lost in each other to the fading sun behind them to cast the shadow of a heart.\n The crosswind surged in, filtering through the apertures in the the rotten wood sounding like a chorus of low moans"

c1c3 = "\n The remaining light drained from the hold.Wind screamed through the cracks.\n The whole world reeled. Phantom voices grew louder. \n Almost like a sea wind bearing men's voices up from the wharf.\n Chaos erupted, the mill was shook up with the rattling thunder and lighting.\n It swayed violently as the blades of the fan moved. Windows Banged. n\ Water leaked through the cracks drop by drop."

c2c1 = "\n All the while, up in the clouds were two schools of thoughts debating against each other.n\ Red pill, Blue pill and everything in between"

c2c2 = "\n Overcome with excitement boond dreams of what is to come next? n\ She hopes to drop onto a lotus petal and glimmer like a diamond. n\ To drop into the sea and travel the vastness of it. Yayyy....."

c2c3 = "\n The path of wind and rain is mine to take while yours does yearn a fulfilled life. \n We reach to touch each other, but instead..... \n The gateway open, \n the cloud bursts and boond goes falling down farther and farther......."

c3c1 = "\n Boond splashes on the sea surface and way down she goes into the depth, \n until the light fades away. Beyond the hustling underwater life there came a realm where boond could hear voices. \n A dim thought struggled, stabalised in her mind - \n Maybe the voices were those of the ancestors. \n A beam of light shone and grew larger as the gateway opened and sucked boond in."

c4c1 = "\n The gateway opened and shot boond upwards. \n Afte the metamorphosis, it seemed to boond that a film had been stripped from the world. \n The light was more vivid and hotter, the sea darker, and a new silence surrounded the depths. \n Boond felt a heaviness as she rose higher. \n Soon after, she realised that the light that shone was following her, \n infact it came from within her."

c4c2 = "\n She was pearl now. \n Looking around to find her way, the ocean parted as she bid adieue to her oyster and thanked it. \n What once was her prison was actually her cocoon! \n The ocean was vast and the possibilities endless. \n Boond swayed and swimmed and explored carefree. \n Until a force reeled her and everything around and captured her again. \n Not even the light escaped that ginormous force. Boond cursed her fate. \n Although boond realised that it was different. \n Her prison was moving and so was she with it, until she gets trapped. \n Immobile, scared and stuck. \n The pressure starts building, as if something was shving boond. \n Once \n Twice \n and then a giant push comes blowing everything to shred. \n Boond is once again freed only to find that the whale burst. \n Yes, the whale that had swallowed the pearl that got stuck in it's blowhole and when push came to shove that was the end of whale. \n Boond now roams the depth of the seas searching for her next prey."

b2_txt="Continue to create the plot"



def myClick1():
	global s
	if len(e1.get())==0:
		messagebox.showwarning("Story Generator", "Noun field empty")
	if len(e2.get())==0:
		messagebox.showwarning("Story Generator", "Adjective field empty")
   
	if len(e1.get())!=0 and s==1 :
                
	
		myLabel5=Label(root,text=c1c1)
		myLabel5.pack()
		myButton["text"] = "The strom finally arriving in full force"
		myButton1["text"] = "Wind carrying away the dark clouds"
		s=2
		#b1_txt="New button"
		

	elif len(e1.get())!=0 and s==2 :

		
		myLabel7=Label(root,text=c2c1)
		myLabel7.pack()
		myButton["text"] = "lol1"
		myButton1["text"] = "lol23"
		#b1_txt="New button"

    



def myClick2():
	global s
	if len(e1.get())==0:
   		messagebox.showwarning("Story Generator", "Noun field empty")
	if len(e2.get())==0:
		messagebox.showwarning("Story Generator", "Adjective field empty")
   
	if len(e1.get())!=0 and s==1:
     
                
		myButton["text"] = "The Lotus Lake"
		myButton1["text"] = "The Old Mill"
		
		myLabel6=Label(root,text=c1c1)
		myLabel6.pack()
		s=2
	

	
	elif len(e1.get())!=0 and s==2 :

		
		myLabel8=Label(root,text=c1c2)
		myLabel8.pack()
		myButton["text"] = "The strom finally arriving in full force"
		myButton1["text"] = "Wind carrying away the dark clouds"
	
		s=3
	

		
	elif len(e1.get())!=0 and s==3 :

		
		myLabel9=Label(root,text=c1c3)
		myLabel9.pack()
		myButton["text"] = "Edit the chapter"
		myButton1["text"] = "Continue to Chapter 2"
		s=4
	

   
	elif len(e1.get())!=0 and s==4:
        
		myButton["text"] = "Happpiness of discovering"
		myButton1["text"] = "Sorrow of separation"
		
		myLabel10=Label(root,text=c2c1)
		myLabel10.pack()
		s=5
		

	
	elif len(e1.get())!=0 and s==5 :

		
		myLabel11=Label(root,text=c2c2)
		myLabel11.pack()
		myButton["text"] = "The cloud finally bursts"
		myButton1["text"] = "The imagination continues"
	
		s=6

		
	elif len(e1.get())!=0 and s==6 :

		
		myLabel12=Label(root,text=c2c3)
		myLabel12.pack()
		myButton["text"] = "Edit the chapter"
		myButton1["text"] = "Continue to Chapter 3"
	
		s=7


   
	elif len(e1.get())!=0 and s==7:
        
		myButton["text"] = "Accept her fate"
		myButton1["text"] = "Fight for survival"
		
		myLabel13=Label(root,text=c3c1)
		myLabel13.pack()
		s=8
		


		
	elif len(e1.get())!=0 and s==8 :

		
		myLabel14=Label(root,text=c4c1)
		myLabel14.pack()
		myButton["text"] = "Edit the chapter"
		myButton1["text"] = "Continue to Chapter 4"
		
		s=9
				
	elif len(e1.get())!=0 and s==9 :

		
		myLabel15=Label(root,text=c4c1)
		myLabel15.pack()
		myButton["text"] = "You've become a Pearl"
		myButton1["text"] = "You're surrounded by dust"
		s=10
		
	elif len(e1.get())!=0 and s==10 :

		
		myLabel16=Label(root,text=c4c2)
		myLabel16.pack()
		myButton["text"] = "Edit the story"
		myButton1["text"] = "Display"
		
				
		



		
        

	

	
    






   
           



 

       
     
myLabel12=Label(root, text = "Chapter")
myLabel12.pack()
myLabel21=Label(root, text=i)
myLabel21.pack()
                  
myLabel1=Label(root, text = "For a moment close your eyes and imagine you are a droplet, a droplet of clean blue water.......")
myLabel1.pack()

myLabel2=Label(root, text = "What do you want to call yourself ?")
myLabel2.pack()

e1=Entry(root,width=18)
e1.pack()

myLabel3=Label(root, text = "It's the time when you decide what are your strengths. So enter a trait for your strength")
myLabel3.pack()

e2=Entry(root,width=18)
e2.pack()

"""myLabel13=Label(root, text = "Just like the two sides of the coin you need to choose your weaknesses as well. Enter a trait for your weakness")
myLabel13.pack()

e3=Entry(root,width=18)
e3.pack()"""
                  



 
myButton=Button(root,text="Go Back",command=myClick1)
myButton.pack()

myButton1=Button(root,text=b2_txt,command=myClick2)
myButton1.pack()


myLabel1.pack(padx=(30), pady=(20))
myLabel2.pack(padx=(30), pady=(5))
myLabel3.pack(padx=(30), pady=(5))
"""myLabel13.pack(padx=(30), pady=(5))
myLabel12.pack(padx=(30), pady=(5))
myLabel21.pack(padx=(30), pady=(5))"""
myButton.pack(padx=(30), pady=(20))





root.mainloop()
