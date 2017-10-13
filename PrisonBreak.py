#Prison Break

#This is a quick command-line text adventure which takes input from the user to direct the story.

import time
import os

def intro():
	print("""
		 - The Prison Game -

		The object of this game is to escape the prison without being caught.

		Ready to begin? (y/n)
	  """)
	choice = input()
	if choice == 'y':
		cell_main()
	else:
		quit

#clears screen and places title
def prison_title():
	os.system('cls')
	print("""
		##################################################
		#      PPPPP RRRRR IIIII SSSSS  OOO  N    N      #			 
		#      P   P R   R   I   S     O   O N N  N      #					 
		#      PPPPP RRRRR   I   SSSSS O   O N  N N      #			 
		#      P     R  R    I       S O   O N   NN      #		 
		#      P     R   R IIIII SSSSS  OOO  N    N      #		 
		##################################################
				""")

#start
def cell_main():	
	prison_title()
	print("""
		You are in a prison cell. You've been here for 20 years for a crime you
		did not commit, and need to get out. There are some dirty bed sheets,
		a mirror by the sink, and the cell door is locked.

		Press S to inspect the Sheets
		Press L to inspect the Lock
		Press M to inspect the Mirror
				""")
	choice = input()
	if choice == 's':
		sheets_inspect()
	elif choice == 'l':
		cell_lock()
	elif choice == 'm':
		mirror_inspect()

def cell_with_mirror():
	prison_title()
	print("""
		You are in your cell with the mirror. You wonder how you could use this to
		escape. The gross sheets are still on the bed, and the cell door is locked.
		
		Press S to inspect the Sheets
		Press L to inspect the Lock
				""")
	choice = input()
	if choice == 's':
		sheets_with_mirror()
	elif choice == 'l':
		cell_lock_mirror()

def sheets_inspect():
	prison_title()
	print("""
		There are filthy, disgusting sheets on the bed.
		You can't believe you actually sleep in these. That's prison life...

		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell_main()

def sheets_with_mirror():
	prison_title()
	print("""
		You look at the same disgusting sheets again.
		Hopefully you won't have to look at them much longer.

		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell_mirror()

def mirror_inspect():
	prison_title()
	print("""
		As you look into the mirror yet again after 20 years, you suddenly notice that
		the mirror looks a little strange. You are compelled to take a closer look...
		
		Press L to Look closer
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'l':
		mirror_look()
	elif choice == 'r':
		cell_main()

def mirror_look():
	prison_title()
	print("""
		When you look at it from another angle, you can see that the mirror is loose.
		It looks like you can take it.

		Press T to Take the mirror
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 't':
		cell_with_mirror()
	elif choice == 'r':
		cell_main()

def cell_lock():
	prison_title()
	print("""
		It's one of those keypad locks. You have no idea what the combination is.
		You can't see the keypad from where you're standing. If you could look at it
		from the outside, you might be able to see which numbers were pressed by that
		slob guard's dirty hands.

		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell_main()

def cell_lock_mirror():
	prison_title()
	print("""
		It's one of those keypad locks. You have no idea what the combination is.
		Maybe now you can see which numbers were pressed by that slob guard's dirty hands.
		
		Press M to use Mirror
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'm':
		keypad()
	elif choice == 'r':
		cell_mirror()

def keypad():
	prison_title()
	print("""
		You reach your hand through the bars, and point the mirror back at the keypad.
		You can now see the combination to unlock it.
		
		Press K to use the Keypad
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'k':
		cell_escape()
	elif choice == 'r':
		cell_mirror()

def cell_escape():
	prison_title()
	print("""
		You escaped your cell! Now is your best chance to escape! There are some boxes
		to your left, and a closet door about 20 feet away. The hallway looks like it
		leads to some stairs.
		
		Press C to check the Closet
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_knob()
	elif choice == 's':
		stairs_guard()

def closet_knob():
	prison_title()
	print("""
		Just as you reach for the doorknob, you hear a guard coming down the hall. Your
		heart is pounding in your chest as you start to panic. You need to hide!
		""")
	time.sleep(3)
	print("""
		Press C to hide in the Closet
		Press B to hide behind the Boxes
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'c':
		closet_locked_guard()
	elif choice == 'b':
		boxes()
	elif choice == 'r':
		cell_hide()

def boxes():
	prison_title()
	print("""
		You hide behind the boxes as the guard closes in. He notices the cell door open
 		and runs over to inspect. It doesn't take him long to notice you behind the
 		boxes. Before you know it, you're surrounded by guards. There is no escape.
 		""")
	time.sleep(3)
	print("""
 		The guards cuff you, and escort you to the maximum security solitary cells. The head
 		guard says "There's no way you can escape now. You will die in this cell!"
 		""")
	time.sleep(5)
	print("""
		Press R to Restart the game
				""")
	choice = input()	
	if choice == 'r':
		cell_main()

def cell_hide():
	prison_title()
	print("""
		You are back in your cell. This should avoid suspicion from the gaurd.
		You sit on the bed with nasty sheets as the guards walks by. 

		You make eye-contact with him, and he suspiciously takes a look in your cell...
		""")
	time.sleep(5)
	print("""
		...shrugs, and walks back down the hall and up the stairs.

		Press S to inspect the Sheets
		Press H to go to the Hall
				""")
	choice = input()
	if choice == 's':
		sheets_gross()
	elif choice == 'h':
		hall_no_guard()

def closet_locked_guard():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.
		The guard is still coming! You don't have much time!
	
		Press B to hide behind the Boxes
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'b':
		boxes()
	elif choice == 'r':
		cell_hide()

def closet_locked_no_hairpin():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.

		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall_no_guard()

def closet_hairpin():
	prison_title()
	print("""
		The closet door is locked. You might be able to pick the lock with something.

		Press P to Pick the lock
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'p':
		closet_unlock()
	elif choice == 'r':
		hall_with_hairpin()

def closet_unlock():
	prison_title()
	print("""
		You pick the lock with the hairpin. The hairpin breaks, but the closet door opens.

		Press S to Search the closet
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 's':
		closet_uniform_off()
	elif choice == 'r':
		hall_closet_unlocked()

def closet_uniform_off():
	prison_title()
	print("""
		This closet is full of maintenance equipment. A spare janitor's uniform is hanging up.
		
		Press I to Inspect the uniform
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'i':
		uniform()
	elif choice == 'r':
		hall_closet_unlocked()

def closet_uniform_on():
	prison_title()
	print("""
		This closet is full of maintenance equipment. Nothing else useful here.
		
		Press C to Change out of uniform
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'c':
		closet_uniform_off()
	elif choice == 'r':
		hall_with_uniform()

def open_closet():
	prison_title()
	print("""
		The closet door is open.
		
		Press E to Enter the closet
		Press R to Return to the hall
		""")
	choice = input()
	if choice == 'e':
		closet_uniform_off()
	elif choice == 'r':
		hall_closet_unlocked()

def uniform():
	prison_title()
	print("""
		This uniform looks to be about your size.
		
		Press W to Wear the uniform
		Press R to Return to the closet
				""")
	choice = input()
	if choice == 'w':
		closet_janitor()
	elif choice == 'r':
		closet_open1()

def closet_janitor():
	prison_title()
	print("""
		You are now dressed as a janitor. This could be the perfect disguise.
		
		Press C Change out of the uniform
		Press R to Return to the closet
				""")
	choice = input()
	if choice == 'c':
		closet_uniform_off()
	elif choice == 'r':
		closet_uniform_on()

def stairs_guard():
	prison_title()
	print("""
		You start to motion towards the stairs, and you hear a guard coming down. Your
		heart is pounding in your chest as you start to panic. You need to hide!
		""")
	time.sleep(3)
	print("""
		Press C to hide in the Closet
		Press B to hide behind the Boxes
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'c':
		closet_locked_guard()
	elif choice == 'b':
		boxes()
	elif choice == 'r':
		cell_open()

def stairs_no_guard():
	prison_title()
	print("""
		You peek up the stairs, and see 2 doors. One leading outside, and the other to
		the guard's office. Trying to escape now is just asking to get shot. Better come
		up with a plan.
		
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall_no_guard()

def stairs_with_hairpin():
	prison_title()
	print("""
		You peek up the stairs, and see 2 doors. One leading outside, and the other to
		the guard's office. All you are armed with is a hairpin. Trying to escape now
		is just asking to get shot. Better come up with a plan.
		
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall_with_hairpin()

def stairs_closet_unlocked():
	prison_title()
	print("""
		You peek up the stairs, and see 2 doors. One leading outside, and the other to
		the guard's office. All you are armed with a broken hairpin. Trying to escape
		now is just asking to get shot. Better come up with a plan.

		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'r':
		hall_closet_unlocked()

def stairs_with_uniform():
	prison_title()
	print("""
		There are two doors upstairs. One leading outside, and the other to the guard's office.
		Being dressed as the janitor gives you the best chance yet to escape unnoticed.

		Press C to enter the Courtyard
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 'c':
		courtyard()
	elif choice == 'r':
		hall_with_uniform()

def sheets_gross():
	prison_title()
	print("""
		Ugh! You wonder why you keep looking at these. You have to get out of here!
		
		Press R to Return to your cell
				""")
	choice = input()
	if choice == 'r':
		cell_final()

def hall_no_guard():
	prison_title()
	print("""
		You are in the hallway outside the cell. The hallway leads to stairs, and
		there's a closet door about 20 feet away.

		Press C to check the Closet
		Press H to check the Hall
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_locked_no_hairpin()
	elif choice == 'h':
		hall_find_pin()
	elif choice == 's':
		stairs_no_guard()

def hall_find_pin():
	prison_title()
	print("""
		As you search the hallway, you come across a hairpin. This might come in handy.

		Press T to Take the hairpin
		Press R to Return to the hall
				""")
	choice = input()
	if choice == 't':
		hall_with_hairpin()
	elif choice == 'r':
		hall_no_guard()

def hall_with_hairpin():
	prison_title()
	print("""
		You are in the hallway outside the cell. The hallway leads to stairs, and
		there's a closet door about 20 feet away.

		Press C to check the Closet
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_hairpin()
	elif choice == 's':
		stairs_with_hairpin()

def hall_closet_unlocked():
	prison_title()
	print("""
		You are back in the hallway. Looks like the stairs are your way out.

		Press C to check the Closet
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		open_closet()
	elif choice == 's':
		stairs_closet_unlocked()

def hall_with_uniform():
	prison_title()
	print("""
		You are back in the hallway with the Janitor's uniform on.
		Looks like the stairs are your way out.

		Press C to check the Closet
		Press S to check the Stairs
				""")
	choice = input()
	if choice == 'c':
		closet_uniform_on()
	elif choice == 's':
		stairs_with_uniform()

def cell_final():
	prison_title()
	print("""
		Ok, this is it. The guard won't be back for a while, now is your last chance.
		You can almost feel the freedom.

		Press H to go to the Hallway.
				""")
	choice = input()
	if choice == 'h':
		hall_no_guard()

def courtyard():
	prison_title()
	print("""
		Nervously, you start to climb the stairs. Your hearts is pounding! As you walk
	  by the office, you make eye contact with one of the guards. He says "Hey!"
	  and your heart stops.
	  		""")
	time.sleep(4)
	print("""
		Press T to Talk to the guard
	  Press R to Run for it
				""")
	choice = input()
	if choice == 't':
		guard()
	elif choice == 'r':
		run()

def guard():
	prison_title()
	print("""
		The guards says "Have a good night," and nods to you. You can't believe
    that actually worked!
    
    Press C to enter the Courtyard.
				""")
	choice = input()
	if choice == 'c':
		courtyard()

def run():
	prison_title()
	print("""
		You panic and burst out the door as the guard chases you. The guard sounds the
	  alarm and signals to outside guards there's a prisoner on the loose. Both towers
	  have guns drawn on you as they take aim. The first bullet almost hits you in the
	  leg. 
	  """)
	time.sleep(3)
	print("""
	  You keep running. The gate is only 20 yards away, just a little further and
	  you're free! Suddenly, you fall to the ground as you feel your lower body go
	  completely numb. You've been shot. You can't move your legs. You take one last
	  look at the gate, just several feet away. You hear one final shot and everything
	  goes black.	  
				""")
	time.sleep(5)
	print("""
		Game Over!

		Press R to Restart
			""")
	choice = input()
	if choice == 'r':
		cell_main()

def courtyard():
	prison_title()
	print("""
		You wish the guard a good night, and enter the courtyard. Your heart
    is pounding out of your chest as you walk to the outer gate. You get to the
    gate, and look up at the tower.

    You think to yourself, "please open the gate..." The gate opens for you.
    You smile as you walk off the prison grounds. You are finally free!    
				""")
	time.sleep(10)
	print("""
		Press R to Restart
			""")
	choice = input()
	if choice == 'r':
		cell_main()

intro()