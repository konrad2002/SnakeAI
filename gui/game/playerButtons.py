# buttons for game with player slot

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle,Canvas,Ellipse,Color,Line

import math

class PlayerButtons (RelativeLayout):
    def __init__ (self, game, **kwargs):
        super(PlayerButtons, self).__init__(**kwargs)
        print("[game] created " + str(self.__class__))

        self.game = game

    def drawBackground(self):
        with self.canvas:
            self.canvas.clear()

            Color(.1, .2, .7, .5)
            self.sizeX = self.size[0]
            self.sizeY = self.size[1]
            self.bg = Rectangle(pos=(0, 0), size=(self.sizeX, self.sizeY))

            self.buttons = []

            self.readyBtn = Button(
                text = "Bereit",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.onReady
            )

            self.buttons.append(self.readyBtn)
            self.add_widget(self.readyBtn)

            self.readyBtn2 = Button(
                text = "Bereit",
                # pos = (0 , 0),
                # size_hint = (.1, .1),
                on_release = self.onReady
            )

            self.buttons.append(self.readyBtn2)
            self.add_widget(self.readyBtn2)



            self.key1Btn = Button(
                text = "W-A-S-D",
                # pos = (100 , 0),
                # size_hint = (.1, .1),
                on_release = lambda *args: self.onSetKeyboard(1)
            )
            self.key2Btn = Button(
                text = "Pfeiltasten",
                # pos = (200 , 0),
                # size_hint = (.1, .1),
                on_release = lambda *args: self.onSetKeyboard(2)
            )

            self.buttons.append(self.key1Btn)
            self.buttons.append(self.key2Btn)

            self.add_widget(self.key1Btn)
            self.add_widget(self.key2Btn)



            # calculation of button positions and size (depending on number of buttons)
            self.sqrt = math.sqrt(len(self.buttons))
            self.cols = round(self.sqrt + 0.4999)

            for i,button in enumerate(self.buttons):
                if self.game.main.settings.playerMode != 2:
                    button.size_hint = (
                        0.1,
                        ( 1 / self.cols - ( 0.30 / self.cols ) )
                    )
                else:
                    button.size_hint = (
                        1 / self.cols,
                        0.1
                    )

                row = round( ( i / self.cols ) + 0.50001 ) - 1
                col = i % self.cols

                button.pos = (
                    col * self.sizeX / self.cols, # x
                    row * self.sizeY / self.cols  #y
                )

                print("Button " + str(i) + ": " + str(col) + " | " + str(row))

    def onReady(self, a):
        self.game.ready()

    def onSetKeyboard(self, keyType):
        print("[KEYS] set keyboard for " + str(self.game.instance) + " to " + str(keyType))
        self.buttons[keyType - 1].color = (0,1,0,1)
        self.game.setKeyboard(keyType)