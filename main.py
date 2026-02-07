def collectItem():
    if player.is_touching(item):
        game.add_score(1)
        item.delete()
        spawnItem()
        basic.pause(200)

def on_button_pressed_a():
    if game.is_running():
        player.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if game.is_running():
        player.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

def togglePause():
    if game.is_game_over():
        control.reset()
    elif game.is_paused():
        game.resume()
    else:
        game.pause()
def movePlayer():
    if player.is_touching_edge():
        if player.get(LedSpriteProperty.X) == 0 and player.get(LedSpriteProperty.DIRECTION) == -90:
            player.set(LedSpriteProperty.X, 4)
        elif player.get(LedSpriteProperty.X) == 4 and player.get(LedSpriteProperty.DIRECTION) == 90:
            player.set(LedSpriteProperty.X, 0)
        elif player.get(LedSpriteProperty.Y) == 0 and player.get(LedSpriteProperty.DIRECTION) == 0:
            player.set(LedSpriteProperty.Y, 4)
        elif player.get(LedSpriteProperty.Y) == 4 and player.get(LedSpriteProperty.DIRECTION) == 180:
            player.set(LedSpriteProperty.Y, 0)
        else:
            player.move(1)
    else:
        player.move(1)

def on_logo_pressed():
    togglePause()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def spawnItem():
    global item
    item = game.create_sprite(randomFreeCoord(player.get(LedSpriteProperty.X)),
        randomFreeCoord(player.get(LedSpriteProperty.Y)))
    item.set(LedSpriteProperty.BRIGHTNESS, 127)
    item.set(LedSpriteProperty.BLINK, 200)
def randomFreeCoord(playerCoord: number):
    global randomCoord
    randomCoord = randint(0, 4)
    while randomCoord == playerCoord:
        randomCoord = randint(0, 4)
    return randomCoord
randomCoord = 0
item: game.LedSprite = None
player: game.LedSprite = None
game.start_countdown(10000)
game.set_score(0)
player = game.create_sprite(2, 2)
spawnItem()

def on_forever():
    while game.is_running():
        movePlayer()
        collectItem()
        basic.pause(500)
basic.forever(on_forever)
