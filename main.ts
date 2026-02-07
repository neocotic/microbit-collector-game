function collectItem () {
    if (player.isTouching(item)) {
        game.addScore(1)
        item.delete()
        spawnItem()
        basic.pause(200)
    }
}
input.onButtonPressed(Button.A, function () {
    if (game.isRunning()) {
        player.turn(Direction.Left, 90)
    }
})
input.onButtonPressed(Button.B, function () {
    if (game.isRunning()) {
        player.turn(Direction.Right, 90)
    }
})
function togglePause () {
    if (game.isGameOver()) {
        control.reset()
    } else if (game.isPaused()) {
        game.resume()
    } else {
        game.pause()
    }
}
function movePlayer () {
    if (player.isTouchingEdge()) {
        if (player.get(LedSpriteProperty.X) == 0 && player.get(LedSpriteProperty.Direction) == -90) {
            player.set(LedSpriteProperty.X, 4)
        } else if (player.get(LedSpriteProperty.X) == 4 && player.get(LedSpriteProperty.Direction) == 90) {
            player.set(LedSpriteProperty.X, 0)
        } else if (player.get(LedSpriteProperty.Y) == 0 && player.get(LedSpriteProperty.Direction) == 0) {
            player.set(LedSpriteProperty.Y, 4)
        } else if (player.get(LedSpriteProperty.Y) == 4 && player.get(LedSpriteProperty.Direction) == 180) {
            player.set(LedSpriteProperty.Y, 0)
        } else {
            player.move(1)
        }
    } else {
        player.move(1)
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    togglePause()
})
function spawnItem () {
    item = game.createSprite(randomFreeCoord(player.get(LedSpriteProperty.X)), randomFreeCoord(player.get(LedSpriteProperty.Y)))
    item.set(LedSpriteProperty.Brightness, 127)
    item.set(LedSpriteProperty.Blink, 200)
}
function randomFreeCoord (playerCoord: number) {
    randomCoord = randint(0, 4)
    while (randomCoord == playerCoord) {
        randomCoord = randint(0, 4)
    }
    return randomCoord
}
let randomCoord = 0
let item: game.LedSprite = null
let player: game.LedSprite = null
game.startCountdown(60000)
game.setScore(0)
player = game.createSprite(2, 2)
spawnItem()
basic.forever(function () {
    while (game.isRunning()) {
        movePlayer()
        collectItem()
        basic.pause(500)
    }
})
