# menu for selection of one or two player slots

from gui.menu.slot import SlotMenu

from kivy.uix.widget import Widget
from kivy.uix.button import Button

class SubMenu (Widget):
    def __init__ (self, menuApp, **kwargs):
        super(SubMenu, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.menuApp = menuApp

        self.cols = 0
        self.rows = 0

        if self.menuApp.playerMode == 1:
            self.cols = 1
            self.rows = 1
        
        if self.menuApp.playerMode == 2:
            self.cols = 2
            self.rows = 1

        if self.menuApp.playerMode == 4:
            self.cols = 2
            self.rows = 2

        self.playerTypes = []
        self.slotBtns = []

        for i in range(self.menuApp.playerMode):
            self.playerTypes.append(0)
            j = i + 1
            if j == 1:
                x = 50
                y = 50
                if self.menuApp.playerMode == 4:
                    y = 145

            if j == 2:
                x = 200
                y = 50
                if self.menuApp.playerMode == 4:
                    y = 145

            if j == 3:
                x = 50
                y = 50

            if j == 4:
                x = 200
                y = 50

            slotBtn = Button(
                text="Spieler-Typ " + str(j) + "\n auswählen",
                pos=(
                    x,
                    y
                ),
                size=(
                    ( 300 / self.cols ),
                    ( 190 / self.rows )
                ),
                on_press=lambda *args: self.onSlotBtn(i)
            )

            self.slotBtns.append(slotBtn)
            self.add_widget(slotBtn)

    def onSlotBtn(self, value):
        self.slotMenu = SlotMenu(self, value)
        self.add_widget(self.slotMenu)

    def selectPlayerType(self, playerType, slot):
        self.slotBtns[slot].text = self.menuApp.mainController.settings.typeNames[playerType - 1]
        self.playerTypes[slot] = playerType
        self.menuApp.updatePlayerTypes()
        self.remove_widget(self.slotMenu)