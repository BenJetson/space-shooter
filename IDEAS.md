# Space-Shooter - Check your understanding.


## Questions...

0. What are the height and width of the game window? Where is the origin (0, 0) in a pygame window?
1. Describe how the objects in this game are layered during drawing.
2. What event results in the value 'done' getting set to False? What happens when done is False?
3. What key needs to be pressed to start the game? Where is the line of code that detects this key press?
4. When the game starts, there is a delay of '45 ticks' before objects start moving. How long is this in seconds? How did you calculate this?
5. What is the velocity of an Alien when the game starts? Remember, velocity has both a magnitude in pixels per refresh and a direction.
6. The game settings assign a bullet_speed to 6. Why is it that a positive value for bullet_speed makes the bullet travel up which is in a negative direction in the pygame coordinate plane?
7. What is the speed of an Alien after 4 levels have been cleared? How did you calculate this value.
8. Each time an Alien fleet hits the edge of the screen, the entire fleet moves down. How many pixels downward does the fleet move?
9. How many points are gained when an alien is shot? Where is the line of code that awards points for hitting an alien?
10. How may points are lost for shooting a bullet? Where is the line of code that deducts points?
11. What is the maximum number of bullets that can appear on the screen at once? How is this determined?
12. How much shield value does a cannon start with? How much shield value is lost when the cannon is hit by a bomb? How is this amount determined?
13. In the game loop, there are calls to the draw() function for Aliens, Bullets, Bombs, and theCannon. However there is no draw function in these classes. Why is it possible to call the draw function for these objects?
14. The Cannon class contains a move() function while the Alien, Bullet, and Bomb do not. Why doesn't the Cannon use the inherited move() function?
15. What is the probability that an Alien drops a bomb on a single iteration of the game loop while on level 1? How was this value calculated? What is the probability on level 10?
16. In your own words, explain how it is beneficial to break the game into multiple files unlike the previous game we made. Compare and contrast this code to previous code you have written in your explanation.
17. In your own words, explain how it is beneficial to create and extend objects. Compare and contrast this code to previous code you have written in your explanation.


## To try...

0. Come up with a name for the game.
1. Find your own artwork for the cannon, aliens, bullets, and bombs.
2. Create many more aliens and arrange them in an interesting formation.
3. Create more interesting background scenery during game play.
4. Edit the display_start_screen() function so that it displays the name of the game along with an interesting backdrop. Make sure it also tells how to start the game.
5. Edit the display_pause_screen() function so that it indicates that the game is in a paused state and tells how to resume playing. The pause text will overlay game objects, so make sure there is sufficient contrast.
6. Edit the display_game_stats() function so that it displays the current score, high score, level, and shield strength.
7. Make the shield display as a bar/meter rather than a number.
8. Edit the display_end_screen() function so that it says Game Over and tells how to restart. The game over text will be on top of the game objects, so make sure you have sufficient contrast.
9. Make the shot sound play when a shot is fired.
10. Make a hit sound play when an alien is shot.
11. Make theme music play in a loop when the game starts.
12. Find your own music to play during the start screen and end screen.
13. Use a conditional so that sound only plays if sound_on is set to True.
14. Throughout game play, check to see if the current score is higher than the high score. If it is, update the high score to match the current score. Save the new high score to a data file at the end of the game.
15. Have a power-up fall from the sky at periodic/random intervals (perhaps once per level). If the cannon collides with the power-up, replenish the shield to 100.
16. Create a power-up which temporarily raises the shot limit.
17. Create a power-up which gives the cannon a brief period of invincibility.
18. Make the game immediately end if an alien touches either the ground or the cannon.
19. Create a UFO object which flies across the top of the screen. Randomly spawn the UFO at a location far off the screen so that it appears at an unpredictable time. Award more points for shooting the UFO than you do for regular aliens.
20. Move the 'settings' out of the game.py file and into a settings.json file within a data folder. Then read the settings from the JSON file when the game loads.
21. Make the game playable with the XBox 360 controller rather than a keyboard.
22. Write a READ_ME file for the game which includes a backstory, describes the goal of the game, explains the controls, and gives point values/deducions for game events.
23. Rework the Alien class so it has a power much like the Cannon. Give the Alien a default power of 1. When processing aliens, apply_damage of one. You'll also need to call a check_power function in the Aliens update() which will kill the alien if it reaches a power of zero. Now create a SuperAlien classs which extends Aliend. SuperAliens have a default power of 2 or 3. SuperAliens will take 2-3 shots to kill. Use a different image for SuperAliens. It is not necessary to create a new list of SuperAliens. They will update the same as regular Aliens, so just add them to the aliens list in setup.