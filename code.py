#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This program makes sprite move

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)  # insert at the top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()