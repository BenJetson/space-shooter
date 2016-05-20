# Space-Shooter - Check your understanding.


## Questions...

1. What are the height and width of the game window? Where is the origin (0, 0) in a pygame window?
2. Describe how the objects in this game are layered during drawing.
3. What event results in the value 'done' getting set to False? What happens when done is False?
4. What key needs to be pressed to start the game? Where is the line of code that detects this key press?
5. When the game starts, there is a delay of '45 ticks' before objects start moving. How long is this in seconds? How did you calculate this?
6. What is the velocity of an Alien when the game starts? Remember, velocity has both a magnitude in pixels per refresh and a direction.
7. The game settings assign a bullet_speed to 6. Why is it that a positive value for bullet_speed makes the bullet travel up which is in a negative direction in the pygame coordinate plane?
8. What is the speed of an Alien after 4 levels have been cleared? How did you calculate this value.
9. Each time an Alien fleet hits the edge of the screen, the entire fleet moves down. How many pixels downward does the fleet move?
10. How many points are gained when an alien is shot? Where is the line of code that awards points for hitting an alien?
11. How may points are lost for shooting a bullet? Where is the line of code that deducts points?
12. What is the maximum number of bullets that can appear on the screen at once? How is this determined?
13. How much shield value does a cannon start with? How much shield value is lost when the cannon is hit by a bomb? How is this amount determined?
14. In the game loop, there are calls to the draw() function for Aliens, Bullets, Bombs, and theCannon. However there is no draw function in these classes. Why is it possible to call the draw function for these objects?
15. The Cannon class contains a move() function while the Alien, Bullet, and Bomb do not. Why doesn't the Cannon use the inherited move() function?
16. What is the probability that an Alien drops a bomb on a single iteration of the game loop while on level 1? How was this value calculated? What is the probability on level 10?
17. In your own words, explain how it is beneficial to break the game into multiple files unlike the previous game we made. Compare and contrast this code to previous code you have written in your explanation.
18. In your own words, explain how it is beneficial to create and extend objects. Compare and contrast this code to previous code you have written in your explanation.


## To try... (Point values are in parentheses.)

1. Change the name of the game. (5)
2. Find your own artwork for the cannon, aliens, bullets, and bombs. (5)
3. Create many more aliens and arrange them in an interesting formation. (5)
4. Create more interesting background scenery during game play. (5)
5. Edit the display_start_screen() function so that it displays the name of the game along with an interesting backdrop. Make sure it also tells how to start the game. (5)
6. Edit the display_pause_screen() function so that it indicates that the game is in a paused state and tells how to resume playing. The pause text will overlay game objects, so make sure there is sufficient contrast. (5)
7. Edit the display_game_stats() function so that it displays the current score, high score, level, and shield strength. (10)
8. Make the shield display as a bar/meter rather than a number. (10)
9. Edit the display_end_screen() function so that it says Game Over and tells how to restart. The game over text will be on top of the game objects, so make sure you have sufficient contrast. (5)
10. Make the shot sound play when a shot is fired.(5)
11. Make a hit sound play when an alien is shot. (5)
12. Make a sound play when an cannon is hit by a bomb. (5)
13. Make theme music play in a loop when the game starts. (5)
14. Find your own music to play during the start screen and end screen. (5)
15. Use a conditional so that sound only plays if sound_on is set to True. (5)
16. Throughout game play, check to see if the current score is higher than the high score. If it is, update the high score to match the current score. Save the new high score to a data file at the end of the game. Functions already exist to do this. You just need to figure out how to use them. (10)
17. Have a power-up fall from the sky at periodic/random intervals (perhaps once per level). If the cannon collides with the power-up, replenish the shield to 100. (15)
18. Create a power-up which temporarily raises the shot limit. (10)
19. Create a power-up which gives the cannon a brief period of invincibility. (10)
20. Make the game immediately end if an alien touches either the ground or the cannon. (5)
21. Create a UFO object which flies across the top of the screen. Randomly spawn the UFO at a location far off the screen so that it appears at an unpredictable time. Award more points for shooting the UFO than you do for regular aliens. (10)
22. Move the 'settings' out of the game.py file and into a settings.json file within a data folder. Then read the settings from the JSON file when the game loads. (15)
23. Make the game playable with the XBox 360 controller rather than a keyboard. (15)
24. Write a READ_ME file for the game which includes a backstory, describes the goal of the game, explains the controls, and gives point values/deducions for game events. (10)
25. Rework the Alien class so it has a power much like the Cannon. Give the Alien a default power of 1. When processing aliens, apply_damage of one. You'll also need to call a check_power function in the Aliens update() which will kill the alien if it reaches a power of zero. Now create a SuperAlien classs which extends Aliend. SuperAliens have a default power of 2 or 3. SuperAliens will take 2-3 shots to kill. Use a different image for SuperAliens. It is not necessary to create a new list of SuperAliens. They will update the same as regular Aliens, so just add them to the aliens list in setup. (15)
