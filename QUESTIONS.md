# Questions

The questions below are designed to get you to look at specific features of the code so you understand how the game works before you begin modifying the code. Answer the questions and turn them in by the due dates listed in Google Classroom.

1. What are the height and width of the game window? Where is the origin (0, 0) in a pygame window?
2. Describe how the objects in this game are layered during drawing.
3. What event results in the value 'done' getting set to True? What happens when done is True?
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
