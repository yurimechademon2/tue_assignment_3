from tkinter import *
from random import randint, shuffle

# solution version 1: without extensions

def show_duo_names():
    print()
    print('┌─────────────────────┬───────────────────────┐')
    print('│ 0HV120 assignment 3 │ Memory Test           │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 1       │ name 1                │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 2       │ name 2                │')
    print('└─────────────────────┴───────────────────────┘')

class MemoryTestWindow:
    def __init__(self, root, msInvisible, msBetween, sequenceLength):
        self.root = root
        self.fontSize = 10
        self.fontFamily = "Helvetica"
        self.fontWeight = "bold"
        self.screenWidth = 1300
        self.defaultPadding = 20
        self.count = 5
        self.frame = None
        self.container1 = None
        self.container2 = None
        self.container3 = None
        self.container3Label1 = None
        self.container3Label2 = None
        self.container3Label3 = None
        self.container3Input1 = None
        self.container3Input2 = None
        self.container3Input3 = None
        self.topMessageBox = None
        self.countingMessage = None
        self.startBtn = None
        self.block1 = None
        self.block2 = None
        self.block3 = None
        self.block4 = None
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.blockContainer = None
        self.blockWidth = 300
        self.blockHeight = 300
        self.blockPadding = 20
        self.msInvisible = msInvisible
        self.msBetween = msBetween
        self.sequenceLength = sequenceLength
        self.blockColors = ["blue", "red", "green", "yellow"]
        self.observationalSequence = []
        self.recallSequence = []
        self.isObservationalPhase = True
        self.isSequenceCorrect = True
        self.defaultBg = "white"
        self.defaultInputBg = "lightgray"
        self.isFirstTry = True

    def initializeApp(self):
        self.initializeScreen()
        self.initializeWidgets()
        # if sequence lenth is 0... then it must be 1.
        if (self.sequenceLength == 0):
            self.sequenceLength = 1

    def initializeScreen(self):
        self.frame = Frame(self.root, width=self.screenWidth, height=500, bg=self.defaultBg)
        self.frame.pack_propagate(False)  
        self.frame.pack(padx=self.defaultPadding, pady=self.defaultPadding)

        self.container1 = Frame(self.frame, width=self.screenWidth, height=30, bg=self.defaultBg)
        self.container1.pack_propagate(False)  
        self.container1.pack()

        self.container2 = Frame(self.frame, width=self.screenWidth, height=400, bg=self.defaultBg)
        self.container2.pack_propagate(False)
        self.container2.pack(fill="both", expand=True)

        self.container3 = Frame(self.frame, width=self.screenWidth, height=200, bg=self.defaultBg)
        self.container3.pack_propagate(False)
        self.container3.pack()

        return

    def initializeWidgets(self):
        
        self.countingMessage = Label(self.container2, text="counting", font=(self.fontFamily, self.fontSize, self.fontWeight), bg=self.defaultBg)
        self.countingMessage.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window

        self.topMessageBox = Label(self.container1, bg=self.defaultBg, text="Click 'start' to begin the memory test.", font=(self.fontFamily, self.fontSize, self.fontWeight))
        self.topMessageBox.pack(side="top")  # Place the label at the top of the frame

        self.startBtn = Button(self.container3, text="Start", bg=self.defaultInputBg, font=(self.fontFamily, self.fontSize, self.fontWeight), command=self.startCounting)  # startBtn
        self.startBtn.grid(row=0, column=0)

        self.container3Label1 = Label(self.container3, bg=self.defaultBg, text="ms invisible: ", font=(self.fontFamily, self.fontSize, self.fontWeight))  # First label
        self.container3Label1.grid(row=0, column=1, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Label2 = Label(self.container3,bg=self.defaultBg, text="ms between: ", font=(self.fontFamily, self.fontSize, self.fontWeight))  # Second label
        self.container3Label2.grid(row=0, column=3, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Label3 = Label(self.container3,bg=self.defaultBg, text="sequence length", font=(self.fontFamily, self.fontSize, self.fontWeight))  # Third label
        self.container3Label3.grid(row=0, column=5, padx=self.defaultPadding, pady=self.defaultPadding)

        input1 = StringVar()
        input2 = StringVar()
        input3 = StringVar()
        input1.set(self.msInvisible) 
        input2.set(self.msBetween) 
        input3.set(self.sequenceLength) 

        self.container3Input1 = Entry(self.container3, bg=self.defaultInputBg, textvariable=input1, font=(self.fontFamily, self.fontSize, self.fontWeight))  # First input field
        self.container3Input1.grid(row=0, column=2, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input2 = Entry(self.container3, bg=self.defaultInputBg, textvariable=input2, font=(self.fontFamily, self.fontSize, self.fontWeight))  # Second input field
        self.container3Input2.grid(row=0, column=4,  padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input3 = Entry(self.container3, bg=self.defaultInputBg, textvariable=input3, font=(self.fontFamily, self.fontSize, self.fontWeight))  # Third input field
        self.container3Input3.grid(row=0, column=6, padx=self.defaultPadding, pady=self.defaultPadding)
    
    def countDown(self):
        for second in range(1):
        # for second in range(self.count):
            self.root.after(second*1000, self.countTostartObservationalPhase)

    def startCounting(self):
        self.topMessageBox.config(text="Counting down...")
        self.startBtn.config(state="disabled")
        self.countDown()

    def convertToDot(self):
        dots = ""
        for i in range(self.count-1):
            dots += '.'
        return dots

    def initializeBlocks(self):
        self.blockContainer = Frame(self.container2, width=800, height=700, bg=self.defaultBg)
        self.blockContainer.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window
        self.blockContainer.grid_rowconfigure(0, minsize=self.blockHeight)  # Set min height for row 0
        self.blockContainer.grid_rowconfigure(1, minsize=self.blockHeight)  # Set min height for row 1
        self.blockContainer.grid_columnconfigure(0, minsize=self.blockWidth)  # Set min width for column 0
        self.blockContainer.grid_columnconfigure(1, minsize=self.blockWidth)  # Set min width for column 1

        self.block1 = Frame(self.blockContainer, bg="blue")  
        self.block1.grid(row=0, column=0, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding)  

        self.block2 = Frame(self.blockContainer, bg="red")   
        self.block2.grid(row=0, column=1, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block3 = Frame(self.blockContainer, bg="green")   
        self.block3.grid(row=1, column=0, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block4 = Frame(self.blockContainer, bg="yellow")   
        self.block4.grid(row=1, column=1, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block1.grid_propagate(False)
        self.block2.grid_propagate(False)
        self.block3.grid_propagate(False)
        self.block4.grid_propagate(False)

        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.topMessageBox.config(text="Watch the sequence...")        
        self.bindBlocks()

        # if (self.isFirstTry == False):
        #     self.randomizeSequence()

    def startObservationalPhase(self):
        self.initializeBlocks()

    def randomizeSequence(self):
        shuffle(self.blockColors)
        for block in range(len(self.blocks)):
            self.blocks[block].config(bg=self.blockColors[block])

    def hideBlock(self, event):
        self.unbindBlocks()
        blockToBeHidden = event.widget
        blockToBeHidden.grid_remove()
        blockToBeHidden.after(self.msInvisible, lambda: self.showBlock(blockToBeHidden))

    def showBlock(self, block):
        block.grid()
        self.root.after(self.msBetween, lambda: self.managePhases(block))

    def managePhases(self, block):
        self.bindBlocks()
        if (self.isObservationalPhase):
            self.observationalSequence.append(block.cget("bg"))
            if (len(self.observationalSequence) == self.sequenceLength):
                # print (len(self.observationalSequence), self.sequenceLength)
                # begin recall phase
                self.isObservationalPhase = False
                self.topMessageBox.config(text="Repeat the sequence...")        
                # self.startRecallPhase()
        else:
            self.recallSequence.append(block.cget("bg"))
            if (len(self.recallSequence) == self.sequenceLength):
                self.endRecallPhase()

    def destroyBlocks(self):
        self.block1.destroy()
        self.block2.destroy()
        self.block3.destroy()
        self.block4.destroy()
        
    def endRecallPhase(self):
        if (self.recallSequence != self.observationalSequence):
            self.isSequenceCorrect = False

        self.block1.grid_remove()
        self.block2.grid_remove()
        self.block3.grid_remove()
        self.block4.grid_remove()

        self.countingMessage = Label(self.container2, text="", font=(self.fontFamily, self.fontSize, self.fontWeight), bg=self.defaultBg)
        self.countingMessage.place(relx=0.5, rely=0.5, anchor='center')
            # The next ’levels’ have to be started automatically (without the user
            # having to press start again), although there should be a delay of two
            # seconds to give the user the time to mentally prepare for the next
            # observation phase.

        if (self.isSequenceCorrect == True):
            self.countingMessage.config(text="Your sequence was correct.")    
            self.root.after(2000, self.toNextLevel)
        else:
            # Once the user does not click the right sequence display the following
            # message in the center of the canvas: ”you ended with a sequence of n”,
            # with n the current length of the sequence.
            self.countingMessage.config(text=f"You ended with a sequence of {self.sequenceLength}")
            self.root.after(2000, self.reset)
            
    def clean(self):
        self.recallSequence = []
        self.observationalSequence = []
        self.isObservationalPhase = True
        self.isSequenceCorrect = True
        self.topMessageBox.config(text="Watch the sequence...")        
        self.countingMessage.config(text="")
        self.block1.grid()
        self.block2.grid()
        self.block3.grid()
        self.block4.grid()

        # self.initializeBlocks()

    def reset(self):
        # If the user clicks the right sequence display, proceed with a sequence of
        # 2, and then a sequence of 3 etc.
        self.sequenceLength = 1
        self.isFirstTry = True
        self.block1.config(bg="blue")
        self.block2.config(bg="red")
        self.block3.config(bg="green")
        self.block4.config(bg="yellow")
        self.clean()           

    def toNextLevel(self):
        # If the user clicks the right sequence display, proceed with a sequence of
        # 2, and then a sequence of 3 etc.
        if (self.isSequenceCorrect):
            if (self.sequenceLength < 5):
                self.sequenceLength += 1
        self.isFirstTry = False
        self.randomizeSequence()
        self.clean()                

    def bindBlocks(self):
        self.block1.bind("<Button-1>", self.hideBlock)
        self.block2.bind("<Button-1>", self.hideBlock)
        self.block3.bind("<Button-1>", self.hideBlock)
        self.block4.bind("<Button-1>", self.hideBlock)

    def unbindBlocks(self):
        self.block1.unbind("<Button-1>")
        self.block2.unbind("<Button-1>")
        self.block3.unbind("<Button-1>")
        self.block4.unbind("<Button-1>")

    def countTostartObservationalPhase(self):
        if (self.count == 5):
            self.countingMessage.destroy()
            self.startObservationalPhase()
            return
        
        self.countingMessage.config(text=f"{self.convertToDot()}")
        self.count = self.count - 1

def main():
    msInvisible = 500
    msBetween = 500
    sequenceLength = 0

    show_duo_names()
    root = Tk()  
    window = MemoryTestWindow(root, msInvisible, msBetween, sequenceLength)
    root.title("Memory Test")
    window.initializeApp()
    root.mainloop()

main()