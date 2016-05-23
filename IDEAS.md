# Ideas 

Create a fork of the game and implement some of the features listed. Point values for each feature are in parentheses. More difficult/time-consuming features are worth more. You can earn up to 115 points out of 100 for the project. No credit will be given for partially completed features. Your final game submission must run without crashing. If any features do not work, remove them before turning your project in.

You may work in groups of 2 or 3 on this project. However, groups of 2 will receive a 15-point deduction and groups of 3 will receive a 25-point deduction. This does not mean that groups cannot earn 115 points. It just means that groups need to implement more features to get full/extra credit.


### Base features

1. Change the name of the game. Also change the file name for game.py to reflect the name of your game. (5)
2. Create many more aliens and arrange them in an interesting formation. The formation should be symmetrical and spacing between aliens should be uniform. The formation should be centered horizontally on the screen when the game starts. (10)
3. Edit the display_start_screen() function so that it displays the name of the game along with an interesting backdrop and the current high score. Make sure it also tells how to start the game. (5)
4. Edit the display_pause_screen() function so that it indicates that the game is in a paused state and tells how to resume playing. The pause text will overlay game objects, so make sure there is sufficient contrast. Also be sure that text is centered horizontally. (5)
5. Edit the display_end_screen() function so that it says Game Over and tells how to restart. The game over text will overlay game objects, so make sure there is sufficient contrast. Also be sure that text is centered horizontally. (5)
6. Edit the display_game_stats() function so that it displays the current score, high score, level, and shield strength. Be sure that the game stats are displayed in a way that they do not interfere with game play. (5)
7. Throughout game play, check to see if the current score is higher than the high score. If it is, update the high score to match the current score. (5)
8. Make the game immediately end if an alien touches either the ground or the cannon. (5)

### Art

1. Find your own artwork for the cannon, aliens, bullets, and bombs. Be sure that each image is cropped correctly and that each uses transparency. (5)
2. Create more interesting background scenery for the game. (5)
3. Find your own fonts to use. (5)
4. Make the shield strength display as a bar/meter rather than a number. (5)

### Sound

1. Make the HIT sound play when an alien is hit by a bullet. Find another sound to play when an cannon is hit by a bomb. (5)
2. Make the THEME music play in a loop while the game is in the PLAYING stage. (It is okay if the music continues to play while paused). Stop the music when the game ends. (5)
3. Replace the shot, hit, and theme with your own sounds. (5)
4. Find your own music to play during the start screen and end screens. Be sure that this does not play during other stages. (5)
5. Modify the game so that sounds will only play if sound_on setting is True. (5)
6. Create a function toggle_sound() which toggles the value of sound_on between True and False when the 's' key is pressed. When sound is not on, a mute icon should appear somewhere on the screen. (10)

### More Game Objects

1. Create a UFO object which flies across the top of the screen once per level. Randomly spawn the UFO at a location far off the screen so that it appears at an unpredictable time. Award more points for shooting the UFO than you do for regular aliens. (15)
2. Rework the Alien class so it has a shield much like the Cannon. Give the Alien a default shield of 1. When processing aliens, apply_damage of one. You'll also need to call a check_shield function in the Aliens update() which will kill the alien if it reaches a shield of zero. Now create a SuperAlien classs which extends Alien. SuperAliens have a default shield of 3. SuperAliens will take 3 shots to kill. Use a different image for SuperAliens. It is not necessary to create a new list of SuperAliens. They will update the same as regular Aliens, so just add them to the aliens list in setup. (15)
3. Create a power-up object that falls from the sky at a random time during each level. If the cannon catches the power-up, replenish the shield to 100. (15)
4. Create a power-up which doubles the shot limit for 4 seconds. There should be some type of visual indication that the shot limit power-up is being applied. (20)
5. Create a power-up which gives the cannon a invincibility to bombs for 4 seconds. There should be some type of visual indication that the invincibility power-up is being applied. (20)

### Miscellaneous 

1. Write a READ_ME file for the game which includes a backstory, describes the goal of the game, explains the controls, and gives point values/deducions for game events. (5)
2. Track the number shots taken and hits during the game. When the game ends, display the percentage of shots that were hits. (5)
3. Save the new high score to a data file at the end of the game. A function already exists to write the high score to a file. You just need to figure out how/where to use it. (5)
4. Use [pygame-xbox360controller](https://github.com/joncoop/pygame-xbox360controller) the game playable with a controller rather than a keyboard. Use the left stick to move the cannon and A to shoot. Be sure that features such as start, pause, and restart are also mapped to the controller. Don't forget to update display text to reflect controller settings. (20)
